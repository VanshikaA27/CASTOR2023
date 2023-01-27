
import os

import telebot
os.environ["Token"] = "5834855129:AAGw5KJnmdpkGghD9qpp5LXmD_aL7BVhrS4"

BOT_TOKEN = os.getenv("Token")

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.infinity_polling()