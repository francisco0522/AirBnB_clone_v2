#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu: /data/
sed -i 'root /usr/share/nginx/html;/a location /hbnb_static/ {\n alias /data/web_static/current/;\n};' /etc/nginx/sites-available/default
service nginx restart