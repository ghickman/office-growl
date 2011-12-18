# Office Growl

Provides a web facing API to expose Growl Network Notifications via the GNTP protocol.

## Installation

Clone the repository:

    git clone git://github.com/ghickman/office-growl.git

Set the variables:

    NAME = 'My application name'
    ICON_URL = 'http://example.com/some/path.[ico|png]'
    NOTIFIER = 'A name for the notifier'
    PORTS = {'lion': 23053, 'snow leopard': 23052}
    TITLE = 'Notification name'


## Deployment

Most likely Nginx and Gunicorn.

## To Do

Document the deployment with SSL support.
The password is being sent in plain text right now. Use base64 to encode it and update this project to deal with it in that format.

