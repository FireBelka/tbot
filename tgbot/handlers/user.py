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

def callback_inline(call, bot: TeleBot):
    try:
        if call.message:
            if call.data == 'flat':
                item1 = types.InlineKeyboardButton("Flat", callback_data='flat')
                markup.add(item1)
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊', reply_markup=markup)             
            elif call.data == 'cottage':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))
