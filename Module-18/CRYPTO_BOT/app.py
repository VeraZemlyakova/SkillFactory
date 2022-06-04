import telebot
from extensions import ConvertionException, CryptoConverter
from config import TOKEN, currencies

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команду 'start'.
@bot.message_handler(commands=['start', ])
def handle_start(message: telebot.types.Message):
    name = message.chat.username if message.chat.username else message.chat.first_name
    bot.send_message(message.chat.id, f"Добро пожаловать, {name}!")
    handle_help(message)


# Обрабатываются все сообщения, содержащие команду '/help'.
@bot.message_handler(commands=['help', ])
def handle_help(message: telebot.types.Message):
    text = f'  Чтобы получить стоимость определенного количества валюты, введите команду боту в следующем формате:\n\
    <имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n\
    Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values', ])
def handle_values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'+'\n'.join(currencies.keys())
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def handle_text(message: telebot.types.Message):
    try:
        values = list(map(lambda x: x.lower(), message.text.split(' ')))
        if len(values) > 3:
            raise ConvertionException('Слишком много параметров.')
        elif len(values) < 3:
            raise ConvertionException('Слишком мало параметров.')
        base, quote, amount = values
        summ = CryptoConverter.get_price(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Стоимость {amount} {base} - {summ:.2f} {quote}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
