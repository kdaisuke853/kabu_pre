<template>

    <div class="container">
      <h1>最近10日間のグラフ</h1>
      <select v-model="selected">
        <!--
            <option value="表示したいグラフを選んでください">Please Select</option>
            <option value="Open">始値(Open)</option>
            <option value="Low">安値(Low)</option>
            <option value="High">高値(High)</option>
            <option value="Close">終値(Close)</option>
          -->
            <option>Open</option>
            <option>Low</option>
            <option>High</option>
            <option>Close</option>

      </select>

      <div id="app">

        <p v-if="selected == '表示したいグラフを選んでください'">
        </p>

        <p v-else-if="selected == 'Open'">
          <line-chart
            :data="chartData_Open"
            :options="options"
            :height="100"
        ></line-chart></p>

        <p v-else-if="selected == 'Low'">
          <line-chart
            :data="chartData_Low"
            :options="options"
            :height="100"
        ></line-chart></p>

        <p v-else-if="selected == 'High'">
          <line-chart
            :data="chartData_High"
            :options="options"
            :height="100"
        ></line-chart></p>

        <p v-else-if="selected == 'Close'">
          <line-chart
            :data="chartData_Close"
            :options="options"
            :height="100"
        ></line-chart></p>

      {{selected}}
      </div>
    </div>
</template>

<script>
import LineChart from "../timechart.vue";
export default {
  name: "ChartLineSample",
  components: {
    LineChart
  },
  data: 
  function() {
    
    var datas2 = JSON.parse(localStorage.getItem('datalist'));
    //var code_name = localStorage.getItem('code');
    return {
      selected: "表示したいグラフを選んでください",
      datas:JSON.parse(localStorage.getItem('datalist')),


      chartData_Open: {
        //x軸
        labels: [datas2.Date[234],datas2.Date[235], datas2.Date[236], datas2.Date[237],datas2.Date[238], datas2.Date[239], datas2.Date[240],datas2.Date[241], datas2.Date[242], datas2.Date[243]],
        // データ詳細
        datasets: [
          {
          //グラフタイトル
            label: datas2.name,
            //データ値(y軸)
            data: [datas2.Open[234],datas2.Open[235], datas2.Open[236], datas2.Open[237],datas2.Open[238], datas2.Open[239], datas2.Open[240],datas2.Open[241], datas2.Open[242], datas2.Open[243]],
            backgroundColor: "#6090EF",
          }
        ]
      },
      chartData_Close: {
        //x軸
        labels: [datas2.Date[234],datas2.Date[235], datas2.Date[236], datas2.Date[237],datas2.Date[238], datas2.Date[239], datas2.Date[240],datas2.Date[241], datas2.Date[242], datas2.Date[243]],
        // データ詳細
        datasets: [
          {
          //グラフタイトル
            label: datas2.name,
            //データ値(y軸)
            data: [datas2.Close[234],datas2.Close[235], datas2.Close[236], datas2.Close[237],datas2.Close[238], datas2.Close[239], datas2.Close[240],datas2.Close[241], datas2.Close[242], datas2.Close[243]],
            backgroundColor:"#98fb98",
          }
        ]
      },
      chartData_Low: {
        //x軸
        labels: [datas2.Date[234],datas2.Date[235], datas2.Date[236], datas2.Date[237],datas2.Date[238], datas2.Date[239], datas2.Date[240],datas2.Date[241], datas2.Date[242], datas2.Date[243]],
        // データ詳細
        datasets: [
          {
          //グラフタイトル
            label: datas2.name,
            //データ値(y軸)
            data: [datas2.Low[234],datas2.Low[235], datas2.Low[236], datas2.Low[237],datas2.Low[238], datas2.Low[239], datas2.Low[240],datas2.Low[241], datas2.Low[242], datas2.Low[243]],
          }
        ]
      },
      chartData_High: {
        //x軸
        labels: [datas2.Date[234],datas2.Date[235], datas2.Date[236], datas2.Date[237],datas2.Date[238], datas2.Date[239], datas2.Date[240],datas2.Date[241], datas2.Date[242], datas2.Date[243]],
        // データ詳細
        datasets: [
          {
          //グラフタイトル
            label: datas2.name,
            //データ値(y軸)
            data: [datas2.High[234],datas2.High[235], datas2.High[236], datas2.High[237],datas2.High[238], datas2.High[239], datas2.High[240],datas2.High[241], datas2.High[242], datas2.High[243]],
          }
        ]
      },
      options: {responsive: true
                      , maintainAspectRatio: true
                      },
      addFlag: false,
    };
  },
};
</script>

<style>
.input-group {
  margin: 5px;
}
</style>