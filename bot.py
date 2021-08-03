import telebot
import firestore_service
from models import User 
from firestore_service import order_list
import keyboards
import time 

import emoji
from credentials import TOKEN

bot = telebot.TeleBot(token=TOKEN)

#triggered when '/start'
#bot send intro message 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='Welcome to Josh Vape Shop',
        reply_markup=keyboards.main_keyboard()
        )
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Whoops. Something wrong happen. Try again'
        )

@bot.message_handler(commands=['Shop'])
def shop_item(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='we sell only our best',
        reply_markup=keyboards.shop_keyboard()
        )
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Whoops')



@bot.message_handler(regexp='Closed Pod System')
def closed_pod_item(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='Choose your closed pod:',
        reply_markup=keyboards.closed_pod()
        )
    
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Whoops')


@bot.message_handler(regexp='Open Pod System')
def open_pod_item(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='Choose your open pod',
        reply_markup=keyboards.open_pod()
        )
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Whoops')
    
@bot.message_handler(regexp='Local Flavours')
def local_flavours_item(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='Choose your local flavours',
        reply_markup=keyboards.local_flavours()
        )
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Whoops')

@bot.message_handler(regexp='Imported Flavours')
def imported_flavours_item(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='Choose your imported flavours',
        reply_markup=keyboards.imported_flavours()
        )
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Whoops')

@bot.message_handler(regexp='Accessories')
def accessories_item(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='Choose your accessories',
        reply_markup=keyboards.accessories()
        )
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Whoops')

@bot.message_handler(commands=['disposable'])
def disposable_item(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='Choose disposable',
        reply_markup=keyboards.disposable_keyboard())
    except:
        bot.send_message(chat_id=message.chat.id,
        text='whoops')

while True:
    try:
        bot.polling(none_stop=False)
    except Exception:
        print('crash')
        time.sleep(1)

