# handlers
#from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import any_user, callback_inline

# middlewares
from tgbot.middlewares.antiflood_middleware import antispam_func

# states
from tgbot.states.register_state import Register

# telebot
from telebot import TeleBot

# config
from tgbot import config


# remove this if you won't use middlewares:
from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True

# I recommend increasing num_threads
bot = TeleBot(config.TOKEN, num_threads=5)
def register_handlers():
    bot.register_message_handler(any_user, commands=['start'], pass_bot=True)
    #bot.register_message_handler(callback_inline, commands=['start'], pass_bot=True)


register_handlers()

# Middlewares
bot.register_middleware_handler(antispam_func, update_types=['message'])

# query_handler
bot.register_callback_query_handler(callback_inline,func=lambda call: True)


def run():
    bot.infinity_polling()


run()
