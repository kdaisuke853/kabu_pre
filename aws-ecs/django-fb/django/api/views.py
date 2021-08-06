from django.shortcuts import render
import os
import re
import json, ast
from django.http.response import HttpResponse
import pandas as pd
from fbprophet import Prophet

UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def loginfunc(request):
    context = {
        'message': '初めてのメッセージ',
        'content': 'ようこそ、Djangoは楽しい！',
    }
    return render(request, 'login.html', {'context': context})


# JsonResponse(data)



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
        """
        post_code = json_load['code']

        post_code = str(post_code)

        post_code2 = post_code.replace('"', '')

        print(post_code2)
        name = kabu_db.objects.filter(code=post_code2)
        name2 = list(name.values())
        print(name)
        print(name2[0]['name'])
        name_val = name2[0]['name']
        """

        # 辞書型の文字列を辞書型に変換
        dic = ast.literal_eval(json_target)

        # データセットから日付を取得。取得したい文字:2021-06-10。取得後、辞書のtimestampに代入 ⇨ 1年分の方に機能移行
        """
        for x in range(244):
            a = re.search(r'[0-9]*-[0-9][0-9]-[0-9][0-9]', dic['timestamp'][str(x)])
            dic['timestamp'][str(x)] = a.group(0)
        """
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
