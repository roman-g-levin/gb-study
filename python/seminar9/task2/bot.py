import logging
from my_bot_token import TOKEN

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Enable logging
from commands.base import start, player_profile_command
from handlers.player_profile import input_player_name_handler, input_player_age_handler, PLAYER_NAME_STATE, \
    PLAYER_AGE_STATE, PLAYER_GENDER_STATE, input_player_gender_handler, ASK_Q_CANDIES, game_pass

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# TOKEN = "abc-....-xyz"
# you need the file my_bot_token.py with your telegram-bot token


def main() -> None:
    """Start the bot."""

    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    player_profile_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('game', player_profile_command)],
        states={
            PLAYER_NAME_STATE: [MessageHandler(Filters.text, input_player_name_handler)],
            PLAYER_AGE_STATE: [MessageHandler(Filters.text, input_player_age_handler)],
            PLAYER_GENDER_STATE: [MessageHandler(Filters.text, input_player_gender_handler)],
            ASK_Q_CANDIES: [MessageHandler(Filters.text, game_pass)],
        },
        fallbacks=[],
    )


    dispatcher.add_handler(player_profile_conv_handler)

    # Start the Bot
    updater.start_polling()     # опрашиваем сервер телеграма

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()