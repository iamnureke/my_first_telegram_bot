import telebot
from telebot import types
import Utilities as U
from FakeStore import FakeStoreAPI

fake_store_api = FakeStoreAPI()

TOKEN = '6736451867:AAHa-o8Y7QakNH9dFD_FmOPZ114NhfLdaNE'
BOT_USERNAME = '@FakeStoreAPI_bot'

bot = telebot.TeleBot(TOKEN, parse_mode='MarkDown')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'''
Приветсвтую, **{message.from_user.first_name}**!
Это тестовый бот для FakeStoreAPI
Что я могу?
/help - переходите сюда
'''
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['products'])
def show_all_products(message):
    bot.send_message(message.chat.id, f'{U.do_format()}')


@bot.message_handler(commands=['categories'])
def show_all_categories(message):
    bot.send_message(message.chat.id, f'{U.show_categories()}')


@bot.message_handler(commands=['selectbyid'])
def select_by_id(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    for i in range(1, 21):
        arg = types.KeyboardButton(f'ID {i}')
        markup.add(arg)
        i += 1
    main = types.KeyboardButton('Главное меню')
    markup.add(main)
    bot.send_message(message.chat.id, '...', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    all_products = types.KeyboardButton('Все продукты')
    categories = types.KeyboardButton('Категории')
    products_by_id = types.KeyboardButton('Продукты по id')
    products_by_category = types.KeyboardButton('Продукты по категории')
    markup.add(all_products, categories, products_by_id, products_by_category)
    bot.send_message(message.chat.id, '...', reply_markup=markup)


@bot.message_handler(commands=['selectbycategory'])
def selectbycategory(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for category in fake_store_api.get_all_categories():
        categories = types.KeyboardButton(f'{category}')
        markup.add(categories)
    main = types.KeyboardButton('Главное меню')
    markup.add(main)
    bot.send_message(message.chat.id, '...', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func_button(message):
    if (message.text == 'Все продукты'):
        show_all_products(message)
    elif (message.text == 'Категории'):
        show_all_categories(message)
    elif (message.text == 'Продукты по id'):
        select_by_id(message)
    elif (message.text == 'Главное меню'):
        help(message)
    elif (message.text == 'Продукты по категории'):
        selectbycategory(message)
    elif (message.text == f'{fake_store_api.get_all_categories()[0]}'):
        bot.send_message(message.chat.id, f'{U.category_electronics()}')
    elif (message.text == f'{fake_store_api.get_all_categories()[1]}'):
        bot.send_message(message.chat.id, f'{U.category_jewelery()}')
    elif (message.text == f'{fake_store_api.get_all_categories()[2]}'):
        bot.send_message(message.chat.id, f'{U.category_men_clothing()}')
    elif (message.text == f'{fake_store_api.get_all_categories()[3]}'):
        bot.send_message(message.chat.id, f'{U.category_women_clothing()}')
    for i in range(0, 20):
        if (message.text == f'ID {i + 1}'):
            bot.send_message(message.chat.id, f'{U.do_format_list()[i]}')


bot.infinity_polling()
