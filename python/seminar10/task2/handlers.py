import os.path
import pickle

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from model import abonents

(
    SHOW_BUTTON_STATE,
    SHOW_ASK_NAME,
    SHOW_ASK_PHONE,
    NUM_B_STATE
) = range(4)  # [0, 1, 2, ..]


def save_abonents(data, chat_id):
    with open(f'{chat_id}.pickle', 'wb') as f:
        pickle.dump(data, f)


def load_abonents(chat_id):
    file_name = f'{chat_id}.pickle'
    if not os.path.exists(file_name):
        return [{}]
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def show_select_handler(update: Update, context: CallbackContext) -> int:
    global abonents
    #abonents = load_abonents(update.effective_user.id)

    # выбрать режим отображения
    text = update.message.text

    if "1" in text:
        msg = ''
        for a in abonents:
            msg += str(a["id"])+'. '+a["fio"]+', '+str(a["phone"])+'\n'
        update.message.reply_text(msg)
        return ConversationHandler.END
    elif "2" in text:
        update.message.reply_text("Введите имя:")
        return SHOW_ASK_NAME
    elif "3" in text:
        update.message.reply_text("Введите номер телефона:")
        return SHOW_ASK_PHONE

    # Предложить пользователию выбрать действие InlineKeyboard
#    kb = [
#        [InlineKeyboardButton("A + B", callback_data="+"), InlineKeyboardButton("A - B", callback_data="-")],
#        [InlineKeyboardButton("A * B", callback_data="*"), InlineKeyboardButton("A / B", callback_data="/")]
#    ]
#    reply_kb_markup = InlineKeyboardMarkup(kb)
#    update.message.reply_text(f"{data['username']},\nВыберите операцию: ", reply_markup=reply_kb_markup)
#    return OP_INPUT_STATE


# def op_input_handler(update: Update, context: CallbackContext) -> int:

#    data = load_data(update.effective_user.id)

#    data["op"] = update.callback_query.data   # +, -

#    save_data(data, update.effective_user.id)
#    update.callback_query.message.edit_text("Введите число A: ")
#    return NUM_A_STATE


def show_ask_name_handler(update: Update, context: CallbackContext) -> int:
    global abonents
    #abonents = load_abonents(update.effective_user.id)

    name = update.message.text
    msg = ''
    for a in abonents:
        if a["fio"].upper() == name.upper():
            msg += str(a["id"])+'. '+a["fio"]+', '+str(a["phone"])+'\n'
    update.message.reply_text(msg)
    return ConversationHandler.END


def show_ask_phone_handler(update: Update, context: CallbackContext) -> int:
    global abonents
    #abonents = load_abonents(update.effective_user.id)

    phone = update.message.text
    msg = ''
    for a in abonents:
        if str(a["phone"]) == phone:
            msg += str(a["id"])+'. '+a["fio"]+', '+str(a["phone"])+'\n'
    update.message.reply_text(msg)
    return ConversationHandler.END


#def num_b_handler(update: Update, context: CallbackContext) -> int:
#    data = load_data(update.effective_user.id)
#    data["num_b"] = update.message.text

    # выполнить рассчет и вывести ответ
    # float(data["num_a"]) -> float('2')
#    num_a = data["num_type"](data["num_a"])
#    num_b = data["num_type"](data["num_b"])
#    if data["op"] == '/' and (num_b == 0 or num_b == complex(0j)):
#        data["result"] = "деление на 0 невозможно"
#    else:
#        data["result"] = eval(f'{num_a} {data["op"]} {num_b}')

#    save_data(data, update.effective_user.id)
    #logger.info("{} Пользователь {} ввел число B {}".format(datetime.now().time(), update.effective_user.id, data["num_b"]))
    #logger.info("{} Пользователь {} Результат вычислений {}".format(datetime.now().time(), update.effective_user.id, data["result"]))
#    update.message.reply_text(
#        f"{data['username']},\nРезультат вычислений: {data['result']}")

#    return ConversationHandler.END
