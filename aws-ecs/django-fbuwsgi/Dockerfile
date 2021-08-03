FROM continuumio/anaconda3:2019.03

ENV PYTHONUNBUFFERED 1
RUN mkdir /code2
WORKDIR /code2
ADD ./aws-ecs/django-fbuwsgi/requirements.txt /code2/
ADD hdays.py /code2/
#COPY /django2 /code2/
RUN pip install -r requirements.txt
RUN conda install -c conda-forge uwsgi
RUN conda install -c conda-forge libiconv
RUN conda install -c conda-forge fbprophet
ADD django2 /code2/
RUN mv -f hdays.py /opt/conda/lib/python3.7/site-packages/fbprophet/
RUN chmod 755 docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["/code2/docker-entrypoint.sh"]
EXPOSE 8001



#ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
#WORKDIR /code
#ADD requirements.txt /code/
#追加
#ADD hdays.py /code/
#RUN pip install -r requirements.txt
#RUN conda install -c conda-forge fbprophet
#ADD django /code/


