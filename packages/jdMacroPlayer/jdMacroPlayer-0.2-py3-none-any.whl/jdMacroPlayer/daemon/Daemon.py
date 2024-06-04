from ..Constants import DBUS_DAEMON_SERVICE_NAME, SHORTCUT_TRIGGER
from ..core.action_types import get_action_type_by_id
from ..Functions import is_flatpak
from typing import TYPE_CHECKING
import jeepney.io.blocking
import configparser
import subprocess
import traceback
import threading
import tempfile
import jeepney
import secrets
import sys
import os


if TYPE_CHECKING:
    from ..Environment import Environment
    from ..core.Macro import Macro


class Deamon:
    def __init__(self, env: "Environment") -> None:
        self._env = env

        self._portal = jeepney.DBusAddress(
            object_path="/org/freedesktop/portal/desktop",
            bus_name="org.freedesktop.portal.Desktop",
        )
        self._global_shortcuts = self._portal.with_interface("org.freedesktop.portal.GlobalShortcuts")
        self._conn = jeepney.io.blocking.open_dbus_connection()

        with open(os.path.join(env.program_dir, "daemon", "Interface.xml"), "r", encoding="utf-8") as f:
            self._introspect_data = f.read()

        self._activated_macros: dict[str, bool] = {}
        self._running_macros: dict[str, bool] = {}

    def is_running(self) -> bool:
        address = jeepney.DBusAddress(
            bus_name="org.freedesktop.DBus",
            object_path="/org/freedesktop/DBus",
            interface="org.freedesktop.DBus",
        )

        req = jeepney.new_method_call(address, "ListNames", "", ())
        rep = self._conn.send_and_get_reply(req)

        return DBUS_DAEMON_SERVICE_NAME in rep.body[0]

    def prepare(self) -> None:
        rep = self._conn.send_and_get_reply(jeepney.bus_messages.message_bus.RequestName(DBUS_DAEMON_SERVICE_NAME))
        if rep.body[0] != 1:
           sys.exit(1)

        if is_flatpak():
            background = self._portal.with_interface("org.freedesktop.portal.Background")
            self._conn.send_and_get_reply(jeepney.new_method_call(background, "RequestBackground", "sa{sv}", ("", {"reason": ("s", "Run Daemon in Background")})))

    def open(self) -> None:
        token = secrets.token_hex()
        sender_name = self._conn.unique_name[1:].replace(".", "_")
        handle = f"/org/freedesktop/portal/desktop/request/{sender_name}/{token}"

        response_rule = jeepney.bus_messages.MatchRule(
            type="signal", interface="org.freedesktop.portal.Request", path=handle
        )
        jeepney.io.blocking.Proxy(jeepney.bus_messages.message_bus, self._conn).AddMatch(response_rule)

        with self._conn.filter(response_rule) as responses:
            req = jeepney.new_method_call(self._global_shortcuts, "CreateSession", "a{sv}", ({"handle_token": ("s", token), "session_handle_token": ("s", "Macros")},))

            self._conn.send_and_get_reply(req)
            resp = self._conn.recv_until_filtered(responses)
            self._session_handle = resp.body[1]["session_handle"][1]

    def _generate_ydotool_socket(self) -> None:
        socket_dir = tempfile.gettempdir()

        for i in os.listdir(socket_dir):
            if i.startswith("jdmacroplayer_ydotool_socket_"):
                os.remove(os.path.join(socket_dir, i))

        self._ydotool_socket = tempfile.mktemp(prefix="jdmacroplayer_ydotool_socket_", dir=socket_dir)
        os.environ["YDOTOOL_SOCKET"] = self._ydotool_socket

    def start_ydotoold(self) -> None:
        self._generate_ydotool_socket()

        if os.access("/dev/uinput", os.W_OK):
            self._ydotoold_pid = subprocess.Popen(["ydotoold", "-p", self._ydotool_socket, "-o", f"{os.getuid()}:{os.getuid()}"], cwd=os.path.expanduser("~")).pid
        elif is_flatpak():
            self._ydotoold_pid = subprocess.Popen(["flatpak-host-launch", "--pkexec", "ydotoold", "-p", self._ydotool_socket, "-o", f"{os.getuid()}:{os.getuid()}"], cwd=os.path.expanduser("~")).pid
        else:
            self._ydotoold_pid = subprocess.Popen(["pkexec", "--disable-internal-agent", "ydotoold", "-p", self._ydotool_socket, "-o", f"{os.getuid()}:{os.getuid()}"], cwd=os.path.expanduser("~")).pid

    def get_existing_shortcuts(self) -> list[str]:
        token = secrets.token_hex()
        sender_name = self._conn.unique_name[1:].replace(".", "_")
        handle = f"/org/freedesktop/portal/desktop/request/{sender_name}/{token}"

        response_rule = jeepney.bus_messages.MatchRule(
            type="signal", interface="org.freedesktop.portal.Request", path=handle
        )
        jeepney.io.blocking.Proxy(jeepney.bus_messages.message_bus, self._conn).AddMatch(response_rule)

        with self._conn.filter(response_rule) as responses:
            req = jeepney.new_method_call(self._global_shortcuts, "ListShortcuts", "oa{sv}", (self._session_handle, {"handle_token": ("s", token)}))
            self._conn.send_and_get_reply(req)
            resp = self._conn.recv_until_filtered(responses)

            shortcut_list: list[str] = []
            for i in resp.body[1]["shortcuts"][1]:
                shortcut_list.append(i[0])
            return shortcut_list

    def prepare_shortcuts(self) -> None:
        shortcut_list = self.get_existing_shortcuts()

        arg_list = []
        for macro in self._env.macro_manager.get_all_macros():
            if macro.id not in shortcut_list:
                arg_list.append((macro.id, {"description": ("s", macro.name)},))

        if len(arg_list) == 0:
            return

        args = (self._session_handle, arg_list, "", {})

        req = jeepney.new_method_call(self._global_shortcuts, "BindShortcuts", "oa(sa{sv})sa{sv}", args)
        self._conn.send_and_get_reply(req)

    def _execute_macro_internal(self, macro: "Macro") -> None:
        for action in macro.actions:
            action_type = action.get_type_object()

            if action_type is None:
                continue

            try:
                action_type.execute_action(self._env, action.config)
            except Exception:
                print(traceback.format_exc(), file=sys.stderr)

        self._running_macros[macro.id] = False

    def _execute_macro(self, macro: "Macro") -> None:
        if self._running_macros.get(macro.id, False):
            return

        thread = threading.Thread(target=self._execute_macro_internal, args=(macro,))
        self._running_macros[macro.id] = True
        thread.start()

    def _stop(self) -> None:
        try:
            subprocess.run(["kill", "-SIGTERM", str(self._ydotoold_pid)])
        except Exception:
            pass

        try:
            os.remove(self._ydotool_socket)
        except FileNotFoundError:
            pass

        sys.exit(0)

    def _test_execute_action_type(self, action_type_id: str) -> tuple[bool, str, str]:
        action_type = get_action_type_by_id(action_type_id)
        if action_type is None:
            return False, "Action type not found", ""

        try:
            config = action_type.get_test_config(action_type.get_current_config_version())
        except Exception:
            return False, "Failed to run get_test_config()", traceback.format_exc()

        try:
            action_type.execute_action(self._env, config)
        except Exception:
            return False, "Failed to run execute_action()", traceback.format_exc()

        return True, "", ""

    def _handle_interface(self, msg: jeepney.Message) -> None:
        match msg.header.fields[jeepney.HeaderFields.member]:
            case "ExecuteMacroByID":
                if len(msg.body) != 1:
                    self._conn.send_message(jeepney.new_error(msg, DBUS_DAEMON_SERVICE_NAME + ".Error.WrongArguments"))
                    return

                macro = self._env.macro_manager.get_macro_by_id(msg.body[0])
                if macro is None:
                    self._conn.send_message(jeepney.new_error(msg, DBUS_DAEMON_SERVICE_NAME + ".Error.MacroNotFound"))
                    return
                else:
                    self._conn.send_message(jeepney.new_method_return(msg, "", ()),)
                    self._execute_macro(macro)

            case "ExecuteMacroByName":
                if len(msg.body) != 1:
                    self._conn.send_message(jeepney.new_error(msg, DBUS_DAEMON_SERVICE_NAME + ".Error.WrongArguments"))
                    return

                macro = self._env.macro_manager.get_macro_by_name(msg.body[0])
                if macro is None:
                    self._conn.send_message(jeepney.new_error(msg, DBUS_DAEMON_SERVICE_NAME + ".Error.MacroNotFound"))
                    return
                else:
                    self._conn.send_message(jeepney.new_method_return(msg, "", ()),)
                    self._execute_macro(macro)

            case "Reload":
                self._env.macro_manager.load_file()
                self.prepare_shortcuts()
                self._conn.send_message(jeepney.new_method_return(msg, "", ()),)

            case "Stop":
                self._conn.send_message(jeepney.new_method_return(msg, "", ()),)
                self._stop()

            case "TestExecuteActionType":
                if len(msg.body) != 1:
                    self._conn.send_message(jeepney.new_error(msg, DBUS_DAEMON_SERVICE_NAME + ".Error.WrongArguments"))
                    return

                if not self._env.debug_mode:
                    self._conn.send_message(jeepney.new_error(msg, DBUS_DAEMON_SERVICE_NAME + ".Error.NoDebugMode", ("s"), ("This function is only aviable in debug mode",)))
                    return

                self._conn.send_message(jeepney.new_method_return(msg, "bss", self._test_execute_action_type(msg.body[0])))

            case "GetDebugInformation":
                self._conn.send_message(jeepney.new_method_return(msg, "a{ss}", ({
                    "version": self._env.version,
                    "data_dir": self._env.data_dir,
                    "program_dir": self._env.program_dir,
                },)),)

            case "Introspect":
                self._conn.send_message(jeepney.new_method_return(msg, "s", (self._introspect_data,)))

            case "Ping":
                self._conn.send_message(jeepney.new_method_return(msg, "", ()),)

            case "GetMachineId":
                machine_id = ""
                for current_file in ("/var/lib/dbus/machine-id", "/etc/machine-id"):
                    if os.path.isfile(current_file):
                        with open(current_file, "r", encoding="utf-8") as f:
                            machine_id = f.read().strip()
                            break
                self._conn.send_message(jeepney.new_method_return(msg, "s", (machine_id,)))

            case _:
                self._conn.send_message(jeepney.new_error(msg, DBUS_DAEMON_SERVICE_NAME + ".Error.InvalidMethod"))

    def _handle_signal(self, msg) -> None:
        signal_type = msg.header.fields[jeepney.HeaderFields.member]

        if signal_type not in ("Activated", "Deactivated"):
            return

        macro_id = msg.body[1]

        if signal_type == "Deactivated":
            try:
                del self._activated_macros[macro_id]
            except KeyError:
                pass

        macro = self._env.macro_manager.get_macro_by_id(macro_id)

        if macro is None:
            return

        if macro_id in self._activated_macros and macro.shortcut_trigger != SHORTCUT_TRIGGER.HOLD:
            return

        if signal_type == "Activated":
            self._activated_macros[macro_id] = True

        if signal_type == "Deactivated" and macro.shortcut_trigger == SHORTCUT_TRIGGER.RELEASED:
            self._execute_macro(macro)
        elif macro.shortcut_trigger != SHORTCUT_TRIGGER.RELEASED:
            self._execute_macro(macro)

    def listen(self) -> None:
        while True:
            msg = self._conn.receive()
            match msg.header.message_type:
                case jeepney.MessageType.method_call:
                    if msg.header.fields[jeepney.HeaderFields.destination] == DBUS_DAEMON_SERVICE_NAME:
                        self._handle_interface(msg)
                case jeepney.MessageType.signal:
                    if msg.header.fields[jeepney.HeaderFields.interface] == "org.freedesktop.portal.GlobalShortcuts":
                        self._handle_signal(msg)
