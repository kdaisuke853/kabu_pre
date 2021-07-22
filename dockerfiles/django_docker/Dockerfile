# Docker Hubにあるpythonイメージをベースにする
#FROM python:3.8-alpine
FROM continuumio/anaconda3:2019.03

# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
#RUN apt-get install gcc build-base
#RUN apk --update
#RUN apk add gcc build-base linux-headers
#RUN apt-get update
#RUN apt-get install -y build-essential cmake clang libssl-dev vim
#RUN addgroup -S uwsgi && adduser -S -G uwsgi uwsgi
#RUN apt-get install -y build-essential python
#RUN apt-get install python3.8-dev
#RUN conda install uwsg
#RUN apk add gcc build-base linux-headers
#RUN addgroup -S uwsgi && adduser -S -G uwsgi uwsgi
#RUN pip install Flask==0.10.1 uWSGI
RUN pip install -r requirements.txt
RUN conda install -c conda-forge fbprophet
#RUN mv -f hdays.py /opt/conda/lib/python3.7/site-packages/fbprophet
ADD . /code/
# ホストPCの各種ファイルをcodeディレクトリにコピーする
