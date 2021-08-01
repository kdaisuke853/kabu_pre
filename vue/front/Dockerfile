FROM node:lts-alpine

RUN mkdir /code
# node.js の環境変数を定義する
# 本番環境では production
ENV NODE_ENV=production
WORKDIR /code
COPY /my-project/ /code/
# プロジェクトの依存ライブラリをインストールする
RUN npm uninstall -g vue-cli
RUN rm -rf node_modules package-lock.json && npm install
#RUN npm install
# ポート8080番を開放する
EXPOSE 8080
CMD ["npm", "run", "serve"]





