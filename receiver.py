from datetime import datetime
from time import sleep
import requests

after = 0


class ChatBot:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def say_hello(self):
        return f'Hello, my name {self.name}'

    def say_buy(self):
        return f'Buy, see you!'


bot = ChatBot('Alexx')


def print_message(message):
    beauty_time = datetime.fromtimestamp(message['time'])
    beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M')
    print(beauty_time, message['name'])
    print(message['text'])
    print()


while True:
    params = {'after': after}
    response = requests.get('http://127.0.0.1:5000/messages', params=params)
    data = response.json()  # {'messages': messages}

    for message in data['messages']:
        # if message['text'].lower() == 'hello':
        #     print(bot.say_hello())
        if 'Hello' in message['text']:
            bot.say_hello()
        print_message(message)

        after = message['time']

    sleep(1)  # засыпаем на 1 секунду
