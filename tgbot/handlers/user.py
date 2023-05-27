from telebot import TeleBot
from telebot import types

def any_user(message: types.Message, bot: TeleBot):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Flat")
    item2 = types.KeyboardButton("Cottage")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Hi, {0.first_name}!\nI'm - <b>{1.first_name}</b>, bot.\nWhich type of house do you prefer".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)