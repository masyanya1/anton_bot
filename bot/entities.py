from aiogram import types
from typing import Union

type Event = Union[
        types.CallbackQuery,
        types.Message
        ]
