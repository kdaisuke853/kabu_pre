# kabu_pre

## 制作背景
サービス概要は現在や1年間の株価を取得して、グラフ表示や株価予測ができるアプリケーションです。
昨今、機械学習学習が注目されているもののテストデータの用意やモデルへの適用など敷居が高いのが現状です。
その課題を解決するために、webから1クリックで簡単な時系列予測をできる簡易的なWebアプリの作成に取り掛かりました。
今はまだ、ProphetというFacebook製時系列予測OSSのみですが今後はより機械学習について学習して様々な手法な機械学習を実施できるようなアプリにしていきたいです。
また株価以外のデータにおいても予測できるようなアプリを目指しています。

## URL
URL:https://kabupresub.com/  
ユーザー登録をしてもらい、そのアカウントでログインできます  
![alt](https://github.com/kdaisuke853/kabu_pre/blob/master/image/%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E7%94%BB%E9%9D%A2.png)

## モデル図
![alt](https://github.com/kdaisuke853/kabu_pre/blob/master/image/graph-model.png)

## インフラ構成図  
![alt](https://github.com/kdaisuke853/kabu_pre/blob/master/image/test3.png)

## 使用技術  
### フロントエンド  
・Vue 2.6.11  
・Vue router  
・vuetify 2.5.8  
・buex 3.6.2  
・vue-chartjs 3.4.2  
・vue-apexcharts 1.6.1  
・bootstrap-vue　2.21.2  

### バックエンド  
・Python 3.7.3  
・Conda 4.10.3  
・Django 3.2.3  
・djangorestframework  
・uwsgi  
・fbprophet  

### クラウド(AWS)  
・ECR/ECS  
・Fargate  
・ALB  
・Route53  
・RDS(Mysql)  


### 開発環境等その他  
・Docker  
・Circleci  
・Nginx  

## 機能一覧
|  | 機能 |
----|---- 
| 1 | アカウント登録機能 |
| 2 | ログイン機能 |
| 3 | ログアウト機能 |
| 4 | タスク登録機能 |
| 5 | タスク削除機能 |
| 6 | タスク表示機能 |
| 7 | 最新の株価取得機能 |
| 8 | 最新の株価1年間取得機能(始値・終値・高値・低値) |
| 9 | 10日間の株価グラフ表示機能(始値・終値・高値・低値) |
| 10 | 1年間の株価グラフ表示機能(始値・終値・高値・低値) |
| 11 | 株価予測機能(始値・終値・高値・低値) |
| 12 | 株価コード検索機能|
| 13 | 株価コード表アップロード機能|

## 何ができるのか  
### ①株価コード検索  
  
https://user-images.githubusercontent.com/80162502/128960211-d8c62845-c448-4386-9b69-924e378b47e6.mov　　

### ②株価取得(現在価格・1年分)　　　
![demo](https://github.com/kdaisuke853/kabu_pre/blob/master/%E6%A0%AA%E4%BE%A1%E5%8F%96%E5%BE%97.gif)  

  
### ③株価グラフ表示機能  
![demo2](https://github.com/kdaisuke853/kabu_pre/blob/master/graph.gif)

### ④株価予測機能  
![demo3](https://github.com/kdaisuke853/kabu_pre/blob/master/predict.gif)
