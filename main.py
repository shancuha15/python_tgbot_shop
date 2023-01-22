import sqlite3

import telebot

import btn as nav
import const
import db as dbv
import reminder as rem

# Token connection.
bot = telebot.TeleBot(const.API_TOKEN)


# Database connection.
conn = sqlite3.connect('botusers.db', check_same_thread=False)
cursor = conn.cursor()


# Sending a message from the reminder.txt file to users from the database entered in the user_list.txt file.
# Only an administrator with a unique username can send messages to users.
@bot.message_handler(commands=['reminder'])
def reminder(message):
    token = const.API_TOKEN
    chatID = []
    calc = 0
    text_file = open('reminder.txt', 'r', encoding='utf-8')
    text = text_file.read()
    text_file.close()
    u_id = message.from_user.username
    if u_id == 'hrdrfstrsmtr':
        file = open('user_list.txt')
        for i in file:
            chatID.append(i)
            calc += 1
        file.close()
        chatID = [x.replace('\n', '') for x in chatID]
        for i in chatID:
            rem.send_text(token, i, text)


# The "start" command sends a greeting to the user, collects information about the user in the database.
@bot.message_handler(commands=['start'])
def start(message):
    username = []
    name = message.from_user.username
    bot.send_message(message.chat.id, text=""" 
    Вас вітає інтернет-магазин Artspase 🎨✨
Тут ти можеш переглянути, обрати та замовити товари, які тобі довподоби ☺️Обирай необхідну опцію та тицяй на відповідну кнопку! Я чекаю..
    """.format(message.from_user),
                     reply_markup=nav.markup_menu)
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    dbv.db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


# The "Contacts" command sends to the user necessary information to contact the owner.
@bot.message_handler(commands=['contacts'])
def contact(message):
    bot.send_message(message.chat.id, text="""
    Наші контакти:
    
@rita_bgrv - власниця 📩
@hrdrfstrsmtr - технічна підтримка 🛠
    """.format(message.from_user))


# Commands that respond to button clicks.
@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == "🛒 Товари":
        bot.send_message(message.chat.id, "coming soon...",
                         reply_markup=nav.markup_products)
    elif message.text == "ℹ️ Інформація о нас":
        bot.send_message(message.chat.id, """coming soon...""", reply_markup=nav.markup_menu)
    elif message.text == "✉️ Підтримка":
        bot.send_message(message.chat.id, """
        Вас вітає підтримка магазину Artspase. 💬
У вас щось трапилось? 🤯😱
     ▪️Для вирішення вашого питання чи для пропозицій натисніть клавішу «Додаткова інформація». 
      ▪️ Для вирішення технічних питань натисніть клавішу «Технічна підтримка». 
                                            """, reply_markup=nav.markup_support)
    elif message.text == '📃 Перелік товарів':
        bot.send_message(message.chat.id, text="""📃 Перелік товарів!""", reply_markup=nav.markup_perelik)
    elif message.text == '📦 Набори':
        bot.send_message(message.chat.id, text="""coming soon...""",
                         reply_markup=nav.markup_products)
    elif message.text == '📉 Знижки':
        bot.send_message(message.chat.id, text="""coming soon...""", reply_markup=nav.markup_products)
    elif message.text == '💁 Персональне замовлення':
        bot.send_message(message.chat.id, text="""coming soon...""", reply_markup=nav.markup_products)
    elif message.text == '⬅️Назад':
        bot.send_message(message.chat.id, text='Повертаю назад!', reply_markup=nav.markup_menu)
    elif message.text == '📩 Додаткова інформація':
        bot.send_message(message.chat.id, text="""Натисни тут 👇🏻️""",
                         reply_markup=nav.markup_follow_Rita)
    elif message.text == '📩 Технічна підтримка':
        bot.send_message(message.chat.id, text="""Натисни тут 👇🏻️""", reply_markup=nav.markup_follow_Vlad)
    elif message.text == '📓 Блокноти':
        info_notebook_list = {'1': '1-й блокнот', '2': '2-й блокнот', '3': '3-й блокнот', '4': '4-й блокнот',
                              '5': '5-й блокнот', '6': '6-й блокнот'}
        a = '.png'
        for i in range(1, len(info_notebook_list) + 1, 1):
            conv = str(i)
            bot.send_photo(message.chat.id, photo=open(r"pictures/notebook/notebook" + conv + a
                                                       , 'rb'), caption=info_notebook_list[conv])
    elif message.text == '🎨 Картини':
        info_painting_list = {'1': '1-а картина', '2': '2-а картина', '3': '3-я картина', '4': '4-а картина',
                              '5': '5-а картина', '6': '6-а картина', '7': '7-а картина'}
        a = '.png'
        for i in range(1, len(info_painting_list) + 1, 1):
            conv = str(i)
            bot.send_photo(message.chat.id, photo=open(r"pictures/painting/paint" + conv + a,
                                                       'rb'), caption=info_painting_list[conv])
    elif message.text == '📃 Стікери':
        info_sticker_list = {'1': '1-й стік ', '2': '2-й стік', '3': '3-й стік', '4': '4-й стік', '5': '5-й стік',
                             '6': '6-й стік'}
        a = '.png'
        for i in range(1, len(info_sticker_list) + 1, 1):
            conv = str(i)
            bot.send_photo(message.chat.id, photo=open(r"pictures/stickers/stick" + conv + a,
                                                       'rb'), caption=info_sticker_list[conv])
    elif message.text == '🫶Розказати про нас':
        bot.send_message(message.chat.id, "👇🏻", reply_markup=nav.markup_share)
    elif message.text == '⬅️Нaзад':
        bot.send_message(message.chat.id, text='Повертаю назад!', reply_markup=nav.markup_products)
    else:
        bot.reply_to(message, """Я вас не розумію""", reply_markup=nav.markup_menu)


if __name__ == '__main__':
    bot.polling()
