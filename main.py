from gntp.notifier import GrowlNotifier

ports = {'lion': 23053, 'snow leopard': 23052}

peons = {'george': {'host': 'localhost', 'os': 'lion'}}

incuna_main = 'Incuna Notifier'

def bark(message, host, os):
    growl = GrowlNotifier(
        applicationName = 'Incuna Public Service Announcements',
        notifications = [incuna_main],
        defaultNotifications = [incuna_main],
        hostname = host,
        port = ports[os],
    )
    growl.register()

    growl.notify(
        noteType = incuna_main,
        title = 'Incuna PSA',
        description = message,
        icon = 'http://incuna.com/favicon.ico',
        sticky = False,
        priority = 1,
    )

from Queue import Queue
from threading import Thread
q = Queue()
def worker():
    while True:
        item = q.get()
        bark(item['message'], item['host'], item['os'])
        q.task_done()

from flask import Flask, request
app = Flask(__name__)

@app.route('/growl', methods=['POST'])
def hello():
    q.put(request.json)
    return ''

if __name__ == '__main__':
    t = Thread(target=worker)
    t.daemon = True
    t.start()

    app.debug = True
    app.run()

