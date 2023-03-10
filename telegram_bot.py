'''
텔레그램을 활용한 챗봇
/로 시작하는 대화는 command
아니면 그냥 text
'''

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from chatgpt import chatGPT


token = ""
chat_id = ""
bot = telegram.Bot(token)

# Updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

# MessageHandler
def handler(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    text = chatGPT(user_text)
    context.bot.send_message(chat_id=user_id, text=text)



handler = MessageHandler(Filters.text & (~Filters.command), handler)
dispatcher.add_handler(handler)

updater.start_polling()









