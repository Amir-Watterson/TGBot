import telebot
import webbrowser

bot = telebot.TeleBot('7482070870:AAHM371n7SapG_bZG4ltFZsyfoh8nx7OwxI')

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://t.me/bunkeramira')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Помощь</b> <em>Инфа</em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)