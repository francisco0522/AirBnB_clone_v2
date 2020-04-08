#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo echo "Holberton School" > /var/www/html/index.html
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/current /data/web_static/releases/test/
sudo 