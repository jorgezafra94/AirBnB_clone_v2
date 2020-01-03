#!/usr/bin/env bash                                                                                                                                                                                                
sudo apt-get -y update
sudo apt-get -y install nginx
# enable pass of traffic in the port 80                                                                                                                                                                            
sudo ufw allow 'Nginx HTTP'
# instructions                                                                                                                                                                                                     
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
cd /data/web_static/releases/test/
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    FAKE HTML\n  </body>\n</html>" > index.html
cd -
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
cd /etc/nginx/sites-available/
sudo sed -i "s/404_page.html;/404_page.html;\n\t# static page/" default
sudo sed -i "s/# static page/# static page\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/index.html;\n\t}/" default
cd -
sudo service nginx restart
