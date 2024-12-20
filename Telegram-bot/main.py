import telebot
import sqlite3

from django.contrib.messages.context_processors import messages

bot = telebot.TeleBot("")
name = None

@bot.message_handler(commands = ["start"])
def start(message):
    conn = sqlite3.connect('rezyx.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50)')
    conn.commit()
    cur.close()
    conn.close()


    bot.send_message(message.chat.id, "hello just a second we will register you, Print your name")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat_id, "Input your password")
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('rezyx.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES('%s', '%s')" %(name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Users list", callback_data='users'))
    bot.send_message(message.chat_id, "User was registered!", reply_markup = markup)

bot.polling(none_stop = True)