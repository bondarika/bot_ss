from aiogram import types 

def keyboard_admin():
    keyboard_admin = [
        types.InlineKeyboardButton(text='Управление отделом', callback_data='dept_managment'),
        types.InlineKeyboardButton(text='Назначить собрание', callback_data='assign_meeting'),
        types.InlineKeyboardButton(text='Доступные команды', callback_data='admin_help')
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[keyboard_admin], resize_keyboard=True)
    return keyboard