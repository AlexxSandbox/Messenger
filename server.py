# python server.py
# localhost:5000
import time
from flask import Flask, request, abort
from datetime import datetime as dt

app = Flask(__name__)

db = [
    {
        'name': 'Jack',
        'text': 'Hello all',
        'time': time.time()
    },
    {
        'name': 'Mick',
        'text': 'Hello Jack',
        'time': time.time()
    }
]


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    time_now = dt.utcnow()
    return {'status': True,
            'name': 'alexx',
            'time': time_now,
            'users': len(set([user['name'] for user in db])),
            'messages': len(db)
            }


@app.route("/send", methods=['POST'])
def send_message():
    # если post запрос пришел пустой
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    # если в post запросе нет поля name, text
    if not (name and text and isinstance(name, str) and isinstance(text, str)):
        return abort(400)

    new_message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    db.append(new_message)

    return {'ok': True}


@app.route("/messages")
def get_message():
    try:
        after = float(request.args.get('after', 0))
    except ValueError:
        return abort(400)

    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)

    return {
        'messages': messages
    }


app.run()
