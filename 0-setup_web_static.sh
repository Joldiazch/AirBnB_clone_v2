#!/usr/bin/env bash
# task 0
sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

sed -i "s/root \/var\/www\/html;/root \/data\/web_static\/current\/;/g" /etc/nginx/sites-enabled/default
sed -i "/root \/data\/web_static\/current\/;/a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo service nginx restart
