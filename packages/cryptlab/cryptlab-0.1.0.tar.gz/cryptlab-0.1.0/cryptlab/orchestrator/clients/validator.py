from enum import Enum, EnumType
from inspect import signature
import inspect
from typing import cast

from loguru import logger

from cryptlab.client.common import client_action

MAX_ACTION_LIST_LENGTH = 100


def validate_action_list(
    n_clients: int, actions: list[list], actions_enum: EnumType
) -> tuple[bool, str]:
    if len(actions) > MAX_ACTION_LIST_LENGTH:
        return False, "Rejected exec config: too many actions"

    for action in actions:
        client_number, action_str, *params = action

        if not 0 <= client_number < n_clients:
            return False, f"Rejected {action}: invalid client number"

        # Here we use the fact that BaseActionEnum subclasses StrEnum
        if action_str.lower() not in actions_enum:
            return False, f"Rejected {action}: action_str not in enum"

        # Now, extract the signature of the handled method and check for parameter correctness
        act_enum: Enum = actions_enum(action_str.lower())  # pyright: ignore
        handler = client_action.get_command_handler(act_enum)
        sig = signature(handler)

        # We will have to force parameters to always be passed by as positional args

        if len(params) != len(sig.parameters) - 1:
            return (
                False,
                f"Rejected {action}: Invalid number of parameters (Got {len(params)}, expected {len(sig.parameters) - 1})",
            )

        for p1, p2 in zip(params, list(sig.parameters.values())[1:]):
            if type(p1) != p2.annotation:
                return (
                    False,
                    f"Rejected {action}: invalid type (Got {type(p1).__name__}, expected {p2.annotation.__name__})",
                )

    return True, ""


def get_basic_type_string(t: type) -> str:
    match t():
        case int():
            return "number"
        case str():
            return "string"
        case bool():
            return "boolean"
        case _:
            raise ValueError(f"{t} is not a basic JSON type")


def construct_type_schema(p):
    d = {"name": p.name}
    match p.annotation():
        case int() | str() | bool():
            d["type"] = get_basic_type_string(p.annotation)
        case list():
            d["type"] = "array"
            d["items"] = {"type": get_basic_type_string(p.annotation.__args__[0])}
        case _:
            raise ValueError(f"Cannot match type {sig_type}")
    return d


def construct_action_schema(actions_enum: EnumType) -> dict:
    action_schemas = []
    for action in actions_enum:
        action = cast(Enum, action)
        handler = client_action.get_command_handler(action)  # pyright: ignore
        sig = signature(handler)

        logger.info(list(sig.parameters.values()))
        schema = {
            "name": action.name,
            "n_params": len(sig.parameters) - 1,
            "params": [
                construct_type_schema(p)
                for p in cast(
                    list[inspect.Parameter], list(sig.parameters.values())[1:]
                )
            ],
        }

        action_schemas.append(schema)
    return action_schemas
