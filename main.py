import lamda
import telebot
from telebot import types
import webbrowser


bot = telebot.TeleBot('6383276353:AAE09Od66pMkM2CzM3RXVsIRUwaIIlrecdU')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт Python', url = 'https://python.org')
    btn2 = types.InlineKeyboardButton('Перейти на сайт Apple', url='https://apple.com')
    btn3 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn4 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)

    bot.reply_to(message, 'nice picture!', reply_markup = markup)

@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Text was deleted', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands = ['site', 'website', 'python', 'python check'])
def site(message):
    webbrowser.open('https://python.org')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    initialsCheck(message)

@bot.message_handler(commands = ['help'])
def main(message):
    bot.send_message(message.chat.id, 'help information')

def initialsCheck(message):
    if (message.from_user.last_name != None):
        bot.send_message(message.chat.id, f'welcome {message.from_user.first_name} {message.from_user.last_name}!')
    else:
        bot.send_message(message.chat.id, f'welcome {message.from_user.first_name}!')

@bot.message_handler()
def info(message):
    user_message = message.text.lower()
    if user_message == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif user_message == 'hi' or 'hello' or 'start' or 'main':
        initialsCheck(message)

bot.polling(none_stop=True)