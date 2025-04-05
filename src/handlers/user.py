import logging
import subprocess
import os
import requests

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message


user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.full_name}, давай учить слова вместе!\nОтправь мне голосовое сообщение'
    )


@user_router.message(F.text)
async def return_message(message: Message):
    my_requeset = requests.get('http://192.168.1.22:8081/start')

    await message.answer(my_requeset.text)

