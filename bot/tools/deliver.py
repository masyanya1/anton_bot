from aiogram import types
from loader import bot
from entities import Event
from typing import Union

async def process_event(
        event: Event,
        with_user_id: bool = False) -> Union[types.Message, int]:

    message = None
    if type(message) is types.CallbackQuery:
        message = event.message
    else:
        message = event

    if with_user_id:
        return message, event.from_user.id
    return message

async def deliver_message(
        event: Event,
        init_message: bool = False,
        **kwargs) -> None:

    message = await process_event(event)

    if type(kwargs['text']) in [list, tuple]:
        text = ''
        for i in kwargs['text']:
            text += i
    else:
        text = kwargs['text']

    if init_message:
        await bot.send_message(
                chat_id=message.chat.id,
                text=text,
                reply_markup=kwargs.get('keyboard')
                )

    else:
        await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=message.message_id,
                text=text,
                reply_markup=kwargs.get('keyboard')
                )
                
