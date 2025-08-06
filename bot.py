import telebot
import os

TOKEN = "8392455786:AAE70XdMc_WQO4Cutb_1biitUeweCRENDjU"  # তোমার বট টোকেন
bot = telebot.TeleBot(TOKEN)

# /start কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    link = "https://fanciful-haupia-f0127e.netlify.app/"
    bot.send_message(message.chat.id, f"হ্যালো {message.from_user.first_name}! 👋\n\nএই লিংকটি দেখুন: {link}")

# বট চালু রাখা
bot.polling(none_stop=True)
