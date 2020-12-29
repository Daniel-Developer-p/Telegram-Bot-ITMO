# Install pyTelegramBotAPI
# Install requests
# Register on webite http://api.openweathermap.org/data/2.5/weather
# And get api on this website http://api.openweathermap.org/data/2.5/weather
import requests
import telebot

url = 'http://api.openweathermap.org/data/2.5/weather'
api_weather = 'api your telegram bot'
api_telegram = 'api your telegram bot'

bot = telebot.TeleBot(api_telegram)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.username) + ',' + '\n' +
                     'чтоб узнать погоду напишите команду /weather <имя города>')


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id, '/start запуск бота\n/help команды бота\n/weather <имя города>')


@bot.message_handler(commands=['weather'])
def test(message):
    city_name = message.text[9:]

    try:
        params = {'APPID': api_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)
        weather = result.json()

        if weather["main"]['temp'] < 10:
            status = "Сейчас холодно!"
        elif weather["main"]['temp'] < 20:
            status = "Сейчас прохладно!"
        elif weather["main"]['temp'] > 38:
            status = "Сейчас жарко!"
        else:
            status = "Сейчас отличная температура!"

        bot.send_message(message.chat.id, "В городе " + str(weather["name"]) + " температура " + str(
            float(weather["main"]['temp'])) + "\n" +
                         "Максимальная температура " + str(float(weather['main']['temp_max'])) + "\n" +
                         "Минимальная температура " + str(float(weather['main']['temp_min'])) + "\n" +
                         "Скорость ветра " + str(float(weather['wind']['speed'])) + "\n" +
                         "Давление " + str(float(weather['main']['pressure'])) + "\n" +
                         "Влажность " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "Видимость " + str(weather['visibility']) + "\n" +
                         "Описание " + str(weather['weather'][0]["description"]) + "\n\n" + status)

    except:
        bot.send_message(message.chat.id, "Город " + city_name + " не найден")


if __name__ == '__main__':
    bot.polling(none_stop=True)
