import telebot

bot = telebot.TeleBot('6383276353:AAE09Od66pMkM2CzM3RXVsIRUwaIIlrecdU')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'welcome!')

@bot.message_handler(commands = ['help'])
def main(message):
    bot.send_message(message.chat.id, 'help information')



bot.infinity_polling()