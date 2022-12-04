from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
import random

user_profile = {}
current_player = { 0:"человек", 1:"бот"}

(
    PLAYER_NAME_STATE,  # 0
    PLAYER_AGE_STATE,  # 1
    PLAYER_GENDER_STATE,  # 2
    ASK_Q_CANDIES
) = range(4)

def input_player_name_handler(update: Update, context: CallbackContext) -> int:
    name = update.message.text
    user_profile["name"] = name

    update.message.reply_text(f"Введите возраст:")
    return PLAYER_AGE_STATE


def input_player_age_handler(update: Update, context: CallbackContext) -> int:
    age = update.message.text
    if not age.isdigit():
        update.message.reply_text(f"Ошибка! Введите возраст число: ")
        return PLAYER_AGE_STATE

    user_profile["age"] = int(age)

    reply_kb_markup = ReplyKeyboardMarkup([
        ["М", "Ж"],
    ], one_time_keyboard=True)

    update.message.reply_text(f"Введите пол:", reply_markup=reply_kb_markup)

    return PLAYER_GENDER_STATE


def input_player_gender_handler(update: Update, context: CallbackContext) -> int:
    user_profile["gender"] = update.message.text

    #update.message.reply_text(f"Вы ввели следующую информацию: {user_profile}")
    random.seed
    user_profile["total"]=2021
    user_profile["human"]=0
    user_profile["bot"]=0
    user_profile["pass"]=random.randint(0, 1)
    update.message.reply_text(f"Начинаем игру в 2021 конфету.\n\
        Первым ходит {current_player[user_profile['pass']]}")
    ##ход бота
    return ASK_Q_CANDIES
    #return ConversationHandler.END

def game_pass(update: Update, context: CallbackContext) -> int:
    candies = update.message.text
    if candies=='0':
        update.message.reply_text("Игра закончена")
        return ConversationHandler.END
    #анализ корректности ввода
    #проверка на выигрыш
    #ход бота
    #проверка на выигрыш
    #запрос кол-ва конфет
    update.message.reply_text(f"Вы ввели {candies}\n0 - выход")


    return ASK_Q_CANDIES

