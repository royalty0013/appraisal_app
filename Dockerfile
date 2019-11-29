FROM python:3.6-slim-stretch

MAINTAINER Hassan Braimah <hassan.braimah@abujaelectricity.com>

RUN apt-get update && apt install -y software-properties-common python3-setuptools

# Prepare for pillow instalation
RUN apt-get install -y libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
    libharfbuzz-dev libfribidi-dev

RUN apt-get install -y python3-dev default-libmysqlclient-dev libsasl2-dev libldap2-dev libssl-dev

RUN pip install django==1.11.0 mysqlclient python-ldap gunicorn pillow

ADD . /srv

# Force django to server static files
RUN pip install whitenoise

WORKDIR /srv

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "goal_setting.wsgi", "--access-logfile", "-", "--error-logfile", "-"]
