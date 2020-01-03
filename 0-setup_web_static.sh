#!/usr/bin/env bash
# script to configure in order to serve the static pages
sudo apt-get -y update
sudo apt-get -y install nginx
# enable pass of traffic in the port 80
sudo ufw allow 'Nginx HTTP'
name=$HOSTNAME
# configure the file nginx.conf in order the set the header
sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\t# Adding Header/" /etc/nginx/nginx.conf
sudo sed -i "s/# Adding Header/# Adding Header \n\tadd_header X-Served-By $name;/" /etc/nginx/nginx.conf
sudo service nginx restart
# instructions
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
cd /data/web_static/releases/test/
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    FAKE HTML\n  </body>\n</html>" > index.html
cd -
sudo ln -fs /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
cd /etc/nginx/sites-available/
sudo sed -i "s/404_page.html;/404_page.html;\n\n\t# static page/" default
sudo sed -i "s/# static page/# static page\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}/" default
cd -
sudo service nginx restart
