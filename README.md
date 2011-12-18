# Office Growl
Provides a web facing API to expose Growl Network Notifications via the GNTP protocol.

## Installation

Clone the repository:

    git clone git://github.com/ghickman/office-growl.git

Copy the example config file:

    cp config.yaml.example config.yaml

Set the variables to something useful:

    app_name: 'Your Application Name'
    icon_url: 'http://example.com/favicon.ico'
    notification_type: 'Main'
    title: 'Notification Title'

Install the dependencies:

    pip install -r requirements.txt

Test the application works by running the flask development server:

    python main.py


## Deployment
### Supervisor & Gunicorn
Use your favourite package manager:

    sudo aptitude install supervisor

Create a supervisor config file for the site:

    sudo vim /etc/supervisor/conf.d/office-growl.conf

Add the config for gunicorn:

    [program:office_growl]
    command=(/usr/bin/cd /var/www/office_growl; /var/www/office_growl/bin/gunicorn -w 2 -b 127.0.0.1:4000 -u www-data -g www-data main:app)
    user=www-data
    autostart=true
    autorestart=true
    redirect_stderr=True

### Nginx
Create an Nginx config for the application:

    sudo vim /etc/nginx/sites-available/site

Add the config to talk to the Gunicorn process:

    upstream growl_app_server {
        server 127.0.0.1:4000;
    }

    server {
        listen 443;
        server_name example.com;
        ssl on;
        ssl_certificate /etc/nginx/conf/server.crt;
        ssl_certificate_key /etc/nginx/conf/server.key;

        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_pass http://growl_app_server;
            client_max_body_size 10m;
        }
    }

Link the config to `sites-enabled`:

    sudo ln -s /etc/nginx/sites-available/site /etc/nginx/sites-enabled/site

Test the config:

    sudo nginx -t

Reload Nginx:

    sudo /etc/init.d/nginx reload


## To Do
* Document the deployment with SSL support.
* The password is being sent in plain text right now. Use base64 to encode it and update this project to deal with it in that format.

