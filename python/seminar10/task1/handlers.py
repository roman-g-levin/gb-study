import os.path
import pickle

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
#from bot import logger
#from datetime import datetime

(
    OP_BUTTON_STATE,
    OP_INPUT_STATE,
    NUM_A_STATE,
    NUM_B_STATE
) = range(4)  # [0, 1, 2, ..]


def save_data(data, chat_id):
    with open(f'{chat_id}.pickle', 'wb') as f:
        pickle.dump(data, f)


def load_data(chat_id):
    file_name = f'{chat_id}.pickle'
    if not os.path.exists(file_name):
        return None

    with open(file_name, 'rb') as f:
        return pickle.load(f)


def op_select_handler(update: Update, context: CallbackContext) -> int:
    # сохранить с какими числами работаем (с вещественными или цилыми)
    text = update.message.text

    data = load_data(update.effective_user.id)
    if not data:
        data = {
            "username": update.effective_user.username,
            "num_a": 0,
            "num_b": 0,
            "op": "",  # +, -, *...
            "num_type": float
        }


    if "R" in text:
        data["num_type"] = float
    elif "C" in text:
        data["num_type"] = complex

    save_data(data, update.effective_user.id)
    #logger.info("{} Пользователь {} выбрал работу с {}".format(datetime.now().time(), update.effective_user.id, data["num_type"]))

    # Предложить пользователию выбрать действие InlineKeyboard
    kb = [
        [InlineKeyboardButton("A + B", callback_data="+"), InlineKeyboardButton("A - B", callback_data="-")],
        [InlineKeyboardButton("A * B", callback_data="*"), InlineKeyboardButton("A / B", callback_data="/")]
    ]
    reply_kb_markup = InlineKeyboardMarkup(kb)
    update.message.reply_text(f"{data['username']},\nВыберите операцию: ", reply_markup=reply_kb_markup)
    return OP_INPUT_STATE


def op_input_handler(update: Update, context: CallbackContext) -> int:

    data = load_data(update.effective_user.id)

    data["op"] = update.callback_query.data   # +, -

    save_data(data, update.effective_user.id)
    #logger.info("{} Пользователь {} выбрал работу с {}".format(datetime.now().time(), update.effective_user.id, data["op"]))
    update.callback_query.message.edit_text("Введите число A: ")
    return NUM_A_STATE

def num_a_handler(update: Update, context: CallbackContext) -> int:
    data = load_data(update.effective_user.id)

    data["num_a"] = update.message.text

    save_data(data, update.effective_user.id)
    #logger.info("{} Пользователь {} ввел число A {}".format(datetime.now().time(), update.effective_user.id, data["num_a"]))

    update.message.reply_text("Введите число B: ")
    return NUM_B_STATE


def num_b_handler(update: Update, context: CallbackContext) -> int:
    data = load_data(update.effective_user.id)
    data["num_b"] = update.message.text

    # выполнить рассчет и вывести ответ
    num_a = data["num_type"](data["num_a"])     # float(data["num_a"]) -> float('2')
    num_b = data["num_type"](data["num_b"])
    if data["op"]=='/' and (num_b==0 or num_b==complex(0j)):
        data["result"] = "деление на 0 невозможно"
    else:
        data["result"] = eval(f'{num_a} {data["op"]} {num_b}')

    save_data(data, update.effective_user.id)
    #logger.info("{} Пользователь {} ввел число B {}".format(datetime.now().time(), update.effective_user.id, data["num_b"]))
    #logger.info("{} Пользователь {} Результат вычислений {}".format(datetime.now().time(), update.effective_user.id, data["result"]))
    update.message.reply_text(f"{data['username']},\nРезультат вычислений: {data['result']}")

    return ConversationHandler.END
