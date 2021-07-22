from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .ownpermissons import ProfilePermission
from bs4 import BeautifulSoup
from .models import kabu_db
import os
import requests
import re
import csv, json
from django.http.response import JsonResponse, HttpResponse
#from yahoo_finance_api2 import share
#from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import yfinance as yf
from rest_framework.permissions import AllowAny
from django.db import connection


UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


# ユーザーが見れる
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProfilePermission,)  # permissonは制限、allowanyは誰でも

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)  # 承認済みの人

    def get_object(self):
        return self.request.user


# 認証していればタスクが見れる
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


def loginfunc(request):
    context = {
        'message': '初めてのメッセージ',
        'content': 'ようこそ、Djangoは楽しい！',
    }
    return render(request, 'login.html', {'context': context})


def search_value(request):
    if request.method == "GET":
        # target = request.POST['code_input']
        target = request.GET['code_input']
        print(target)
        target_url = 'https://www.nikkei.com/nkd/company/?scode={}'.format(target)
        r = requests.get(target_url)
        soup = BeautifulSoup(r.text, 'lxml')

        val = soup.find('dd', attrs={'class': 'm-stockPriceElm_value now'})
        val2 = str(val)

        time_now_bf = soup.find('dt', attrs={'class': 'm-stockPriceElm_title'})
        time_now_af = str(time_now_bf)

        a = re.search(r'[0-9]*(,|[0-9])[0-9]*', val2)
        t = re.search(r'([0-9]*:[0-9]*)', time_now_af)

        if re.search(r'[0-9]*(,|[0-9])[0-9]*', val2):
            target_val = a.group(0)
            time_now = t.group(0)
            name = kabu_db.objects.filter(code=target)
            name2 = list(name.values())
            # print(name)
            print(name2[0]['name'])
            name_val = name2[0]['name']
            data = {
                'name': name_val,
                'val': target_val,
                'time': time_now
            }
            json_ret = json.dumps(data, ensure_ascii=False)  # unicodeレスポンス阻止のためensure_ascii追加
            return HttpResponse(json_ret)

        else:
            name_val = '銘柄がありません,コードを正しく入力してください'
            target_val = '銘柄がありません,コードを正しく入力してください'
            time_now = ''
            return HttpResponse('形式が違います')
        # print(type(name))
        # print(type(name2))
        # return render(request, 'output.html', {'target_val': target_val, 'time_now': time_now})
        # ret = {"data": "val" + target_val + "time" + time_now}


# JsonResponse(data)


def input_func(request):
    if request.method == "POST":
        code_input = request.POST['code_input']

    return render(request, 'input.html')
#fbprohet部分
"""
def reserve_data(request):
    if request.method == "POST":
        # 受けとったデータを読み込む
        json_str = request.body.decode("utf-8")
        json_data = json.loads(json_str)
        # print(json_data)

        # 受け取ったデータを一旦jsonファイルに保存
        with open('test2.json', 'w') as f:
            json.dump(json_data, f, indent=4)
            json_open = open('test2.json', 'r')
        # jsonから値を読み出す
        json_load = json.load(json_open)

        user_target = json_load['target']
        # 1年分の株価データ
        json_target = json_load['datalist']

        # ポストされたコードからdjangoDBを検索して銘柄名を取得 ⇨ 1年分の方に機能移行
        post_code = json_load['code']

        post_code = str(post_code)

        post_code2 = post_code.replace('"', '')

        print(post_code2)
        name = kabu_db.objects.filter(code=post_code2)
        name2 = list(name.values())
        print(name)
        print(name2[0]['name'])
        name_val = name2[0]['name']


        # 辞書型の文字列を辞書型に変換
        dic = ast.literal_eval(json_target)

        # データセットから日付を取得。取得したい文字:2021-06-10。取得後、辞書のtimestampに代入 ⇨ 1年分の方に機能移行
        # 辞書型をデータフレームに
        df = pd.DataFrame.from_dict(dic)

        # print(df)
        # prophetで使用できるようにtimestampをds,対象カラムをyに変更。予想するターゲットはユーザーが指定したもの。(high,low,open,closeのどれか)

        df = df.rename(columns={user_target: 'y'})
        df = df.rename(columns={'Date': 'ds'})
        # print(df)

        # 時系列解析の機械学習ライブラリ(prophet)で学習。
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=200, freq='H')
        forecast = model.predict(future)
        # 予測の最後の行を取得
        ret_predict = forecast.tail(1)
        # 文字列に変換
        predict_date = str(ret_predict['ds'])
        predict_val = str(ret_predict['yhat'])

        # 予測した日付を取得
        re_predictdate = re.search(r'[0-9]*-[0-9][0-9]-[0-9][0-9]', predict_date)
        predict_date = re_predictdate.group(0)

        # 予測した値を取得

        re_predict_val = re.search(r'\s+[0-9]*', predict_val)
        predict_val_before = re_predict_val.group(0)
        # 余分な空白削除。
        predict_val = predict_val_before.replace(' ', '')

        ret_dict = {
            'date': predict_date,
            'predict_target': predict_val,
        }
        json_ret = json.dumps(ret_dict, ensure_ascii=False)
        os.remove('test2.json')

        return HttpResponse(json_ret)

    else:
        return HttpResponse('データがありません')
"""

def search_values_1year(request):
    if request.method == "GET":
        target = request.GET['code_input']

        #now = datetime.datetime.now()
        #now = now.strftime("%y%m%d")
        company_code = str(target) + '.T'
        target_name = yf.Ticker(company_code)
        target_data = target_name.history(period="1y")
        target_data.to_csv('test.csv')
        df = pd.read_csv('test.csv')
        os.remove('test.csv')

        ret_dict = df.to_dict()
        #ret_json = target_data.to_json()
        name = kabu_db.objects.filter(code=target)
        name2 = list(name.values())
        name_val = name2[0]['name']
        ret_dict['name'] = name_val

        return JsonResponse(ret_dict)

    def search_name_to_code(request):
        if request.method == "GET":
            target = request.GET['code_input']
        



    """
    if request.method == "GET":
        target = request.GET['code_input']

        now = datetime.datetime.now()
        now = now.strftime("%y%m%d")
        company_code = str(target) + '.T'
        my_share = share.Share(company_code)
        try:

            # 1日毎の1年分のデータを取得する場合
            symbol_data = my_share.get_historical(share.PERIOD_TYPE_YEAR,
                                                  1,
                                                  share.FREQUENCY_TYPE_DAY,
                                                  1)
            df = pd.DataFrame(symbol_data.values(), index=symbol_data.keys()).T
            df.timestamp = pd.to_datetime(df.timestamp, unit='ms')
            # df_time = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}', df['timestamp'])
            # df['timestamp'] = df_time.group(0)
            # df['timestamp'] = pd.DatetimeIndex(df.timestamp, name='timestamp').tz_localize('UTC').tz_convert('Asia/Tokyo')
       
            dict2 = {'timestamp': str(df['timestamp']), 'open': df['open'], 'high': df['high'], 'low': df['low'],
                     'close': df['close'], 'volume': df['volume']}
 
            # 日本標準時間に変換
            # df.index = pd.DatetimeIndex(df.timestamp, name='timestamp').tz_localize('UTC').tz_convert('Asia/Tokyo')
            # csvファイルに保存
            # df.to_csv(now + "_" + str(target) + "_" + ".csv", index=False)
            # jsonに変更
            # ret_json = df.to_json()
            ret_dict = df.to_dict()
            # print(ret_dict)
            # print(ret_dict['timestamp'][0])
            print(len(df))
            for x in range(len(df)):
                a = re.search(r'[0-9]*-[0-9][0-9]-[0-9][0-9]', str(ret_dict['timestamp'][x]))
                ret_dict['timestamp'][str(x)] = a.group(0)

            name = kabu_db.objects.filter(code=target)
            name2 = list(name.values())
            # print(name)
            # print(name2[0]['name'])
            name_val = name2[0]['name']
            ret_dict['name'] = name_val

        except YahooFinanceError as e:
            print(e.message)
            pass
        return JsonResponse(ret_dict)
    """

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            path = os.path.join(UPLOAD_DIR, f.name)
            with open(path, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            with open(path, 'r') as destination:
                # read csv
                rdr = csv.reader(destination)
                # ignore header
                next(rdr)
                # upsert
                for r in rdr:
                    ev = kabu_db()
                    ev.code = r[1]
                    ev.name = r[2]
                    ev.save()
            return HttpResponseRedirect('SUCCES')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})

def name_to_code(request):
    if request.method == "GET":
        target_k = request.GET['name_input']
        print(target_k)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM api_kabu_db WHERE Name like %s", ('%'+target_k+'%',))
            weather_datas = cursor.fetchall()
            res_list = []
            for weather_data in weather_datas:
                res = {'Name': weather_data[2],
                       'Code': weather_data[1],
                       }

                res_list.append(res)

            json_rets = json.dumps(res_list, ensure_ascii=False)
            return HttpResponse(json_rets)
