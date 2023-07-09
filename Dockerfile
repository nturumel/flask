FROM python:3.11.0

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install flask
RUN pip3 install gevent

COPY . .
EXPOSE 5000

CMD ["flask", "run"]
