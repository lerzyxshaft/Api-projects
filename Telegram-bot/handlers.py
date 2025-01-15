from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Hello I can help you to check your ID, just send me any message!")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Your ID: {msg.from_user.id}")