from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token="5109901827:AAGhRp6XUaVLtSzvE8FBen9Xouo5-UnT7pU")
dp = Dispatcher(bot)


button_hi = KeyboardButton('Сардор')
button1 = KeyboardButton('Солдат')
button2 = KeyboardButton('Погоняем')
button3 = KeyboardButton('Курган')
button4 = KeyboardButton('Привет')
button5 = KeyboardButton('Здарова')
button6 = KeyboardButton('Яхай')
button7 = KeyboardButton('ИУ')
button8 = KeyboardButton('Как дела?')
button9 = KeyboardButton('дб')
button10 = KeyboardButton('5 лямов')
button11 = KeyboardButton('Эмо')
button12 = KeyboardButton('Суит')
button13 = KeyboardButton('Лейдис')
button14 = KeyboardButton('Не накаляй')
button15 = KeyboardButton('Братишка')
button16 = KeyboardButton('Шандата')
button17 = KeyboardButton('Наркотики')
button18 = KeyboardButton('Камеру убери')
button19 = KeyboardButton('Упражнение')



greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)


markup_big = ReplyKeyboardMarkup(resize_keyboard=True)

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button7, button8, button9, button10, button11, button12
)

markup_big.row(button13, button14)
markup_big.add(button15, button16)
markup_big.insert(button17)
markup_big.insert(button18)
markup_big.insert(button19)

# bot.py
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_audio(message.chat.id, "CQACAgIAAxkBAALzlGIN_2kgpEXJ597KTIbYGsk7BPGsAAIxEQACPj9xSPfWhgsu0kacIwQ")

@dp.message_handler(commands=['Орет'])
async def process_start_command(message: types.Message):
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAED8_hiDdX7-PIXv20wTFk6XpKsG4dh0wACOBQAAqxnoEuT3ZebH7HNbSME", reply_markup=markup_big)


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений", reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp)