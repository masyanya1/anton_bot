from aiogram import Router
from aiogram.filters import CommandStart
from tools import deliver_message, process_event
from entities import Event

router = Router()

@router.message(CommandStart(deep_link=False))
async def welcome_message(event: Event) -> None:
    message = await process_event(event)

    text = (
            'Список досутпных комманд: '
            )

    await deliver_message(
            event,
            init_message=True,
            text=text
            )
