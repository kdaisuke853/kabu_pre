FROM node:lts-alpine

RUN mkdir -p /code

# node.js の環境変数を定義する
# 本番環境では production
ENV NODE_ENV=production

# `package.json` と `package-lock.json` （あれば）を両方コピーする
COPY package*.json ./

# プロジェクトの依存ライブラリをインストールする
RUN npm install

# ディレクトリを移動する
WORKDIR /code

RUN cd my-project
# ポート8080番を開放する
EXPOSE 8080


