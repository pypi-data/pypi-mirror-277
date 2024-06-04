from PyQt6.QtWidgets import QWidget, QComboBox, QMessageBox
from PyQt6.QtCore import QCoreApplication
from typing import Any
import os


def is_flatpak() -> bool:
    return os.path.exists("/.flatpak-info")


def select_combo_box_data(box: QComboBox, data: Any, default_index: int = 0) -> None:
    """Set the index to the item with the given data"""
    index = box.findData(data)
    if index == -1:
        box.setCurrentIndex(default_index)
    else:
        box.setCurrentIndex(index)


def show_error_msgbox(parent: QWidget | None, text: str) -> None:
    "Shows a message box with an error"
    msg_box = QMessageBox(parent)
    msg_box.setWindowTitle(QCoreApplication.translate("Functions", "Error"))
    msg_box.setText(QCoreApplication.translate("Functions", "An unknown error occurred"))
    msg_box.setDetailedText(text)
    msg_box.exec()
