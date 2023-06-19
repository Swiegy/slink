FROM python:3.11

ADD ./ /app
WORKDIR /app

RUN apt-get update && apt-get install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && python /tmp/get-pip.py

RUN make install

EXPOSE 8000

CMD ["sh", "docker-entrypoint.sh"]
