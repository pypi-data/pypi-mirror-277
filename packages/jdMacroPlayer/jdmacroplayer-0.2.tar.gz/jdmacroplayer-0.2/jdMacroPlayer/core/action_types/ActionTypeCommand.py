from PyQt6.QtWidgets import QWidget, QLabel, QPlainTextEdit, QCheckBox, QVBoxLayout
from typing import cast, Any, TYPE_CHECKING
from .ActionTypeBase import ActionTypeBase
from PyQt6.QtCore import QCoreApplication
from ...Functions import is_flatpak
import subprocess
import os


if TYPE_CHECKING:
    from ...Environment import Environment


class ActionTypeCommand(ActionTypeBase):
    def get_id(self) -> str:
        return "command"

    def get_name(self) -> str:
        return QCoreApplication.translate("ActionType", "Execute command")

    def get_config_widget(self, env: "Environment") -> QWidget:
        widget = QWidget()
        widget.text_edit = QPlainTextEdit()
        widget.wait_finish = QCheckBox(QCoreApplication.translate("ActionType", "Wait for command to finish"))

        layout = QVBoxLayout()
        layout.addWidget(QLabel(QCoreApplication.translate("ActionType", "Command:")))
        layout.addWidget(widget.text_edit)
        layout.addWidget(widget.wait_finish)

        widget.setLayout(layout)

        return widget

    def update_config_widget(self, widget: QWidget, config: Any) -> None:
        cast(QPlainTextEdit, widget.text_edit).setPlainText(config["command"])
        cast(QCheckBox, widget.wait_finish).setChecked(config["wait_finish"])

    def get_config_from_widget(self, widget: QWidget) -> Any:
        return {
            "command": cast(QPlainTextEdit, widget.text_edit).toPlainText(),
            "wait_finish": cast(QCheckBox, widget.wait_finish).isChecked(),
        }

    def get_list_text(self, config: Any) -> str:
        return QCoreApplication.translate("ActionType", "Execute command")

    def execute_action(self, env: "Environment", config: Any) -> None:
        if is_flatpak():
            command = ["flatpak-spawn", "--host", "sh", "-c", config["command"]]
        else:
            command = ["sh", "-c", config["command"]]

        if config["wait_finish"]:
            subprocess.run(command, cwd=os.path.expanduser("~"))
        else:
            subprocess.Popen(command, cwd=os.path.expanduser("~"))

    def get_current_config_version(self) -> int:
        return 1

    def upgrade_config(self, config_version: int, config: Any) -> Any:
        match config_version:
            case 0:
                return {"command": config, "wait_finish": True}

    def get_test_config(self, config_version: int) -> Any:
        match config_version:
            case 1:
                return {"command": "ls", "wait_finish": True}
            case 0:
                return "ls"
