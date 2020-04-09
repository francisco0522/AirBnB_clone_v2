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
echo "PASO 5"
mkdir -p /data/web_static/
echo "PASO 6"
mkdir -p /data/web_static/releases/
echo "PASO 7"
mkdir -p /data/web_static/shared/
echo "PASO 8"
mkdir -p /data/web_static/releases/test/
echo "PASO 9"
echo "Holberton School" > /data/web_static/releases/test/index.html
echo "PASO 10"
ln -sfn /data/web_static/releases/test/ /data/web_static/current
echo "PASO 11"
chown -R ubuntu: /data/
echo "PASO 12"
sed -i '/listen 80 default_server;/a rewrite ^/hbnb_static /data/web_static/current/ permanent;' /etc/nginx/sites-available/default
echo "PASO 13"
service nginx start