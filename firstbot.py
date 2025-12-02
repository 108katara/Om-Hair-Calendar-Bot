import telebot
bot = telebot.TeleBot('8502864198:AAFjBpRlPNauYrH_juJi1beG-B-48wKHUT0')

FAVORABLE_DAYS = ['01.12.2025', '03.12.2025', '08.12.2025', '10.12.2025',
                  '11.12.2025', '12.12.2025', '15.12.2025', '16.12.2025',
                  '17.12.2025', '25.12.2025', '27.12.2025', '29.12.2025',
                  '30.12.2025']

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, хочешь постричься по лунному календарю, но не знаешь когда благоприятный день? Пиши дату')

@bot.message_handler(commands=['help'])
def help(message):
    help_text = """
    📅 *Как пользоваться ботом:*
1. Отправьте дату в формате *ДД.ММ.ГГГГ*
   Пример: *01.12.2025*
2. Бот определит, благоприятный ли это день для стрижки

📋 *Доступные команды:*
/start - начать работу
/help - эта справка
    """
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def date(message):
    user_date = message.text.strip()
    if user_date in FAVORABLE_DAYS:
        bot.send_message(message.chat.id, 'День благоприятный')
    else:
        if '.' in user_date and len(user_date.split('.')) == 3:
            bot.send_message(message.chat.id, 'День неблагоприятный')
        else:
            bot.send_message(message.chat.id, 'Перепроверьте дату. Формат: ДД.ММ.ГГГГ')












bot.infinity_polling()