import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN") or "8089134455:AAGgKCQ72yb3WbihwqHumJARjSUrKv5H0q8"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

HTML_LINK = "https://fanciful-haupia-f0127e.netlify.app/"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"হ্যালো 👋\nএখানে তোমার সাইট: {HTML_LINK}")

@server.route(f"/{TOKEN}", methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://telegram-bot-jfrs.onrender.com/{TOKEN}")
    return "Webhook set", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
