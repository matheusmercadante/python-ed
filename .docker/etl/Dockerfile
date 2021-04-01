# FROM python:rc-alpine3.13

# WORKDIR /usr/src/etl/app

# COPY . .

# ENV DOCKERIZE_VERSION v0.6.1
# RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#     && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#     && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# ENTRYPOINT [ "python3" ]
# CMD [ "main.py" ]

# ADD ./.docker/etl/entrypoint.sh /entrypoint.sh

# RUN chmod +x /entrypoint.sh

FROM python:3.8

WORKDIR /usr/src/etl/app

ADD ./ ./

RUN pip install pandas PyMySQL

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

CMD [ "python", "./main.py" ]