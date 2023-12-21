from aiogram import types 

def meetings():
    meetings = [
        types.InlineKeyboardButton(text='Ввести дату', callback_data='enter_data'),
        types.InlineKeyboardButton(text='Добавить аудиторию к собранию', callback_data='enter_flat'),
        types.InlineKeyboardButton(text='Назад', callback_data='back_meetings')
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[meetings], resize_keyboard=True)
    return keyboard