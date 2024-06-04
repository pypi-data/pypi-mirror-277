from PyQt6.QtWidgets import QWidget, QDoubleSpinBox, QLabel, QHBoxLayout, QVBoxLayout
from typing import cast, Any, TYPE_CHECKING
from .ActionTypeBase import ActionTypeBase
from PyQt6.QtCore import QCoreApplication
import time


if TYPE_CHECKING:
    from ...Environment import Environment


class ActionTypeSleep(ActionTypeBase):
    def get_id(self) -> str:
        return "sleep"

    def get_name(self) -> str:
        return QCoreApplication.translate("ActionType", "Sleep")

    def get_config_widget(self, env: "Environment") -> QWidget:
        widget = QWidget()

        widget.spin_box = QDoubleSpinBox()

        spin_box_layout = QHBoxLayout()
        spin_box_layout.addWidget(QLabel(QCoreApplication.translate("ActionType", "Seconds:")))
        spin_box_layout.addWidget(widget.spin_box)

        main_layout = QVBoxLayout()
        main_layout.addLayout(spin_box_layout)
        main_layout.addStretch(1)
        main_layout.setContentsMargins(0, 0, 0, 0)

        widget.setLayout(main_layout)

        return widget

    def update_config_widget(self, widget: QWidget, config: Any) -> None:
        cast(QDoubleSpinBox, widget.spin_box).setValue(config)

    def get_config_from_widget(self, widget: QWidget) -> Any:
        return cast(QDoubleSpinBox, widget.spin_box).value()

    def get_list_text(self, config: Any) -> str:
        return QCoreApplication.translate("ActionType", "Sleep {{seconds}}").replace("{{seconds}}", str(config))

    def execute_action(self, env: "Environment", config: Any) -> None:
        time.sleep(config)

    def get_test_config(self, config_version: int) -> Any:
        match config_version:
            case 0:
                return 0.5
