FROM continuumio/anaconda3:2019.03

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
#追加
ADD hdays.py /code/
RUN pip install -r requirements.txt
RUN conda install -c conda-forge fbprophet
ADD django /code/

