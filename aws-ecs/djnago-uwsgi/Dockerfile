FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code2
WORKDIR /code2
ADD requirements.txt /code2/
RUN pip install -r requirements.txt
COPY /django2 /code2/
RUN chmod 755 docker-entrypoint.sh
EXPOSE 8001
ENTRYPOINT ["/code2/docker-entrypoint.sh"]




#FROM python:3.7
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /code2
#WORKDIR /code2
#ADD requirements.txt /code2/
#RUN pip install -r requirements.txt
#COPY . /code2/

