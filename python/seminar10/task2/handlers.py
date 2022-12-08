import os.path
import pickle

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
#from model import abonents

(
    SHOW_BUTTON_STATE,
    SHOW_ASK_NAME,
    SHOW_ASK_PHONE,
    ADD_ASK_NAME,
    ADD_ASK_PHONE,
    DEL_ASK_ID
) = range(6)  # [0, 1, 2, ..]


def save_abonents(data, chat_id):
    with open(f'{chat_id}.pickle', 'wb') as f:
        pickle.dump(data, f)


def load_abonents(chat_id):
    file_name = f'{chat_id}.pickle'
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def show_select_handler(update: Update, context: CallbackContext) -> int:
    abonents = load_abonents(update.effective_user.id)
    if not abonents:
        update.message.reply_text("Справочник пуст")
        return ConversationHandler.END
    else:
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
        return ConversationHandler.END


def show_ask_name_handler(update: Update, context: CallbackContext) -> int:
    abonents = load_abonents(update.effective_user.id)

    name = update.message.text
    msg = ''
    for a in abonents:
        if a["fio"].upper() == name.upper():
            msg += str(a["id"])+'. '+a["fio"]+', '+str(a["phone"])+'\n'
    update.message.reply_text(msg)
    return ConversationHandler.END


def show_ask_phone_handler(update: Update, context: CallbackContext) -> int:
    abonents = load_abonents(update.effective_user.id)

    phone = update.message.text
    msg = ''
    for a in abonents:
        if str(a["phone"]) == phone:
            msg += str(a["id"])+'. '+a["fio"]+', '+str(a["phone"])+'\n'
    update.message.reply_text(msg)
    return ConversationHandler.END


def add_ask_name_handler(update: Update, context: CallbackContext) -> int:
    abonents = load_abonents(update.effective_user.id)
    if not abonents:
        abonents = []
    name = update.message.text
    new_num = 0  # незаконченный ввод. вводим только имя
    abonents.append({
        "id": new_num,
        "fio": name,
        "phone": 0
        })
    save_abonents(abonents, update.effective_user.id)
    update.message.reply_text("Введите номер телефона:")
    return ADD_ASK_PHONE


def add_ask_phone_handler(update: Update, context: CallbackContext) -> int:
    abonents = load_abonents(update.effective_user.id)

    phone = update.message.text
    if phone.isdigit():
        phone=int(phone)
    else:
        update.message.reply_text("\
            Ошибка ввода номера.\n\
            Введите номер телефона:")
        return ADD_ASK_PHONE

    for i in range(len(abonents)):
        if abonents[i]["id"] == 0:
            name = abonents[i]["fio"]
            if i==0:
                new_num = abonents[-1]["id"] + 1
                abonents.pop(i)
            else:
                abonents.pop(i)
                new_num = abonents[-1]["id"] + 1
            abonents.append({
                "id": new_num,
                "fio": name,
                "phone": phone
            })
            save_abonents(abonents, update.effective_user.id)
            update.message.reply_text(f"Добавлен абонент:\n\
                {new_num}. {name}, {phone}")
            break
    return ConversationHandler.END

def del_ask_id_handler(update: Update, context: CallbackContext) -> int:
    abonents = load_abonents(update.effective_user.id)

    id = update.message.text
    if id.isdigit():
        id=int(id)
    else:
        update.message.reply_text("\
            Ошибка ввода id!\n\
            Введите число!")
        return DEL_ASK_ID

    for i in range(len(abonents)):
        if abonents[i]["id"] == id:
            abonents.pop(i)
            save_abonents(abonents, update.effective_user.id)
            update.message.reply_text(f"Удалена запись с id={id}")
            return ConversationHandler.END
    update.message.reply_text(f"Запись с id={id} не найдена!")
    return ConversationHandler.END
