# web_site by python frame
a simple blog by django(1.11), nginx, uwsgi, docker(docker-compose).

host:port

admin uri: host:port/admin


# start server
configuration:
common config: myweb/config/general.ini
nginx config: myweb/nginx/myweb.conf
docker config: Dockerfile, docker-compose.yml

under DE:
python manage.py runserver 0.0.0.0:port

under PE:
`$ docker-compose up`
into container, initialize db and configuration
`$ docker exec -it container_web_id /bin/bash`
`$ python manage migrate`
`$ python manage makemigration`
`$ python manage createsuperuser`
