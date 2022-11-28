import os
import json
import random
from pathlib import Path
# from bot.cfg import token
# from telegram import ParseMode
from aiogram import Bot, Dispatcher, executor, types
from bot.misc import TgKeys
from bot.handlers import register_all_handlers

BASE_DIR = Path(__file__).resolve().parent


async def __on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)


def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot) # , storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)


# @dp.message_handler(commands=['training'])
# async def training_response(message: types.Message):
#     filelist = os.listdir(BASE_DIR)  # список всех файлов в этой дериктории
#     jsonfiles = []
#     for file in filelist:
#         if file.endswith('.json'):  # расширение .json
#             jsonfiles.append(file)
#     keyboard = types.InlineKeyboardMarkup()
#     if len(jsonfiles) == 0:
#         await bot.send_message(message.from_user.id, 'No trainig for now')
#     elif 0 < len(jsonfiles) <= 8:
#         for i in jsonfiles:
#             num = i.replace('opdracht', '').replace('.json', '')
#             keyboard.add(types.InlineKeyboardButton(text=f'{num}', callback_data=f'training|{num}'))
#         await bot.send_message(message.from_user.id, 'Select workout:', reply_markup=keyboard)
#     else:
#         await bot.send_message(message.from_user.id, 'Poka rano echo dyadya')


# @dp.callback_query_handler(lambda c: c.data.startswith('training'))  # lambda c: c.data == 'a1'
# async def callback_query_response(callback_query: types.CallbackQuery):
#     data = callback_query.data.split('|')
#     with open(f'opdracht{data[1]}.json', 'r') as file:
#         opdracht = json.load(file)
#     question_word = random.choice(list(opdracht.keys()))
#     answer = opdracht[question_word]
#     question = f"Как переводится <b>{question_word}</b>:"
#     data = [opdracht.pop(question_word), random.choice(list(opdracht.values())), random.choice(list(opdracht.values())), random.choice(list(opdracht.values()))]
#     random.shuffle(data)
#     await bot.send_poll(chat_id=callback_query.message.chat.id ,question=question, type='quiz', is_anonymous=False, options=data, correct_option_id=data.index(answer))


# @dp.poll_answer_handler()
# async def poll_answer(poll_answer: types.PollAnswer):
#     print(poll_answer)

