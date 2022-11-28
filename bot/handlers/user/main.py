import os
import json
import random
from pathlib import Path
from aiogram import Dispatcher, Bot, types
from aiogram.types import Message
from bot.database import *


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
opdrachten_path = os.path.join(BASE_DIR, 'opdrachten')


async def start(message: Message) -> None:
    bot: Bot = message.bot
    user_id = message.from_user.id
    check_for_user = check_in_database(table='users', what_to_search='id', what_to_use='user_id', value=str(user_id))
    if check_for_user == []:  # нет такого юзера в базе
        name = " "
        if str(message.from_user.first_name) != "None":
            name = str(message.from_user.first_name)
        if str(message.from_user.last_name) != "None":
            name += str(message.from_user.last_name)
        insert_in_database(table='users', fields=['user_id', 'user_name', 'user_in_game', 'user_last_game'], values=[str(user_id), name, '0', '0'])
    await bot.send_message(user_id, f"<b>Hi</b> there🏖")

    
async def training_response(message: Message):
    bot: Bot = message.bot
    mycursor.execute("SELECT value FROM settings WHERE field = 'Quiz quantity'")
    myresult = mycursor.fetchall()
    keyboard = types.InlineKeyboardMarkup()
    if len(myresult[0][0]) == 0:  # myresult[0][0] = training quantity
        await bot.send_message(message.from_user.id, 'No trainig for now')
    elif 0 < len(myresult[0][0]) <= 8:
        for i in range(1, int(myresult[0][0])+1):
            keyboard.add(types.InlineKeyboardButton(text=f'{i}', callback_data=f'training|{i}'))
        await bot.send_message(message.from_user.id, 'Select workout:', reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, 'Poka rano echo dyadya')

"""
Выбор тренировки, но с json файлами
async def training_response(message: Message):
    bot: Bot = message.bot
    filelist = os.listdir(opdrachten_path)  # список всех файлов в этой дериктории
    jsonfiles = []
    for file in filelist:
        if file.endswith('.json'):  # расширение .json
            jsonfiles.append(file)
    keyboard = types.InlineKeyboardMarkup()
    if len(jsonfiles) == 0:
        await bot.send_message(message.from_user.id, 'No trainig for now')
    elif 0 < len(jsonfiles) <= 8:
        for i in jsonfiles:
            num = i.replace('opdracht', '').replace('.json', '')
            keyboard.add(types.InlineKeyboardButton(text=f'{num}', callback_data=f'training|{num}'))
        await bot.send_message(message.from_user.id, 'Select workout:', reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, 'Poka rano echo dyadya')
"""

async def pre_poll(bot: Bot, chat_id: int):
    game_num = check_in_database("users", "user_in_game", "user_id", str(chat_id))[0][0]
    mycursor.execute(f"SELECT * FROM quiz_{game_num}")
    quiz_info = mycursor.fetchall()
    good_numbers = [i for i in range(len(quiz_info)) if quiz_info[i][4] == 'none']
    the_choosen_one = random.choice(good_numbers)
    print(the_choosen_one)
    del good_numbers[good_numbers.index(the_choosen_one)]
    print(good_numbers)
    question = (
        f"Вопрос {len(quiz_info)-len(good_numbers)} из {len(quiz_info)}\n"
        f"Как преводится слово {quiz_info[the_choosen_one][1]}"
    )
    edit_in_database(f'quiz_{game_num}', 'res', 'processing', 'rus', quiz_info[the_choosen_one][1])
    nums = random.sample(range(len(quiz_info)), 3)
    data = [quiz_info[the_choosen_one][2], quiz_info[nums[0]][2], quiz_info[nums[1]][2], quiz_info[nums[2]][2]]   
    random.shuffle(data)
    await bot.send_poll(chat_id=chat_id, question=question, type='quiz', is_anonymous=False, options=data, correct_option_id=data.index(quiz_info[the_choosen_one][2]))


async def callback_training_response(callback_query: types.CallbackQuery):
    bot = callback_query.bot
    chat_id = callback_query.message.chat.id
    data = callback_query.data.split('|')  # [0]training | [1]num
    quiz = check_in_database(table='word_base', what_to_search='*', what_to_use='lesson', value=f'{data[1]}')
    create_quiz_table(quiz, chat_id)

    await pre_poll(bot, chat_id)


async def poll_answer(quiz_answer: types.PollAnswer):
    bot = quiz_answer.bot
    chat_id = quiz_answer.user.id
    game_num = check_in_database("users", "user_in_game", "user_id", str(chat_id))[0][0]
    result = check_in_database(f'quiz_{game_num}', 'ned', 'res', 'processing')[0][0]
    if quiz_answer.option_ids[0] == result:
        edit_in_database(f'quiz_{game_num}', 'res', 'right', 'res' ,'processing')
    else:
        edit_in_database(f'quiz_{game_num}', 'res', 'wrong', 'res' ,'processing')
    await pre_poll(bot, chat_id)


def register_users_handlers(dp: Dispatcher) -> None:
    # region Msg handlers

    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(training_response, commands=["training"])

    # endregion

    # region Callback handlers
    dp.register_callback_query_handler(callback_training_response, lambda c: c.data.startswith('training'))
    dp.register_poll_answer_handler(poll_answer)
    # endregion