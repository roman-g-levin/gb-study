from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
import random

user_profile = {}
current_player = { 0:"человек", 1:"бот"}
max_candies=121     # первоначальное количество конфет на столе

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
    user_profile["total"]=max_candies
    user_profile["human"]=0
    user_profile["bot"]=0
    user_profile["pass"]=random.randint(0, 1)
    if user_profile['pass']:    # ход бота
        update.message.reply_text(f"Начинаем игру в 2021 конфету.\n\
            Первым ходит бот.\n{bot_pass()}\n\
            Можно взять от 1 до {max_candies_get()} конфет.\n\
            Сколько вы берете конфет?")
    else:
        update.message.reply_text(f"Начинаем игру в 2021 конфету.\n\
            Первым ходите вы.\n{print_stat()}\n\
            Можно взять от 1 до {max_candies_get()} конфет.\n\
            Сколько вы берете конфет?")
    return ASK_Q_CANDIES
    #return ConversationHandler.END

def max_candies_get():
    if user_profile["total"]<28:
        return user_profile["total"]
    else:
        return 28

def bot_pass():
    candies_get=user_profile["total"] % 29  # хотим взять вот столько
    if candies_get<1 or candies_get > max_candies_get():
        candies_get = random.randint(1, max_candies_get())  # если не можем взять сколько хотим, берем случайное число
    user_profile["total"] -= candies_get
    user_profile["bot"] += candies_get
    msg = "Бот взял "+str(candies_get)+" конфет.\n"
    return msg+print_stat()

def print_stat():
    msg="Всего осталось конфет: "+str(user_profile["total"])+\
        "\nу бота: "+str(user_profile["bot"])+\
        "\nу вас: "+str(user_profile["human"])+"\n"
    return msg


def game_pass(update: Update, context: CallbackContext) -> int:
    candies = update.message.text
    if candies=='0':
        update.message.reply_text("Игра закончена")
        return ConversationHandler.END
    if not candies.isdigit():   #анализ корректности ввода
        update.message.reply_text("Нужно ввести число.\n\
            Сколько вы берете конфет?\n\
            0 - выход")
        return ASK_Q_CANDIES
    candies=int(candies)
    if candies<0 or candies>max_candies_get():
        update.message.reply_text(f"Нужно ввести число от 1 до {max_candies_get()}.\n\
            Сколько вы берете конфет?\n\
            0 - выход")
        return ASK_Q_CANDIES
    
    #ход
    user_profile["total"] -= candies
    user_profile["human"] += candies
    
    #проверка на выигрыш
    if user_profile["total"] == 0:
        #выиграл человек
        update.message.reply_text(f"Вы взяли последнюю конфету и ВЫИГРАЛИ!.\n\
            Игра окончена.")
        return ConversationHandler.END

    msg=bot_pass()  #ход бота
    if user_profile["total"] == 0:  #проверка на выигрыш
        update.message.reply_text(f"{msg}Бот взял последнюю конфету и ВЫИГРАЛ!.\n\
            Игра окончена.")
        return ConversationHandler.END
    
    #запрос кол-ва конфет
    update.message.reply_text(f"{msg}\
        Сколько вы берете конфет?\n\
        0 - выход")
    return ASK_Q_CANDIES

