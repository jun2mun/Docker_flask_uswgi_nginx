FROM python:3.5

ADD . /www
WORKDIR /www

RUN python -m pip install --upgrade pip 
RUN pip3 install Flask
RUN pip3 install bs4
RUN pip3 install requests
RUN pip3 install uwsgi

CMD uwsgi uwsgi.ini
