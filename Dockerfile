FROM python:3.7-alpine

RUN adduser -D mlhelper

WORKDIR /home/mlhelper

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt \
RUN venv/bin/pip install gunicorn \

COPY app app
COPY migrations migrations
COPY mlhelper.py config.py ./
RUN chmod a+x boot.sh

ENV FLASK_APP mlhelper.py

RUN chown -R mlhelper:mlhelper ./
USER mlhelper

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]