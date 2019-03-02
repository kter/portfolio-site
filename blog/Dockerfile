FROM python:3.7.2-alpine3.9

RUN pip3 install jinja2 \
    feedparser \
    boto3

RUN mkdir /app
WORKDIR /app
COPY updater.py /app
COPY templates /app/templates

CMD [ "python3", "updater.py" ]