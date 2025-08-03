from flask import Flask, request
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # Render থেকে ENV VAR ব্যবহার করবো
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

HTML_LINK = "https://helpful-blancmange-f00c2d.netlify.app/"  # এখানে তোমার HTML লিঙ্ক বসাও

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"👋 হ্যালো!\nতোমার সাইটের লিঙ্ক:\n{HTML_LINK}")

@server.route("/" + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.stream.read().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://YOUR_RENDER_APP_NAME.onrender.com/" + TOKEN)
    return "Bot is running!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))