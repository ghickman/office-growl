from Queue import Queue
from threading import Thread

from flask import Flask, request
from gntp.notifier import GrowlNotifier

from config import Config

c = Config('config.yaml')

NAME = c.config.get('app_name')
ICON_URL = c.config.get('icon_url')
NOTIFIER = c.config.get('notification_type')
TITLE = c.config.get('title')

def bark(message, host, password):
    growl = GrowlNotifier(
        applicationName = NAME,
        notifications = [NOTIFIER],
        defaultNotifications = [NOTIFIER],
        hostname = host,
        port = '23053',
        password = password
    )
    growl.register()

    growl.notify(
        noteType = NOTIFIER,
        title = TITLE,
        description = message,
        icon = ICON_URL,
        sticky = False,
        priority = 1,
    )

q = Queue()
def worker():
    while True:
        bark(**q.get())
        q.task_done()

t = Thread(target=worker)
t.daemon = True
t.start()

app = Flask(__name__)
@app.route('/', methods=['POST'])
def announce():
    for notification in request.json:
        q.put(notification)
    return ''

if __name__ == '__main__':
    app.run(debug=True)

