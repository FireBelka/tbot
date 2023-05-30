from telebot import TeleBot
from telebot import types


choise =["","","",""]
houses = ["house", "summer", "cottage"]
costs=["15","15-25","25-50","50-100", "100-300", "300+"]
directions=["moscow","logo","madzel","hrodno","brest","dzer","slyck","other"]
ranges=["15km","30km","60km"]

def any_user(message: types.Message, bot: TeleBot):

    # keyboard
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton("Дом", callback_data=houses[0])
    item2 = types.InlineKeyboardButton("Коттедж", callback_data=houses[1])
    item3 = types.InlineKeyboardButton("Дача", callback_data=houses[2])
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Приветствую, {0.first_name}!\n Я - <b>{1.first_name}</b>, моя цель- провести вас по базовым вопросам, чтобы вам не пришлось просматривать неинтересующие вас варианты.\nДавайте начнём с типа жилья".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

def callback_inline(call, bot: TeleBot):

    try:
        if call.message:
            if call.data in houses:
                choise[0]=str(call.data)
                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton("До 15.000$", callback_data=costs[0])
                item2 = types.InlineKeyboardButton("15-25.000$", callback_data=costs[1])
                item3 = types.InlineKeyboardButton("25-50.000$", callback_data=costs[2])
                item4 = types.InlineKeyboardButton("50-100.000$", callback_data=costs[3])
                item5 = types.InlineKeyboardButton("100-300.000$", callback_data=costs[4])
                item6 = types.InlineKeyboardButton("300.000+$", callback_data=costs[5])
                markup.add(item1,item2,item3,item4,item5,item6)
                bot.send_message(call.message.chat.id, 'Отлично, теперь давайте определимся с бюджетом', reply_markup=markup)             
            elif call.data in costs:
                choise[1]=str(call.data)
                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton("Московское", callback_data=directions[0])
                item2 = types.InlineKeyboardButton("Логойское", callback_data=directions[1])
                item3 = types.InlineKeyboardButton("Мядельское", callback_data=directions[2])
                item4 = types.InlineKeyboardButton("Гродненское", callback_data=directions[3])
                item5 = types.InlineKeyboardButton("Брестское", callback_data=directions[4])
                item6 = types.InlineKeyboardButton("Дзержинское", callback_data=directions[5])
                item7 = types.InlineKeyboardButton("Слуцкое", callback_data=directions[6])
                item8 = types.InlineKeyboardButton("Другое", callback_data=directions[7])
                markup.add(item1,item2,item3,item4,item5,item6)
                bot.send_message(call.message.chat.id, 'Замечательно, осталось выбрать направление', reply_markup=markup)
            elif call.data in directions:  
                choise[2]=str(call.data)
                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton("До 15км", callback_data=ranges[0])
                item2 = types.InlineKeyboardButton("До 30км", callback_data=ranges[1])
                item3 = types.InlineKeyboardButton("До 60км", callback_data=ranges[2])
                markup.add(item1,item2,item3)
                bot.send_message(call.message.chat.id, 'Осталось чуть-чуть, какое расстояние от Минска для вас предпочтительно', reply_markup=markup)
            elif call.data in ranges:
                choise[3]=str(call.data)
                bot.send_message(call.message.chat.id, "Ваш выбор:\n{0} \n{1} \n{2} \n{3}".format(choise[0],choise[1],choise[2],choise[3])) 
            else :             
                bot.send_message(call.message.chat.id, 'Alart! Alart! Palestine is under attack!')              
 
 
    except Exception as e:
        print(repr(e))
