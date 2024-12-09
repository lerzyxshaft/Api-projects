import telebot
import sqlite3

from django.contrib.messages.context_processors import messages

bot = telebot.TeleBot("7830554349:AAHlAKM1UmynK3HPEM1LxL9zk7zHsFA7cvc")

@bot.message_handler(commands = ["start"])
def start(massage):
    conn = sqlite3.connect('rezyx.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "hello just a second we will register you, Print your name")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    name = message.text.strip()
    bot

bot.polling(none_stop = True)