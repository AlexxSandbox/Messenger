from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore

import clientui


class Window(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self, url='http://127.0.0.1:5000'):
        super().__init__()
        self.setupUi(self)

        self.url = url

        self.pushButton.pressed.connect(self.send_message)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            response = requests.post(self.url + '/send', json={'name': name, 'text': text})
        except:
            self.textBrowser.append('Server don\'t work')
            self.textBrowser.append('')
            return

        if response.status_code != 200:
            self.textBrowser.append('Input name or text')
            self.textBrowser.append('')
            return

        self.textEdit.clear()

    def get_messages(self):
        params = {'after': self.after}
        try:
            response = requests.get(self.url + '/messages', params=params)
        except:
            return

        data = response.json()

        for message in data['messages']:
            self.print_message(message)
            self.after = message['time']

    def print_message(self, message):
        beauty_time = datetime.fromtimestamp(message['time'])
        beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M')
        self.textBrowser.append(beauty_time + ' ' + message['name'])
        self.textBrowser.append(message['text'])
        self.textBrowser.append('')


app = QtWidgets.QApplication([])
window = Window()  # ./ngrok http 5000 -> Window(url='http://...')
window.show()
app.exec_()
