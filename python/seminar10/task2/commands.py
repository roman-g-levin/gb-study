from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from handlers import SHOW_BUTTON_STATE, ADD_ASK_NAME,\
    save_abonents, DEL_ASK_ID

def start_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(f"Привет {user.first_name}!\n\
        Это бот управления твоим телефонным справочником\n\
        Команды:\n\
        /start - запустить бота и показать инструкцию\n\
        /show - показать справочник\n\
        /add - добавить запись в справочник\n\
        /del - удвлить запись из справочника\n\
        /clear - очистка всего справочника")


def show_command(update: Update, context: CallbackContext) -> int:
    """show abonents command"""
    kb = [
        ["1.Показать справочник полностью"],
        ["2.Поиск по имени"],
        ["3.Поиск по номеру"]
    ]

    reply_kb_markup = ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("Выберите действие", reply_markup=reply_kb_markup)

    return SHOW_BUTTON_STATE

def add_command(update: Update, context: CallbackContext) -> int:
    """add new abonent"""
    update.message.reply_text("Добавление новой записи в справочник\n\
        Введите имя:")
    return ADD_ASK_NAME

def del_command(update: Update, context: CallbackContext) -> int:
    """del abonent with id"""
    update.message.reply_text("Удаление записи в справочнике\n\
        Введите id:")
    return DEL_ASK_ID

def clear_command(update: Update, context: CallbackContext) -> None:
    """удаление всех записей в справочнике"""
    abonents=[]
    save_abonents(abonents, update.effective_user.id)
    update.message.reply_text("Справочник полностью очищен!")
