#!/usr/bin/env bash
# script to configure in order to serve the static pages
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "s/root \/var\/www\/html;/root \/var\/www\/html;\n\tlocation \/hbnb_static\/ { alias \/data\/web_static\/current/;}\n" /etc/nginx/sites-available/default
service nginx restart
exit 0
