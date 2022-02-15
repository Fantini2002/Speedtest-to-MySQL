# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY script.py script.py
ENV DB_HOST=host
ENV DB_PORT=port
ENV DB_USER=user
ENV DB_PASSWD=pwd
ENV DB_DATABASE=db
ENV TIME=1800
CMD [ "python3", "-u", "script.py"]