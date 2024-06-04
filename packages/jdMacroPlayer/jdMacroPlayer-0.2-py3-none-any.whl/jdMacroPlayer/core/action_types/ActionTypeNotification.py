from PyQt6.QtWidgets import QWidget, QLineEdit, QComboBox, QPlainTextEdit, QLabel, QSizePolicy, QFormLayout, QVBoxLayout
from ...Functions import select_combo_box_data
from typing import cast, Any, TYPE_CHECKING
from .ActionTypeBase import ActionTypeBase
from PyQt6.QtCore import QCoreApplication
import jeepney.io.blocking
import jeepney
import secrets


if TYPE_CHECKING:
    from ...Environment import Environment


class ActionTypeNotification(ActionTypeBase):
    def get_id(self) -> str:
        return "notification"

    def get_name(self) -> str:
        return QCoreApplication.translate("ActionType", "Show Notification")

    def get_config_widget(self, env: "Environment") -> QWidget:
        widget = QWidget()
        widget.title_edit = QLineEdit()
        widget.priority_box = QComboBox()
        widget.body_edit = QPlainTextEdit()

        cast(QComboBox, widget.priority_box).setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        cast(QComboBox, widget.priority_box).addItem(QCoreApplication.translate("ActionType", "Low", "Priority"), "low")
        cast(QComboBox, widget.priority_box).addItem(QCoreApplication.translate("ActionType", "Normal", "Priority"), "normal")
        cast(QComboBox, widget.priority_box).addItem(QCoreApplication.translate("ActionType", "High", "Priority"), "high")
        cast(QComboBox, widget.priority_box).addItem(QCoreApplication.translate("ActionType", "Urgent", "Priority"), "urgent")

        select_combo_box_data(widget.priority_box, "normal")

        form_layout = QFormLayout()
        form_layout.addRow(QLabel(QCoreApplication.translate("ActionType", "Title:")), widget.title_edit)
        form_layout.addRow(QLabel(QCoreApplication.translate("ActionType", "Priority:")), widget.priority_box)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(QLabel(QCoreApplication.translate("ActionType", "Text:")))
        main_layout.addWidget(widget.body_edit)

        widget.setLayout(main_layout)

        return widget

    def update_config_widget(self, widget: QWidget, config: Any) -> None:
        cast(QLineEdit, widget.title_edit).setText(config.get("title", ""))
        select_combo_box_data(widget.priority_box, config.get("priority", "normal"))
        cast(QPlainTextEdit, widget.body_edit).setPlainText(config.get("body", ""))

    def get_config_from_widget(self, widget: QWidget) -> Any:
        return {
            "title": cast(QLineEdit, widget.title_edit).text(),
            "priority": cast(QComboBox, widget.priority_box).currentData(),
            "body": cast(QPlainTextEdit, widget.body_edit).toPlainText(),
        }

    def get_list_text(self, config: Any) -> str:
        return QCoreApplication.translate("ActionType", "Show Notification") + " " + config.get("title", "")

    def execute_action(self, env: "Environment", config: Any) -> None:
        address = jeepney.DBusAddress(
            bus_name="org.freedesktop.portal.Desktop",
            object_path="/org/freedesktop/portal/desktop",
            interface="org.freedesktop.portal.Notification",
        )

        with jeepney.io.blocking.open_dbus_connection() as conn:
            req = jeepney.new_method_call(address, "AddNotification", "sa{sv}", (
                secrets.token_hex(),
                {
                    "title": ("s", config.get("title", "")),
                    "body": ("s", config.get("body", "")),
                    "priority": ("s", config.get("priority", "normal")),
                }
            ))
            conn.send_and_get_reply(req)

    def get_test_config(self, config_version: int) -> Any:
        match config_version:
            case 0:
                return {"title": "Title", "body": "Body", "priority": "normal"}
