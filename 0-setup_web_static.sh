#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

echo "PASO 1"
apt-get update
echo "PASO 2"
apt-get -y install nginx
echo "PASO 3"
ufw allow 'Nginx HTTP'
echo "PASO 4"
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu: /data/
sed -i '/listen 80 default_server;/a rewrite ^/hbnb_static /data/web_static/current/ permanent;' /etc/nginx/sites-available/default
service nginx start