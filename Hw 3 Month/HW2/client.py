from config import bot,dp
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ParseMode
from aiogram import types,Dispatcher

async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call = InlineKeyboardButton("next",callback_data="button_call")
    markup.add(button_call)

    question = "Сколько цветов радуге?"
    answer = ['12', '6', '7', '8']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Каждый Охотник Желатет Знать Где Сидит Фазан",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


photo = open("../Bot/media/ctrl c.jpg", "rb")
async def mem(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=photo)

async def pin(message: types.Message):
    await bot.pin_chat_message(message.reply_to_message.from_user)


def register_handler(dp:Dispatcher):
    dp.register_message_handler(mem,commands=['mem'])
    dp.register_message_handler(quiz1,commands=['quiz','start'])
    dp.register_message_handler(pin,commands=['pin'])