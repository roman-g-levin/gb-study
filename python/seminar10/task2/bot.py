import logging
from datetime import datetime
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from commands import start_command, show_command, add_command, clear_command
from handlers import SHOW_BUTTON_STATE, show_select_handler,\
    SHOW_ASK_NAME, show_ask_name_handler, SHOW_ASK_PHONE, show_ask_phone_handler,\
    ADD_ASK_NAME, add_ask_name_handler, ADD_ASK_PHONE, add_ask_phone_handler
    #op_input_handler, OP_INPUT_STATE, NUM_A_STATE, NUM_B_STATE, \
    #num_b_handler, num_a_handler

#TOKEN = ""
from my_bot_token import TOKEN


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""

    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    # dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("start", start_command))

    show_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('show', show_command)],
        states={
            SHOW_BUTTON_STATE: [MessageHandler(Filters.regex(r"1|2|3"), show_select_handler)],
            SHOW_ASK_NAME: [MessageHandler(Filters.text, show_ask_name_handler)],
            SHOW_ASK_PHONE: [MessageHandler(Filters.text, show_ask_phone_handler)]
        },
        fallbacks=[]
    )

    dispatcher.add_handler(show_conv_handler)

    add_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_command)],
        states={
            ADD_ASK_NAME: [MessageHandler(Filters.text, add_ask_name_handler)],
            ADD_ASK_PHONE: [MessageHandler(Filters.text, add_ask_phone_handler)]
        },
        fallbacks=[]
    )
    dispatcher.add_handler(add_conv_handler)

    dispatcher.add_handler(CommandHandler("clear", clear_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()