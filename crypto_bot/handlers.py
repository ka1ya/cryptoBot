from telegram.ext import CallbackContext
from states import States
from model import UserProfile
from crypto_api import get_crypto_prices
from telegram import ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup


def start_handler(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    context.user_data['user_id'] = user_id

    reply_markup = ReplyKeyboardMarkup([['📋 Main Menu']], one_time_keyboard=True)
    update.message.reply_text("Welcome to the Crypto Bot! How can I assist you?", reply_markup=reply_markup)

    return States.MAIN_MENU


def registration_handler(update: Update, context: CallbackContext):
    user_id = context.user_data['user_id']
    phone_number = update.message.text
    user_profile = UserProfile(
        user_id=user_id,
        first_name=update.message.from_user.first_name,
        last_name=update.message.from_user.last_name,
        username=update.message.from_user.username,
        phone_number=phone_number)
    user_profile.save()

    update.message.reply_text(f"Thank you for registering with the phone number {phone_number}!")
    return States.MAIN_MENU


def main_menu_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup([['💰 Crypto Menu', '🔄 Calculator']], one_time_keyboard=True)
    update.message.reply_text("Main Menu - Choose an option:", reply_markup=reply_markup)

    return States.CRYPTO_MENU


def crypto_menu_handler(update, context):
    reply_markup = create_crypto_menu_keyboard()

    update.message.reply_text("Choose a cryptocurrency:", reply_markup=reply_markup)

    return States.CRYPTO_MENU


def create_crypto_menu_keyboard():
    crypto_data = get_crypto_prices()

    buttons = []
    for crypto_coin in crypto_data:
        name = crypto_coin['name']
        buttons.append([InlineKeyboardButton(text=name, callback_data=f'crypto_{name}')])

    return InlineKeyboardMarkup(buttons)


def send_crypto_details(update, context, crypto_name, currency_code):
    crypto_data = get_crypto_prices()

    selected_crypto = next((coin for coin in crypto_data if coin['name'] == crypto_name), None)

    if selected_crypto:
        currency_data = selected_crypto['prices'].get(currency_code)

        if currency_data:
            price = currency_data['price']
            image_url = currency_data['image_url']
            context.bot.send_photo(
                chat_id=update.message.chat_id,
                photo=image_url,
                caption=f"{crypto_name} Price: {price} {currency_code}")
        else:
            update.message.reply_text("Data not available for the selected currency.")
    else:
        update.message.reply_text("Data not available for the selected cryptocurrency.")


def calculator_handler(update: Update, context: CallbackContext):
    # Логіка калькулятора (обмін криптовалюти на долари та зворотнього курсу)

    update.message.reply_text("Calculator result: ...")  # Повернення результату

    return States.MAIN_MENU

