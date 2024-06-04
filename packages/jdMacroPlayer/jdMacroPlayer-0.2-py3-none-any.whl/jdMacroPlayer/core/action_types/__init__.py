from .ActionTypeNotification import ActionTypeNotification
from .ActionTypeMousemove import ActionTypeMousemove
from .ActionTypeKeypress import ActionTypeKeypress
from .ActionTypeCommand import ActionTypeCommand
from .ActionTypeSleep import ActionTypeSleep
from .ActionTypeClick import ActionTypeClick
from .ActionTypeType import ActionTypeType
from .ActionTypeBase import ActionTypeBase
from typing import Optional


def get_all_action_types() -> list[ActionTypeBase]:
    return [
        ActionTypeCommand(),
        ActionTypeKeypress(),
        ActionTypeType(),
        ActionTypeMousemove(),
        ActionTypeClick(),
        ActionTypeSleep(),
        ActionTypeNotification(),
    ]


def get_action_type_by_id(type_id: str) -> Optional[ActionTypeBase]:
    for action_type in get_all_action_types():
        if action_type.get_id() == type_id:
            return action_type
    return None
