import time
import datetime as dt

message1 = {
    'name': 'Jack',
    'text': 'Hello all',
    'time': time.time()
}

message2 = {
    'name': 'Mick',
    'text': 'Hello Jack',
    'time': time.time()
}

db = [message1, message2]


def send_message(name, text):
    new_message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    db.append(new_message)


def get_message(after=0):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return messages


def print_messages(messages):
    for message in messages:
        beauty_time = dt.datetime.fromtimestamp(message['time']).strftime('%Y/%m/%d %H:%M')
        print(beauty_time, message['name'])
        print(message['text'])
        print()
