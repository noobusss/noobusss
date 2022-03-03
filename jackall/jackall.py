from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5109901827:AAGhRp6XUaVLtSzvE8FBen9Xouo5-UnT7pU"

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def answer(message: types.Message):
    btn1 = KeyboardButton('Привет')
    markup1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn1)
    await message.reply('Привет', reply_markup=markup1)


@dp.message_handler(content_types=['text'])
async def chat(message: types.Message):
    if message.text == 'Привет':
        btn3 = InlineKeyboardButton('Отлично!', callback_data='good')
        btn4 = InlineKeyboardButton('Не очень!', callback_data='bad')
        markup2 = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True).add(btn3, btn4)
        await message.reply('Привет, как дела?', reply_markup=markup2)


    else:
        await message.reply('Извините, но я не понимаю!')





if __name__ == '__main__':
    executor.start_polling(dp)