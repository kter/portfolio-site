FROM python:3.6.8-jessie

RUN mkdir /app
WORKDIR /app

RUN apt update && \
  apt install -y curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  pip install awscli
  
RUN curl -OL https://github.com/sass/dart-sass/releases/download/1.17.2/dart-sass-1.17.2-linux-x64.tar.gz && \
    tar xf dart-sass-1.17.2-linux-x64.tar.gz 

CMD ["/bin/sh",  "/app/bootstrap.sh"]