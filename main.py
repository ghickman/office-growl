from Queue import Queue
from threading import Thread

from flask import Flask, request
from gntp.notifier import GrowlNotifier

NAME = ''
ICON_URL = ''
NOTIFIER = ''
PORTS = {'lion': 23053, 'snow leopard': 23052}
TITLE = ''

def bark(message, host, os, password):
    growl = GrowlNotifier(
        applicationName = NAME,
        notifications = [NOTIFIER],
        defaultNotifications = [NOTIFIER],
        hostname = host,
        port = PORTS[os],
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

app = Flask(__name__)
@app.route('/growl', methods=['POST'])
def announce():
    q.put(request.json)
    return ''

if __name__ == '__main__':
    t = Thread(target=worker)
    t.daemon = True
    t.start()
    app.run(debug=True)

