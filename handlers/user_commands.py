from aiogram import Router, types
from aiogram.filters.command import Command
from keyboards.dept_managment import dept_managment
import logging

router = Router()

@router.message(Command("start", "help"))
async def cmd_start(message: types.Message):
    try:
        if 0:
            with open('text/main_member.txt', 'r', encoding='utf-8') as file:
                text = file.read()
            await message.answer(text)

        elif 1:
            with open('text/main_admin.txt', 'r', encoding='utf-8') as file:
                text = file.read()
            await message.answer(text=text, reply_markup=dept_managment())
        else:
            with open('text/main_none.txt', 'r', encoding='utf-8') as file:
                text = file.read()
            await message.answer(text)

    except Exception as e:
        error_message = f"An error occurred: {e}"
        logging.exception(error_message)
        await message.answer("Произошла ошибка")