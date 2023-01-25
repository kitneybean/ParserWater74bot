import telebot
from Excel import *
from WORD import *
from telebot import types 
token = '5981565293:AAHy-6cyloxhxEIOyMPQEE69yILMOiTpByk'    #ТОКЕН БОТА, ПРИ КОПИРОВАНИИ СКРИПТА ПОСТАВИТЬ СВОЙ
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🏷️ Акции")
    btn2 = types.KeyboardButton("💵 Цены")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для парсинга цен и акций".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🏷️ Акции"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📝Спарсить акции")
        btn2 = types.KeyboardButton("🔚Последний файл акций")
        btn3 = types.KeyboardButton("🔙 Назад")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите, что вы хотите", reply_markup=markup)
    elif(message.text == "💵 Цены"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📝Спарсить цены")
        btn2 = types.KeyboardButton("🔚Последний файл цен")
        btn3 = types.KeyboardButton("🔙 Назад")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите, что вы хотите", reply_markup=markup)
    elif(message.text == "📝Спарсить акции"):
        bot.send_message(message.chat.id, "Сайты парсятся, пожалуйста подождите...")
        try:
            parsing_aktsii()
            f = open("PARSER.docx","rb")
        except:
            bot.send_message(message.chat.id, "Не удалось спарсить сайты, последняя версия:")
            f = open("PARSER.docx","rb")
        bot.send_document(message.chat.id,f)
    elif (message.text == "🔚Последний файл акций"):
        bot.send_message(message.chat.id, "Последний файл акций:")
        f = open("PARSER.docx","rb")
        bot.send_document(message.chat.id,f)
    elif(message.text == "📝Спарсить цены"):
        bot.send_message(message.chat.id, "Сайты парсятся, пожалуйста подождите")
        try:
            parsing()
            f = open("PARSER.xlsx","rb")
        except:
            bot.send_message(message.chat.id, "Не удалось спарсить сайты, последняя версия:")    
            f = open("PARSER.xlsx","rb")
        bot.send_document(message.chat.id,f)
    elif (message.text == "🔚Последний файл цен"):
        bot.send_message(message.chat.id, "Последний файл цен:")
        f = open("PARSER.xlsx","rb")
        bot.send_document(message.chat.id,f)
    elif message.text == "🔙 Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🏷️ Акции")
        btn2 = types.KeyboardButton("💵 Цены")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")

bot.polling(none_stop=True, interval=0)

