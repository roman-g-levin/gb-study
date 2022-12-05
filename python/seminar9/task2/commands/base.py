# Define a few command handlers. These usually take the two arguments update and
# context.
from telegram import Update
from telegram.ext import CallbackContext
from handlers.player_profile import PLAYER_NAME_STATE, user_profile, current_player, ASK_Q_CANDIES
import random

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_text(f"Привет {user.first_name}!\nЗапуск игры:\n /game\n")
    


def player_profile_command(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(f"Введите имя: ")

    return PLAYER_NAME_STATE

