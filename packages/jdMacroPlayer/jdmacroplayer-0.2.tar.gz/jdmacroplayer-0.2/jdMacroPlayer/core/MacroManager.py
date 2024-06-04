from typing import TYPE_CHECKING
from .Macro import Macro
import json
import uuid
import os


if TYPE_CHECKING:
    from ..Environment import Environment


_CURRENT_SAVE_VERSION = 2

class MacroManager:
    def __init__(self, env: "Environment") -> None:
        self._macro_list: list[Macro] = []
        self._env = env

    def get_macro_by_id(self, macro_id: str) -> Macro | None:
        for current_macro in self._macro_list:
            if current_macro.id == macro_id:
                return current_macro
        return None

    def get_macro_by_name(self, name: str) -> Macro | None:
        for current_macro in self._macro_list:
            if current_macro.name.lower() == name.lower():
                return current_macro
        return None

    def create_new_macro(self) -> Macro:
        while True:
            current_id = str(uuid.uuid4())
            if self.get_macro_by_id(current_id) is None:
                new_macro = Macro()
                new_macro.id = current_id
                return new_macro

    def update_macro(self, macro: "Macro") -> None:
        for i in range(len(self._macro_list)):
            if self._macro_list[i].id == macro.id:
                self._macro_list[i] = macro
                break
        else:
            self._macro_list.append(macro)

        self.write_file()

    def write_file(self) -> None:
        data = {
            "version": _CURRENT_SAVE_VERSION,
            "macros": [],
        }

        for macro in self._macro_list:
            data["macros"].append(macro.get_save_data())

        try:
            os.makedirs(self._env.data_dir)
        except FileExistsError:
            pass

        with open(os.path.join(self._env.data_dir, "macros.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_file(self) -> None:
        self._macro_list.clear()

        if not os.path.isfile(os.path.join(self._env.data_dir, "macros.json")):
            return

        with open(os.path.join(self._env.data_dir, "macros.json"), "r", encoding="utf-8") as f:
            data = json.load(f)

        version = data["version"]

        for macro_data in data["macros"]:
            for i in range(version, _CURRENT_SAVE_VERSION):
                Macro.update_save_data(i, macro_data)

            self._macro_list.append(Macro.from_save_data(macro_data))

    def get_all_macros(self) -> list[Macro]:
        return self._macro_list

    def delete_macro_by_id(self, macro_id: str) -> None:
        for i in range(len(self._macro_list)):
            if self._macro_list[i].id == macro_id:
                del self._macro_list[i]
                self.write_file()
                return
