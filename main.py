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

for peon in peons:
    bark('Burritos have Arrived.', peons[peon]['host'], peons[peon]['os'])

