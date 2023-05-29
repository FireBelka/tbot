from telebot import TeleBot
from telebot import types

def any_user(message: types.Message, bot: TeleBot):

    # keyboard
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton("Дом", callback_data='house')
    item2 = types.InlineKeyboardButton("Коттедж", callback_data='cottage')
    item3 = types.InlineKeyboardButton("Дача", callback_data='summer')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Приветствую, {0.first_name}!\n Я - <b>{1.first_name}</b>, моя цель- провести вас по базовым вопросам, чтобы вам не пришлось просматривать неинтересующие вас варианты.\nДавайте начнём с типа жилья".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

def callback_inline(call, bot: TeleBot):
    house = "house"
    summer= "summer"
    cottage = "cottage"
    cost15 = "15"
    cost25= "15-25"
    cost50= "25-50"
    cost100= "50-100"
    cost300= "100-300"
    costalot= "300+"
    try:
        if call.message:
            if call.data == 'house':
                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton("До 15.000$", callback_data='house_15')
                item2 = types.InlineKeyboardButton("15-25.000$", callback_data='house_15-25')
                item3 = types.InlineKeyboardButton("25-50.000$", callback_data='house_25-50')
                item4 = types.InlineKeyboardButton("50-100.000$", callback_data='house_50-100')
                item5 = types.InlineKeyboardButton("100-300.000$", callback_data='house_100-300')
                item6 = types.InlineKeyboardButton("300.000+$", callback_data='house_300+')
                markup.add(item1,item2,item3,item4,item5,item6)
                bot.send_message(call.message.chat.id, 'Отлично, теперь давайте определимся с бюджетом', reply_markup=markup)             
            elif call.data == 'cottage':
                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton("До 15.000$", callback_data='cottage_15')
                item2 = types.InlineKeyboardButton("15-25.000$", callback_data='cottage_15-25')
                item3 = types.InlineKeyboardButton("25-50.000$", callback_data='cottage_25-50')
                item4 = types.InlineKeyboardButton("50-100.000$", callback_data='cottage_50-100')
                item5 = types.InlineKeyboardButton("100-300.000$", callback_data='cottage_100-300')
                item6 = types.InlineKeyboardButton("300.000+$", callback_data='cottage_300+')
                markup.add(item1,item2,item3,item4,item5,item6)
                bot.send_message(call.message.chat.id, 'Отлично, теперь давайте определимся с бюджетом', reply_markup=markup)
            elif call.data == 'summer':
                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton("До 15.000$", callback_data='summer_15')
                item2 = types.InlineKeyboardButton("15-25.000$", callback_data='summer_15-25')
                item3 = types.InlineKeyboardButton("25-50.000$", callback_data='summer_25-50')
                item4 = types.InlineKeyboardButton("50-100.000$", callback_data='summer_50-100')
                item5 = types.InlineKeyboardButton("100-300.000$", callback_data='summer_100-300')
                item6 = types.InlineKeyboardButton("300.000+$", callback_data='summer_300+')
                markup.add(item1,item2,item3,item4,item5,item6)
                bot.send_message(call.message.chat.id, 'Отлично, теперь давайте определимся с бюджетом', reply_markup=markup) 
            elif house in call.data:
                if cost15 in call.data:
                    markup = types.InlineKeyboardMarkup(row_width=3)
                    item1 = types.InlineKeyboardButton("Московское", callback_data='h15moscow')
                    item2 = types.InlineKeyboardButton("Логойское", callback_data='h15logo')
                    item3 = types.InlineKeyboardButton("Мядельское", callback_data='h15madzel')
                    item4 = types.InlineKeyboardButton("Гродненское", callback_data='h15hrodno')
                    item5 = types.InlineKeyboardButton("Брестское", callback_data='h15brest')
                    item6 = types.InlineKeyboardButton("Дзержинское", callback_data='h15dzer')
                    item7 = types.InlineKeyboardButton("Слуцкое", callback_data='h15slyck')
                    item8 = types.InlineKeyboardButton("Другое", callback_data='h15other')
                    markup.add(item1,item2,item3,item4,item5,item6)
                    bot.send_message(call.message.chat.id, 'Дом - бюджет до 15.000$. Теперь давайте определимся с направлением от Минска', reply_markup=markup)
                elif cost25 in call.data:
                    markup = types.InlineKeyboardMarkup(row_width=3)
                    item1 = types.InlineKeyboardButton("Московское", callback_data='h25moscow')
                    item2 = types.InlineKeyboardButton("Логойское", callback_data='h25logo')
                    item3 = types.InlineKeyboardButton("Мядельское", callback_data='h25madzel')
                    item4 = types.InlineKeyboardButton("Гродненское", callback_data='h25hrodno')
                    item5 = types.InlineKeyboardButton("Брестское", callback_data='h25brest')
                    item6 = types.InlineKeyboardButton("Дзержинское", callback_data='h25dzer')
                    item7 = types.InlineKeyboardButton("Слуцкое", callback_data='h25slyck')
                    item8 = types.InlineKeyboardButton("Другое", callback_data='h25other')
                    markup.add(item1,item2,item3,item4,item5,item6)
                    bot.send_message(call.message.chat.id, 'Дом - бюджет до 25.000$. Теперь давайте определимся с направлением от Минска', reply_markup=markup)                                      


            else :
                bot.send_message(call.message.chat.id, 'Alart! Alart! Palestine is under attack!')              
 
 
    except Exception as e:
        print(repr(e))
