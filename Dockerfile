FROM python:latest

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    echo "deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib" >/etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ jessie main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    build-essential \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    python-lxml \
    libssl-dev \
    zlib1g-dev \
    libffi-dev \
    python3-dev \
    libmysqlclient-dev

RUN pip install cryptography mysqlclient scrapy

VOLUME /app

WORKDIR /app

EXPOSE 5000
