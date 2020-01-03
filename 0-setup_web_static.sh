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
# instructions
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
cd /etc/nginx/sites-available/
sudo sed -i "s/404_page.html;/404_page.html;\n\n\t# static page/" default
sudo sed -i "s/# static page/# static page\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex on;\n\t}\n/" default
cd -
sudo service nginx restart
exit 0
