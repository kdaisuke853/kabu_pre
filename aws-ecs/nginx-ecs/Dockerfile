FROM nginx:1.13

# 設定ファイルをコピーする
#COPY ./nginx/conf /etc/nginx/conf.d
#COPY ./nginx/uwsgi_params /etc/nginx/uwsgi_params

ADD ./aws-ecs/nginx-ecs/nginx/uwsgi_params /etc/nginx/uwsgi_params
ADD ./aws-ecs/nginx-ecs/nginx/conf /etc/nginx/conf.d
CMD ["nginx", "-g", "daemon off;"]