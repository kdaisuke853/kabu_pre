FROM continuumio/anaconda3:2019.03

# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN conda install -c conda-forge fbprophet
RUN conda install -c -y conda-forge uwsgi
RUN conda install -c -y conda-forge libiconv
COPY /django /code/
RUN mv -f hdays.py /opt/conda/lib/python3.7/site-packages/fbprophet

RUN chmod 755 docker-entrypoint.sh
ENTRYPOINT ["/code/docker-entrypoint.sh"]
