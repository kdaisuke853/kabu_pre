FROM node:lts-alpine

# http サーバをインストールする
RUN npm install -g http-server

# カレントワーキングディレクトリ
WORKDIR /app

# package.jsonとpackage-lock.json両方コピー
COPY ./vue/my-project/package*.json ./

# ライブラリをインストールする
RUN npm install

# カレントワーキングディレクトリにプロジェクトのファイルやフォルダをコピーする
COPY ./vue/my-project/. .

# 本番向けにアプリケーションをビルド
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]




