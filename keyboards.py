from telebot import types
from telebot.types import Message


def main_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('/Shop')
    itembtnb = types.KeyboardButton('/Contact')
    itembtnc = types.KeyboardButton('/FAQ')  # keyboard input
    itembtnd = types.KeyboardButton('/Shipping')
    itembtne = types.KeyboardButton('/Pick Up')
    itembtnf = types.KeyboardButton('/Payment')
    itembtng = types.KeyboardButton('/register')
    itembtnh = types.KeyboardButton('/disposable')
    markup.row(itembtna, itembtnb, itembtnc) # keyboard layout
    markup.row(itembtnd, itembtne, itembtnf,itembtng,itembtnh)
    return markup 

def shop_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('Closed Pod System')
    itembtnb = types.KeyboardButton('Open Pod System')
    itembtnc = types.KeyboardButton('Local Flavours')
    itembtnd = types.KeyboardButton('Imported Flavours')
    itembtne = types.KeyboardButton('Accessories')
    markup.row(itembtna, itembtnb)
    markup.row(itembtnc, itembtnd, itembtne)
    return markup

def disposable_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('Jojo')
    itembtnb = types.KeyboardButton('Haha')
    markup.row(itembtna)
    markup.row(itembtnb)
    return markup


def closed_pod():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('Pod A')
    itembtnb = types.KeyboardButton('Pod B')
    itembtnc = types.KeyboardButton('Pod C')
    itembtnd = types.KeyboardButton('Josh Pod') 
    markup.row(itembtna, itembtnb)
    markup.row(itembtnc, itembtnd)
    return markup 

def open_pod():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('Pod A')
    itembtnb = types.KeyboardButton('Pod B')
    markup.row(itembtna, itembtnb)
    return markup 

def local_flavours():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('Flavour A')
    itembtnb = types.KeyboardButton('Flavour B')
    markup.row(itembtna, itembtnb)
    return markup 

def imported_flavours():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('Int Flav A')
    itembtnb = types.KeyboardButton('Int Flav B')
    markup.row(itembtna, itembtnb)
    return markup 

def accessories():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('Accessories A')
    itembtnb = types.KeyboardButton('Accessories B')
    markup.row(itembtna, itembtnb)
    return markup 
 



 


def remove_keyboard():
    markup = types.ReplyKeyboardRemove()
    return markup 


