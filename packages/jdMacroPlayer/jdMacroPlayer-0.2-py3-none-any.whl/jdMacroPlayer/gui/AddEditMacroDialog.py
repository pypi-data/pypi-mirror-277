from PyQt6.QtWidgets import QDialog, QListWidgetItem, QStyle, QMenu, QApplication, QMessageBox
from ..ui_compiled.AddEditMacroDialog import Ui_AddEditMacroDialog
from PyQt6.QtCore import Qt, QCoreApplication, QPoint
from .AddEditActionDialog import AddEditActionDialog
from ..Functions import show_error_msgbox
from ..Constants import SHORTCUT_TRIGGER
from PyQt6.QtGui import QIcon, QAction
from typing import TYPE_CHECKING
from ..core.Action import Action
import traceback
import json
import copy


if TYPE_CHECKING:
    from ..Environment import Environment
    from .MainWindow import MainWindow
    from ..core.Macro import Macro


_CLIPBOARD_MAGIC = "jdMacroPlayer-Magic:"


class AddEditMacroDialog(QDialog, Ui_AddEditMacroDialog):
    def __init__(self, main_window: "MainWindow", env: "Environment", macro: "Macro") -> None:
        super().__init__(main_window)

        self.setupUi(self)

        self._env = env
        self._macro = macro

        self.tab_widget.tabBar().setDocumentMode(True)
        self.tab_widget.tabBar().setExpanding(True)
        self.tab_widget.setCurrentIndex(0)

        self._load_macro(macro)

        self._update_action_buttons_enabled()

        self.ok_button.setIcon(QIcon(env.app.style().standardIcon(QStyle.StandardPixmap.SP_DialogOkButton)))
        self.cancel_button.setIcon(QIcon(env.app.style().standardIcon(QStyle.StandardPixmap.SP_DialogCancelButton)))

        self.action_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.action_list.customContextMenuRequested.connect(self._action_list_context_menu)
        self.action_list.currentItemChanged.connect(self._update_action_buttons_enabled)
        self.add_action_button.clicked.connect(self._add_action_button_clicked)
        self.edit_action_button.clicked.connect(self._edit_action_button_clicked)
        self.remove_action_button.clicked.connect(self._remove_action_button_clicked)

        self.ok_button.clicked.connect(self._ok_button_clicked)
        self.cancel_button.clicked.connect(self.close)

        if macro.name == "":
            self.setWindowTitle(QCoreApplication.translate("AddEditMacroDialog", "Add Macro"))
        else:
            self.setWindowTitle(QCoreApplication.translate("AddEditMacroDialog", "Edit Macro"))

    def _load_macro(self, macro: "Macro") -> None:
        self.name_edit.setText(macro.name)
        self.description_edit.setText(macro.description)

        match macro.shortcut_trigger:
            case SHORTCUT_TRIGGER.PRESSED:
                self.shortcut_pressed_rad.setChecked(True)
            case SHORTCUT_TRIGGER.HOLD:
                self.shortcut_hold_rad.setChecked(True)
            case SHORTCUT_TRIGGER.RELEASED:
                self.shortcut_released_rad.setChecked(True)

        self.action_list.clear()
        for action in macro.actions:
            item = QListWidgetItem(action.get_list_text())
            item.setData(42, action)
            self.action_list.addItem(item)

    def _set_macro_data(self, macro: "Macro") -> None:
        macro.name = self.name_edit.text()
        macro.description = self.description_edit.toPlainText()

        if self.shortcut_pressed_rad.isChecked():
            macro.shortcut_trigger = SHORTCUT_TRIGGER.PRESSED
        elif self.shortcut_hold_rad.isChecked():
            macro.shortcut_trigger = SHORTCUT_TRIGGER.HOLD
        elif self.shortcut_released_rad.isChecked():
            macro.shortcut_trigger = SHORTCUT_TRIGGER.RELEASED

        macro.actions.clear()
        for i in range(self.action_list.count()):
            macro.actions.append(self.action_list.item(i).data(42))

    def _copy_action_clicked(self) -> None:
        action: Action = self.action_list.currentItem().data(42)
        data = json.dumps(action.get_save_data(), ensure_ascii=False)
        QApplication.clipboard().setText(_CLIPBOARD_MAGIC + data)

    def _paste_action_clicked(self) -> None:
        try:
            data = json.loads(QApplication.clipboard().text().removeprefix(_CLIPBOARD_MAGIC))
            action = Action.from_save_data(data)


            item = QListWidgetItem(action.get_list_text())
            item.setData(42, action)
            self.action_list.addItem(item)
        except Exception:
            show_error_msgbox(self, traceback.format_exc())

    def _action_list_context_menu(self, pos: QPoint) -> None:
        menu = QMenu(self)

        copy_action = QAction(QCoreApplication.translate("AddEditMacroDialog", "Copy"), self)
        copy_action.setEnabled(self.action_list.currentItem() is not None)
        copy_action.triggered.connect(self._copy_action_clicked)
        menu.addAction(copy_action)

        paste_action = QAction(QCoreApplication.translate("AddEditMacroDialog", "Paste"), self)
        paste_action.setEnabled(QApplication.clipboard().text().startswith(_CLIPBOARD_MAGIC))
        paste_action.triggered.connect(self._paste_action_clicked)
        menu.addAction(paste_action)

        menu.popup(self.action_list.mapToGlobal(pos))

    def _update_action_buttons_enabled(self) -> None:
        enabled = self.action_list.currentItem() is not None
        self.edit_action_button.setEnabled(enabled)
        self.remove_action_button.setEnabled(enabled)

    def _add_action_button_clicked(self) -> None:
        dialog = AddEditActionDialog(self, self._env, Action())
        action = dialog.open_dialog()

        if action is None:
            return

        item = QListWidgetItem(action.get_list_text())
        item.setData(42, action)
        self.action_list.addItem(item)

    def _edit_action_button_clicked(self) -> None:
        dialog = AddEditActionDialog(self, self._env, self.action_list.currentItem().data(42))
        action = dialog.open_dialog()

        if action is None:
            return

        self.action_list.currentItem().setData(42, action)
        self.action_list.currentItem().setText(action.get_list_text())

    def _remove_action_button_clicked(self) -> None:
        self.action_list.takeItem(self.action_list.currentRow())

    def _ok_button_clicked(self) -> None:
        if self.name_edit.text().strip() == "":
            QMessageBox.critical(
                self,
                QCoreApplication.translate("AddEditMacroDialog", "No name"),
                QCoreApplication.translate("AddEditMacroDialog", "You need to enter a name"),
            )
            return

        macro = copy.deepcopy(self._macro)
        self._set_macro_data(macro)
        self._env.macro_manager.update_macro(macro)
        self.close()

    def open_dialog(self) -> None:
        self.exec()
