from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from handlers import SHOW_BUTTON_STATE

def start_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(f"Привет {user.first_name}!\n\
        Это бот управления твоим телефонным справочником\n\
        Команды:\n\
        /start - запустить бота и показать инструкцию\n\
        /show - показать справочник\n")


def show_command(update: Update, context: CallbackContext) -> int:
    kb = [
        ["1.Показать справочник полностью"],
        ["2.Поиск по имени"],
        ["3.Поиск по номеру"]
    ]

    reply_kb_markup = ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("Выберите действие", reply_markup=reply_kb_markup)

    return SHOW_BUTTON_STATE