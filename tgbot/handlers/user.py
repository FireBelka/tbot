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
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("New", callback_data='Flat_new')
                item2 = types.InlineKeyboardButton("Old", callback_data='Flat_old')
                markup.add(item1,item2)
                bot.send_message(call.message.chat.id, 'Interior', reply_markup=markup)             
            elif call.data == 'cottage':
                bot.send_message(call.message.chat.id, 'Нет их в Беларуси')
            elif call.data == 'Flat_new':
                bot.send_message(call.message.chat.id, 'Однушка за почку')
            elif call.data == 'Flat_old':
                bot.send_message(call.message.chat.id, 'Сталинка с бабкой')    
            else :
                bot.send_message(call.message.chat.id, 'Alart! Alart! Palestine is under attack!')              
 
 
    except Exception as e:
        print(repr(e))
