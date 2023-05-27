from telebot import TeleBot
from telebot import types

def any_user(message: types.Message, bot: TeleBot):

    # keyboard
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Flat", callback_data='flat')
    item2 = types.InlineKeyboardButton("Cottage", callback_data='cottage')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Hi, {0.first_name}!\nI'm - <b>{1.first_name}</b>, bot.\nWhich type of house do you prefer".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


    