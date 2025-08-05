import telebot

TOKEN = "8392455786:AAE70XdMc_WQO4Cutb_1biitUeweCRENDjU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ হ্যালো! এখানে তোমার HTML লিংক: https://helpful-blancmange-f00c2d.netlify.app/")

bot.polling(none_stop=True)
