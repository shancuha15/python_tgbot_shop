from telebot import types


btn_products = types.KeyboardButton('🛒 Товари')
btn_information = types.KeyboardButton('ℹ️ Інформація о нас')
btn_support = types.KeyboardButton('✉️ Підтримка')
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btn_products, btn_information,
                                                                               btn_support)


btn_perechen_products = types.InlineKeyboardButton('📃 Перелік товарів', callback_data='📃 Перелік товарів')
btn_nabor = types.InlineKeyboardButton('📦 Набори', callback_data='📦 Набори')
btn_sale = types.InlineKeyboardButton('📉 Знижки', callback_data='📉 Знижки')
btn_personal_zakaz = types.InlineKeyboardButton('💁 Персональне замовлення', callback_data='💁 Персональне замовлення')
btn_back_main_menu = types.InlineKeyboardButton('⬅️Назад', callback_data='⬅️Назад')
markup_products = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btn_perechen_products, btn_nabor,
                                                                                   btn_sale, btn_personal_zakaz,
                                                                                   btn_back_main_menu)


btn_Rita = types.InlineKeyboardButton('📩 Додаткова інформація', callback_data='📩 Додаткова інформація')
btn_Vlad = types.InlineKeyboardButton('📩 Технічна підтримка', callback_data='📩 Технічна підтримка')
markup_support = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btn_Rita, btn_Vlad,
                                                                                  btn_back_main_menu)


buttonVlad = types.InlineKeyboardButton("Вже допомагаю!👨🏻‍💻", url='https://t.me/hrdrfstrsmtr')
markup_follow_Vlad = types.InlineKeyboardMarkup().add(buttonVlad)


buttonRita = types.InlineKeyboardButton("Вже слухаю!👩🏻‍💻️", url='https://t.me/rita_bgrv')
markup_follow_Rita = types.InlineKeyboardMarkup().add(buttonRita)


btn_stiker = types.InlineKeyboardButton('📃 Стікери', callback_data='📃 Стікери')
btn_notebook = types.InlineKeyboardButton('📓 Блокноти', callback_data='📓 Блокноти')
btn_paintings = types.InlineKeyboardButton('🎨 Картини', callback_data='🎨 Картини')
btn_back_perechen_products = types.InlineKeyboardButton('⬅️Нaзад', callback_data='⬅️Нaзад')
markup_perelik = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btn_stiker, btn_notebook,
                                                                                  btn_paintings,
                                                                                  btn_back_perechen_products)


switch_button = types.InlineKeyboardButton(text='Поділитися з друзями', switch_inline_query="Диви який крутий магазин!")
markup_share = types.InlineKeyboardMarkup().add(switch_button)



