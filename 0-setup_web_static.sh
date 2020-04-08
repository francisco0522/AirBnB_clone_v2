#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu: /data/
sed -i '/listen 80 default_server;/a rewrite ^/hbnb_static /data/web_static/current/ permanent;' /etc/nginx/sites-available/default
sudo service nginx start