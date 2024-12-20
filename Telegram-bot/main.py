import telebot
import sqlite3

from django.contrib.messages.context_processors import messages

bot = telebot.TeleBot("783055knjklpl;kj4349:AAHlAKjnbmM1UmynK3HPEM1LxL9zk7zHsFA7cvc")
name = None

@bot.message_handler(commands = ["start"])
def start(message):
    conn = sqlite3.connect('rezyx.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
    conn.commit()
    cur.close()
    conn.close()


    bot.send_message(message.chat.id, "Hello just a second we will register you, Print your name")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Input your password")
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
    bot.send_message(message.chat.id, "User was registered!", reply_markup = markup)

@bot.callback_query_handler(func = lambda call: True)
def  callback(call):
    conn = sqlite3.connect('rezyx.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Name: {el[1]}, password: {el[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.polling(none_stop = True)