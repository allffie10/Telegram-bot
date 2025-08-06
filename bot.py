import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

# তোমার Netlify HTML লিঙ্ক
HTML_LINK = "https://helpful-blancmange-f00c2d.netlify.app/"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"👋 হ্যালো! এখানে তোমার লিঙ্ক:\n{HTML_LINK}")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegram-bot-jfrs.onrender.com/' + TOKEN)
    return "Webhook set", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
