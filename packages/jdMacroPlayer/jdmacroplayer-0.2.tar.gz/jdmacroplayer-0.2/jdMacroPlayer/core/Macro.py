from ..Constants import SHORTCUT_TRIGGER
from typing import Type, Any
from .Action import Action


class Macro:
    def __init__(self) -> None:
        self.id = ""
        self.name = ""
        self.description = ""
        self.actions: list[Action] = []
        self.shortcut_trigger = SHORTCUT_TRIGGER.PRESSED

    @classmethod
    def from_save_data(cls: Type["Macro"], data: dict[str, Any]) -> "Macro":
        macro = cls()

        macro.id = data["id"]
        macro.name = data["name"]
        macro.description = data["description"]
        macro.shortcut_trigger = data["shortcut_trigger"]

        for i in data["actions"]:
            macro.actions.append(Action.from_save_data(i))

        return macro

    @staticmethod
    def update_save_data(version: int, data: dict[str, Any]) -> None:
        match version:
            case 1:
                data["shortcut_trigger"] = SHORTCUT_TRIGGER.PRESSED

        for action_data in data["actions"]:
            Action.update_save_data(version, action_data)

    def get_save_data(self) -> dict[str, Any]:
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "actions": [],
            "shortcut_trigger": self.shortcut_trigger,
        }

        for action in self.actions:
            data["actions"].append(action.get_save_data())

        return data
