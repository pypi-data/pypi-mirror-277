from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QLabel, QMessageBox
from ..Constants import DBUS_DAEMON_SERVICE_NAME, DBUS_DAEMON_INTERFACE_NAME
from PyQt6.QtDBus import QDBusConnection, QDBusMessage, QDBusArgument
from PyQt6.QtCore import QCoreApplication, QMetaType, pyqtSlot
from ..core.ActionTypeTests import ActionTypeTests
from .AddEditMacroDialog import AddEditMacroDialog
from ..ui_compiled.MainWindow import Ui_MainWindow
from .SettingsDialog import SettingsDialog
from .WelcomeDialog import WelcomeDialog
from .AboutDialog import AboutDialog
from PyQt6.QtGui import QCloseEvent
from ..Functions import is_flatpak
from typing import TYPE_CHECKING
import configparser
import subprocess
import webbrowser
import shutil
import sys
import os


if TYPE_CHECKING:
    from ..Environment import Environment


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, env: "Environment") -> None:
        super().__init__()

        self.setupUi(self)

        self._env = env

        self._dbus_connection = QDBusConnection.sessionBus()

        self._daemon_running_label = QLabel()
        self.statusBar().addPermanentWidget(self._daemon_running_label)

        if shutil.which("jdmacroplayer-daemon") is None:
            self.autostart_daemon_action.setVisible(False)

        self._update_macro_list()
        self._update_daemon_running()
        self._update_udev_rule_action_text()

        self._dbus_connection.connect("org.freedesktop.DBus", "/org/freedesktop/DBus", "org.freedesktop.DBus", "NameOwnerChanged", self._dbus_name_owner_changed)

        if env.debug_mode:
            ActionTypeTests.prepare_menu(env, ActionTypeTests.TestType.Widget, self.debug_action_tests_widget_menu, self)
            ActionTypeTests.prepare_menu(env, ActionTypeTests.TestType.ListText, self.debug_action_tests_list_text_menu, self)
            ActionTypeTests.prepare_menu(env, ActionTypeTests.TestType.Execute, self.debug_action_tests_execute_menu, self)
            ActionTypeTests.prepare_menu(env, ActionTypeTests.TestType.Upgrade, self.debug_action_tests_upgrade_menu, self)
            ActionTypeTests.prepare_menu(env, ActionTypeTests.TestType.All, self.debug_action_tests_all_menu, self)
            self.open_data_directory_action.triggered.connect(lambda: subprocess.run(["xdg-open", env.data_dir]))
        else:
            self.debug_menu.menuAction().setVisible(False)

        self.exit_action.triggered.connect(lambda: sys.exit(0))

        self.start_daemon_action.triggered.connect(self._start_daemon)
        self.stop_daemon_action.triggered.connect(self._stop_daemon)
        self.udev_rule_action.triggered.connect(self._udev_rule_action_clicked)
        self.autostart_daemon_action.triggered.connect(self._autostart_daemon_action_clicked)

        self.settings_action.triggered.connect(self._settings_action_clicked)

        self.welcome_dialog_action.triggered.connect(self.open_welcome_dialog)
        self.view_source_action.triggered.connect(lambda: webbrowser.open("https://codeberg.org/JakobDev/jdMacroPlayer"))
        self.report_bug_action.triggered.connect(lambda: webbrowser.open("https://codeberg.org/JakobDev/jdMacroPlayer/issues"))
        self.view_documentation_action.triggered.connect(lambda: webbrowser.open("https://jdmacroplayer.readthedocs.io"))
        self.translate_action.triggered.connect(lambda: webbrowser.open("https://translate.codeberg.org/projects/jdMacroPlayer"))
        self.donate_action.triggered.connect(lambda: webbrowser.open("https://ko-fi.com/jakobdev"))
        self.about_action.triggered.connect(lambda: AboutDialog(self, self._env).exec())
        self.about_qt_action.triggered.connect(env.app.aboutQt)

        self.macro_list.currentItemChanged.connect(self._update_macro_buttons_enabled)

        self.add_macro_button.clicked.connect(self._add_macro_button_clicked)
        self.edit_macro_button.clicked.connect(self._edit_macro_button_clicked)
        self.delete_macro_button.clicked.connect(self._delete_macro_button_clicked)
        self.execute_macro_button.clicked.connect(self._execute_macro_button_clicked)

        if env.debug_mode:
            msg = QDBusMessage.createMethodCall(DBUS_DAEMON_SERVICE_NAME, "/", DBUS_DAEMON_INTERFACE_NAME, "Stop")
            self._dbus_connection.call(msg)
            subprocess.Popen([sys.executable, "-m", "jdMacroPlayer.daemon", "--debug"], cwd=os.path.dirname(self._env.program_dir))

    def _update_daemon_running(self) -> None:
        msg = QDBusMessage.createMethodCall("org.freedesktop.DBus", "/org/freedesktop/DBus", "org.freedesktop.DBus", "ListNames")
        response = self._dbus_connection.call(msg)

        if response.errorMessage() != "":
            print(response.errorMessage(), file=sys.stderr)
            return

        self._is_daemon_running = DBUS_DAEMON_SERVICE_NAME in response.arguments()[0]

        if self._is_daemon_running:
            self.start_daemon_action.setEnabled(False)
            self.stop_daemon_action.setEnabled(True)
            self._daemon_running_label.setText(QCoreApplication.translate("MainWindow", "The daemon is running"))
        else:
            self.start_daemon_action.setEnabled(True)
            self.stop_daemon_action.setEnabled(False)
            self._daemon_running_label.setText(QCoreApplication.translate("MainWindow", "The daemon is not running"))

    @pyqtSlot(QDBusMessage)
    def _dbus_name_owner_changed(self, msg: QDBusMessage) -> None:
        if msg.arguments()[0] == DBUS_DAEMON_SERVICE_NAME:
            self._update_daemon_running()

    def _start_daemon(self) -> None:
        subprocess.Popen([sys.executable, "-m", "jdMacroPlayer.daemon"], cwd=os.path.dirname(self._env.program_dir))

    def _stop_daemon(self) -> None:
        msg = QDBusMessage.createMethodCall(DBUS_DAEMON_SERVICE_NAME, "/", DBUS_DAEMON_INTERFACE_NAME, "Stop")
        self._dbus_connection.asyncCall(msg)

    def _reload_daemon(self) -> None:
        msg = QDBusMessage.createMethodCall(DBUS_DAEMON_SERVICE_NAME, "/", DBUS_DAEMON_INTERFACE_NAME, "Reload")
        self._dbus_connection.asyncCall(msg)

    def _is_udev_rule_installed(self) -> bool:
        if is_flatpak():
            return os.path.isfile("/run/host/etc/udev/rules.d/jdmacroplayer-ydotool.rule")
        else:
            return os.path.isfile("/etc/udev/rules.d/jdmacroplayer-ydotool.rule")

    def _update_udev_rule_action_text(self) -> None:
        if self._is_udev_rule_installed():
            self.udev_rule_action.setText(QCoreApplication.translate("MainWindow", "Uninstall udev rule"))
        else:
            self.udev_rule_action.setText(QCoreApplication.translate("MainWindow", "Install udev rule"))

    def _udev_rule_action_clicked(self) -> None:
        if self._is_udev_rule_installed():
            self._uninstall_udev_rule()
        else:
            self._install_udev_rule()

    def _install_udev_rule(self) -> None:
        text = QCoreApplication.translate("MainWindow", "This will install a custom udev rule that will allow jdMacroPlayer to run without root.") + "<br><br>"
        text += QCoreApplication.translate("MainWindow", "This will allow any Program to create fake input without root, so use it at your own risk.") + "<br><br>"
        text += QCoreApplication.translate("MainWindow", "Do you want to install this rule?")

        answer = QMessageBox.question(self, QCoreApplication.translate("MainWindow", "Install udev rule"), text,  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if answer != QMessageBox.StandardButton.Yes:
            return

        rule_path = os.path.join(self._env.program_dir, "data", "jdmacroplayer-ydotool.rule")

        if is_flatpak():
            config = configparser.ConfigParser()
            config.read("/.flatpak-info")
            app_path = config["Instance"]["app-path"]
            rule_path = os.path.join(app_path, rule_path.removeprefix("/app/"))
            subprocess.run(["flatpak-spawn", "--host", "pkexec", "--disable-internal-agent", "install", "-Dm644", rule_path, "-t", "/etc/udev/rules.d"])
        else:
            subprocess.run(["pkexec", "--disable-internal-agent", "install", "-Dm644", rule_path, "-t", "/etc/udev/rules.d"])

        if self._is_udev_rule_installed():
            QMessageBox.information(
                self,
                QCoreApplication.translate("MainWindow", "Rule installed"),
                QCoreApplication.translate("MainWindow", "The rule was successfully installed. You may need to restart your system to take effect."),
            )
        else:
            QMessageBox.critical(
                self,
                QCoreApplication.translate("MainWindow", "Installation failed"),
                QCoreApplication.translate("MainWindow", "The rule could not be installed"),
            )

        self._update_udev_rule_action_text()

    def _uninstall_udev_rule(self) -> None:
        answer = QMessageBox.question(
            self,
            QCoreApplication.translate("MainWindow", "Install udev rule"),
            QCoreApplication.translate("MainWindow", "This will uninstall the udev rule. Are you sure?"),
        )

        if answer != QMessageBox.StandardButton.Yes:
            return

        if is_flatpak():
            subprocess.run(["flatpak-spawn", "--host", "pkexec", "--disable-internal-agent", "rm", "/etc/udev/rules.d/jdmacroplayer-ydotool.rule"])
        else:
            subprocess.run(["pkexec", "--disable-internal-agent", "rm", "/etc/udev/rules.d/jdmacroplayer-ydotool.rule"])

        if not self._is_udev_rule_installed():
            QMessageBox.information(
                self,
                QCoreApplication.translate("MainWindow", "Rule uninstalled"),
                QCoreApplication.translate("MainWindow", "The rule was successfully uninstalled. You may need to restart your system to take effect."),
            )
        else:
              QMessageBox.critical(
                self,
                QCoreApplication.translate("MainWindow", "Uninstallation failed"),
                QCoreApplication.translate("MainWindow", "The rule could not be uninstalled"),
            )

        self._update_udev_rule_action_text()

    def _autostart_daemon_action_clicked(self) -> None:
        arr = QDBusArgument()
        arr.beginArray(QMetaType.Type.QString.value)
        arr.add("jdmacroplayer-daemon", QMetaType.Type.QString.value)
        arr.endArray()

        msg = QDBusMessage.createMethodCall("org.freedesktop.portal.Desktop", "/org/freedesktop/portal/desktop", "org.freedesktop.portal.Background", "RequestBackground")
        msg.setArguments([
            "",
            {
                "reason": QCoreApplication.translate("MainWindow", "Add Daemon to Autostart"),
                "autostart": True,
                "commandline": arr,
            }
        ])
        self._dbus_connection.call(msg)

        QMessageBox.information(
            self,
            QCoreApplication.translate("MainWindow", "Added to Autostart"),
            QCoreApplication.translate("MainWindow", "The daemon was added to the Autostart"),
         )

    def _update_macro_buttons_enabled(self) -> None:
        enabled = self.macro_list.currentItem() is not None
        self.edit_macro_button.setEnabled(enabled)
        self.delete_macro_button.setEnabled(enabled)
        self.execute_macro_button.setEnabled(enabled)

    def _add_macro_button_clicked(self) -> None:
        dialog = AddEditMacroDialog(self, self._env, self._env.macro_manager.create_new_macro())
        dialog.open_dialog()
        self._update_macro_list()

        if self._is_daemon_running:
            self._reload_daemon()

    def _edit_macro_button_clicked(self) -> None:
        macro = self._env.macro_manager.get_macro_by_id(self.macro_list.currentItem().data(42))
        dialog = AddEditMacroDialog(self, self._env, macro)
        dialog.open_dialog()
        self._update_macro_list()

        if self._is_daemon_running:
            self._reload_daemon()

    def _delete_macro_button_clicked(self) -> None:
        self._env.macro_manager.delete_macro_by_id(self.macro_list.currentItem().data(42))
        self._update_macro_list()

        if self._is_daemon_running:
            self._reload_daemon()

    def _execute_macro_button_clicked(self) -> None:
        if not self._is_daemon_running:
            QMessageBox.critical(
                self,
                QCoreApplication.translate("MainWindow", "Daemon not running"),
                QCoreApplication.translate("MainWindow", "The daemon needs to be running to execute a Macro"),
            )
            return

        msg = QDBusMessage.createMethodCall(DBUS_DAEMON_SERVICE_NAME, "/", DBUS_DAEMON_INTERFACE_NAME, "ExecuteMacroByID")
        msg.setArguments([self.macro_list.currentItem().data(42)])
        self._dbus_connection.call(msg)

    def _update_macro_list(self) -> None:
        self.macro_list.clear()
        for macro in self._env.macro_manager.get_all_macros():
            item = QListWidgetItem(macro.name)
            item.setData(42, macro.id)
            self.macro_list.addItem(item)
        self._update_macro_buttons_enabled()

    def _settings_action_clicked(self) -> None:
        dialog = SettingsDialog(self, self._env)
        dialog.exec()

    def open_welcome_dialog(self) -> None:
        dialog = WelcomeDialog(self, self._env)
        dialog.exec()

    def closeEvent(self, event: QCloseEvent | None) -> None:
        if self._env.debug_mode:
            self._stop_daemon()

        return super().closeEvent(event)
