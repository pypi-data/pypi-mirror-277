from ..Constants import DBUS_DAEMON_SERVICE_NAME, DBUS_DAEMON_INTERFACE_NAME
from .action_types import get_all_action_types, get_action_type_by_id
from .action_types.ActionTypeBase import ActionTypeBase
from PyQt6.QtWidgets import QWidget, QMenu, QMessageBox
from PyQt6.QtDBus import QDBusConnection, QDBusMessage
from typing import Any, TYPE_CHECKING
from PyQt6.QtGui import QAction
import traceback


if TYPE_CHECKING:
    from ..Environment import Environment


class ActionTypeTests:
    class TestType:
        Widget = 0
        ListText = 1
        Execute = 2
        Upgrade = 3
        All = 4

    @staticmethod
    def prepare_menu(env: "Environment", test_type: int, menu: QMenu, parent: QWidget) -> None:
        menu.clear()

        action_types = get_all_action_types()
        action_id_list: list[str] = []

        for current_action in action_types:
            menu_action = QAction(current_action.get_name(), parent)
            menu_action.setData({"type": test_type, "actions": [current_action.get_id()]})
            menu_action.triggered.connect(lambda: ActionTypeTests._menu_action_clicked(env, parent))
            action_id_list.append(current_action.get_id())
            menu.addAction(menu_action)

        menu.addSeparator()

        all_action = QAction("All", parent)
        all_action.setData({"type": test_type, "actions": action_id_list})
        all_action.triggered.connect(lambda: ActionTypeTests._menu_action_clicked(env, parent))
        menu.addAction(all_action)

    def _menu_action_clicked(env: "Environment", parent: QWidget) -> None:
        data: dict[str, Any] = parent.sender().data()

        ok = True

        for i in data["actions"]:
            action_type = get_action_type_by_id(i)
            result = ActionTypeTests.run_test(env, data["type"], action_type)
            if not result[0]:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Critical)
                msg_box.setWindowTitle("Test failed")
                msg_box.setText(f"Test failed for {action_type.get_name()}<br><br>{result[1]}")

                if result[2] is not None:
                    msg_box.setDetailedText(result[2])

                msg_box.exec()

                ok = False

        if ok:
            QMessageBox.information(None, "Test passed", "The test has sucessfully passed")

    @staticmethod
    def _run_widget_test(env: "Environment", action_type: ActionTypeBase) -> tuple[bool, str | None, str | None]:
        try:
            widget = action_type.get_config_widget(env)
        except Exception:
            return False, "Failed to run get_config_widget()", traceback.format_exc()

        try:
            test_config = action_type.get_test_config(action_type.get_current_config_version())
        except Exception:
            return False, "Failed to run get_test_config()", traceback.format_exc()

        try:
            action_type.update_config_widget(widget, test_config)
        except Exception:
            return False, "Failed to run update_config_widget()", traceback.format_exc()

        try:
            widget_config = action_type.get_config_from_widget(widget)
        except Exception:
            return False, "Failed to run get_config_from_widget()", traceback.format_exc()

        if test_config != widget_config:
            return False, "Widget returned wrong config", None

        return True, None, None

    @staticmethod
    def _run_list_text_test(action_type: ActionTypeBase) -> tuple[bool, str | None, str | None]:
        try:
            config = action_type.get_test_config(action_type.get_current_config_version())
        except Exception:
            return False, "Failed to run get_test_config()", traceback.format_exc()

        try:
            list_text = action_type.get_list_text(config)
        except Exception:
            return False, "Failed to run get_list_text()", traceback.format_exc()

        if not isinstance(list_text, str):
            return False, "List text is not a string", None

        return True, None, None

    @staticmethod
    def _run_execute_test(action_type: ActionTypeBase) -> tuple[bool, str | None, str | None]:
        msg = QDBusMessage.createMethodCall(DBUS_DAEMON_SERVICE_NAME, "/", DBUS_DAEMON_INTERFACE_NAME, "TestExecuteActionType")
        msg.setArguments([action_type.get_id()])
        result = QDBusConnection.sessionBus().call(msg)

        if result.errorMessage() != "":
            return False, result.errorMessage(), None

        return tuple(result.arguments())

    @staticmethod
    def _run_upgrade_test(action_type: ActionTypeBase) -> tuple[bool, str | None, str | None]:
        try:
            version = action_type.get_current_config_version()
        except Exception:
            return False, "Failed to run get_current_config_version()", traceback.format_exc()

        for i in range(0,version):
            try:
                config = action_type.get_test_config(i)
            except Exception:
                return False, f"Failed to run get_test_config() for version {i}", traceback.format_exc()

            try:
                config = action_type.upgrade_config(i, config)
            except Exception:
                return False, f"Failed to run upgrade_config() for version {i}", traceback.format_exc()

            if i != action_type.get_current_config_version():
                try:
                    new_config = action_type.get_test_config(i + 1)
                except Exception:
                    return False, f"Failed to run get_test_config() for version {i + 1}", traceback.format_exc()

                if config != new_config:
                    return False, f"Upgrade for version {i} failed", None

        return True, None, None

    @staticmethod
    def _run_all_tests(env: "Environment", action_type: ActionTypeBase) -> tuple[bool, str | None, str | None]:
        for current_test in (ActionTypeTests.TestType.Widget, ActionTypeTests.TestType.ListText, ActionTypeTests.TestType.Execute, ActionTypeTests.TestType.Upgrade):
            result = ActionTypeTests.run_test(env, current_test, action_type)
            if not result[0]:
                return result
        return True, None, None

    @staticmethod
    def run_test(env: "Environment", test_type: int, action_type: ActionTypeBase) -> tuple[bool, str | None, str | None]:
        match test_type:
            case ActionTypeTests.TestType.Widget:
                return ActionTypeTests._run_widget_test(env, action_type)
            case ActionTypeTests.TestType.ListText:
                return ActionTypeTests._run_list_text_test(action_type)
            case ActionTypeTests.TestType.Execute:
                return ActionTypeTests._run_execute_test(action_type)
            case ActionTypeTests.TestType.Upgrade:
                return ActionTypeTests._run_upgrade_test(action_type)
            case ActionTypeTests.TestType.All:
                return ActionTypeTests._run_all_tests(env, action_type)
