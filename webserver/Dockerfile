FROM python:3.8

WORKDIR /app

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
# RUN apt-get update

ADD . /app

EXPOSE 5000

CMD ["flask", "run"]