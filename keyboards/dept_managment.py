from aiogram import types

def dept_managment():
    dept_management = [
        types.InlineKeyboardButton(text='Список людей в отделе', callback_data='members_list'),
        types.InlineKeyboardButton(text='Кикнуть человека из отдела', callback_data='kick_member'),
        types.InlineKeyboardButton(text='Отправить сообщение всему отделу', callback_data='send_message_all_dept'),
        types.InlineKeyboardButton(text='Назад', callback_data='back_managment')
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=dept_management)
    return keyboard
