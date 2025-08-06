import os
import telebot
from flask import Flask, request

TOKEN = "8392455786:AAE70XdMc_WQO4Cutb_1biitUeweCRENDjU"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 হ্যালো! এখানে তোমার লিংক: https://fanciful-haupia-f0127e.netlify.app/")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://telegram-bot-jfrs.onrender.com" + TOKEN)
    return "Bot is running!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

