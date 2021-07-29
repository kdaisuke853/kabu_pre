FROM nginx:1.13

# 設定ファイルをコピーする
#COPY ./nginx/conf /etc/nginx/conf.d
#COPY ./nginx/uwsgi_params /etc/nginx/uwsgi_params

ADD ./nginx/uwsgi_params /etc/nginx/uwsgi_params
ADD ./nginx/conf /etc/nginx/conf.d
CMD ["nginx", "-g", "daemon off;"]