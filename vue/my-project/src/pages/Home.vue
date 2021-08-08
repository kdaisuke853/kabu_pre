<template>
<div class="container">
  <h2 class="m-5">機能説明</h2>

  <b-card-group deck>
  <div>
    <b-card
      title="ログイン機能"
      img-src="https://img2.lancers.jp/menu/185096/2555350/081b42d9d906ab551e76a169b6dc936f8072e784e47a5e7bfe4649edc300d1fe/26379849_610_0.png"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        フロント側はVue-jsを使用(axiosでPOST)。バックエンド側はdjango-rest-frameworkで作成したAPI
      </b-card-text>
    </b-card>
  </div>

  <div>
    <b-card
      title="ユーザ登録機能"
      img-src="https://img2.lancers.jp/menu/185096/2555350/081b42d9d906ab551e76a169b6dc936f8072e784e47a5e7bfe4649edc300d1fe/26379849_610_0.png"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        フロント側はVue-jsを使用(axiosでPOST)。バックエンド側はdjango-rest-frameworkで作成したAPI
      </b-card-text>

    </b-card>
  </div>
  <div>
    <b-card
      title="タスク管理機能(サブメニュー)"
      img-src="https://img2.lancers.jp/menu/185096/2555350/081b42d9d906ab551e76a169b6dc936f8072e784e47a5e7bfe4649edc300d1fe/26379849_610_0.png"
      img-alt="Image"
      img-top
      tag="article"
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        フロント側はVue-jsを使用(axiosでPOST)。バックエンド側はdjango-rest-frameworkで作成したAPI
      </b-card-text>
    </b-card>
  </div>

  <div>
    <b-card
      title="株価取得機能(現在)"
      img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
      img-alt="Image"
      img-top
      tag="article"
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        フロント側にて株価コードをバックエンド側に送信。バックエンド側は受け取ったコードから該当の株価をスクレイピングで取得(beautifulsoupのライブラリを使用)
      </b-card-text>
    </b-card>
  </div>

  <div>
    <b-card
      title="株価取得機能(１年分)"
      img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
      img-alt="Image"
      img-top
      tag="article"
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-text>

        フロント側にて株価コードをバックエンド側に送信。バックエンド側は受け取ったコードから該当の株価をyahoofinaceAPIで取得。
        バックエンド側からフロント側にデータが返ってきた際にデータを保存。グラフ表示や株価予測の際にこのデータを使用する。
        <br>※最初はyahoo_finance_api2で実装していたが、7月中旬に動作しなくなったためyfinanceにライブラリを変更
      </b-card-text>
    </b-card>
  </div>

  <div>
    <b-card
      title="株価グラフ(10日間)"
      img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
      img-alt="Image"
      img-top
      tag="article"
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        取得した1年間の株価データから最新の10個のデータを取り出してグラフを作成。vue-chartjsのlinechartを使用。
        高値・安値・始値・終値を選択可能
      </b-card-text>
    </b-card>
  </div>

  <div>
    <b-card
      title="株価グラフ1年間(Candlechart)"
      img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
      img-alt="Image"
      img-top
      tag="article"
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        取得した1年間の株価データを全て使用してグラフを作成。Apexchartを使用(プログラムコードをPythonを使って記載)
      </b-card-text>
    </b-card>
  </div>

  <div>
    <b-card
      title="コード検索"
      img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
      img-alt="Image"
      img-top
      tag="article"
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        銘柄名からコードを検索する機能。検索文字を含む候補を全て出力。バックエンドではdjangoのdbにSELECT文を実行。
      </b-card-text>
    </b-card>
  </div>

  <div>
    <b-card
      title="株価予測"
      img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
      img-alt="Image"
      img-top
      tag="article"
      style="width: 20rem;"
      class="mb-2"
    >
      <b-card-text>
        取得した1年間の株価データを元に時系列予測ライブラリfbprophet(Facebook製時系列予測OSS)により予測を実施。
        予測結果から一番新しいものを1レコード取得し、フロント側に返す。予測対象を高値・安値・始値・終値から選択可能。
        <br><strong>※実際に機械学習ライブラリは使用していますが参考程度にしてください</strong>
      </b-card-text>
    </b-card>
  </div>


</b-card-group>
</div>
</template>

