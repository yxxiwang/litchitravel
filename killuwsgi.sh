 ps -ef | grep wsgi | awk '{print $2}' |xargs kill -9
sleep 2
uwsgi /root/litchitravel/uwsgi.ini
ps -ef | grep wsgi
