import telebot
import webbrowser

bot = telebot.TeleBot("")

@bot.message_handler(commands = ["start"])
def main(massage):
    bot.send_message(massage.chat.id, f"Привет! {massage.from_user.first_name}, {massage.from_user.last_name }")

@bot.message_handler()
def info_eng(message):
    if message.text.lower() == "Info":
        bot.send_message(message.chat.id, "We creating telegram's bots any difficulty levels!")
    elif message.text.lower() == "Инфо":
        bot.send_message(message.chat.id, "Мы создаем телеграм каналы любой сложности!")
    elif message.text.lower() == "id":
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == "about"
        bot.send_message(message.chat.id, "Bot was created to check all the problems ")
    elif message.text_lower() == "me":
        bot.send.message(message.shat.id)

@bot.message_handler(commands = ["site", "website"])
def site(message):
    webbrowser.open('https://web.telegram.org/k/')

def menu

@bot.message_handler(commands = ["help"])
def main(massage):
    bot.send_message(massage.chat.id, "<b>Данный бот создан для наглядного примера работы ботов в телеграмме<b/>", parse_mode = "html")

bot.polling(none_stop = True)