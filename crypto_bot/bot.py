import filters
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, CallbackContext
from telegram.ext import ConversationHandler, Updater
from states import States
from handlers import start_handler, registration_handler, main_menu_handler, crypto_menu_handler, calculator_handler


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_handler)],
    states={
        States.REGISTRATION: [MessageHandler(filters.TEXT, registration_handler)],
        States.MAIN_MENU: [MessageHandler(filters.TEXT, main_menu_handler)],
        States.CRYPTO_MENU: [MessageHandler(filters.TEXT, crypto_menu_handler)],
        States.CALCULATOR: [MessageHandler(filters.TEXT, calculator_handler)],
    },
    fallbacks=[],
    allow_reentry=True
)


def main():
    TOKEN = '6577131949:AAFiFjXYDdmPnqOA43kpfKqsf7i3jVlXWtg'
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

