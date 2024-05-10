import requests 
import telebot  
import json
from random import randint 
from telebot import TeleBot, types 

bot = telebot.TeleBot("6818572449:AAH6JEdjePFscHfPS2EPP_cuqRUcme4Ss5M") 

def random_duck(): 
    url = 'https://random-d.uk/api/random' 
    res = requests.get(url) 
    data = res.json() 
    return data['url'] 

@bot.message_handler(commands=['help']) 
def start(message): 
    bot.send_message(message.chat.id, "Ты что-то не раслышал? Ты можешь сделать это - /duck (Мои фото карточки с утками), /Joke1, /Joke2, /Joke3 (Это мои шуточки которые я сам знаю), /help (Повторю если захочешь)") 
 
@bot.message_handler(commands=['Joke2']) 
def start(message): 
    bot.send_message(message.chat.id, " Орк стрижет эльфа.  - Эльф, тебе уши нужны?  - Конечно.  - На, держи!")

@bot.message_handler(commands=['Joke3']) 
def start(message): 
    bot.send_message(message.chat.id, "И из тьмы Мории на мост вступил нечто состоящее из огня и мрака и над ним развевался пламенный хлыст. (Задолбали эти кибердемоны) - Подумал Гэндальф, переключая плазмаган на ближний бой.")

@bot.message_handler(commands=['duck']) 
def duck(message): 
    print('1') 
    url = random_duck() 
    bot.send_message(message.chat.id, url) 
 
@bot.message_handler(func=lambda message: True) 
def echo_all(message): 
    bot.reply_to(message, message.text) 
 
 
bot.infinity_polling()
