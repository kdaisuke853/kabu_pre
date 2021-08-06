<template>
<div class="container">
  <h2>未来の株価予測</h2>

  <div v-if="!show"> 
    <form class="post-form">
       <label for="user">{{datas_parse.name}}の株価を1年分のデータを元に予測します。</label>
       <br>
       <!--<select name="target">
       <option value="open">始値</option>
       <option value="low">安値</option>
       <option value="high">高値</option>
       <option value="close">終値</option>
       </select>-->
      <label for="select">予測対象:</label>
        <select v-model="selected">
          <option disabled value="どの値を予測したいですか?" >Please Select</option>
            <option value="Open">始値(open)</option>
            <option value="Low">安値(low)</option>
            <option value="High">高値(high)</option>
            <option value="Close">終値(close)</option>
        </select>

       <button type="button" @click="data_post()">実行</button>
     </form>
    </div>

 
      <!--<button type="button" @click="datareset(), show = !show">リセット</button>-->
    <b-spinner variant="primary" label="Spinning" v-show="loading">Loding now ...</b-spinner>
    <transition name = "fade"> 
      <div v-if="show">
        <h2>{{selected}}の予測が完了しました。</h2>
        <h3>銘柄名:{{datas_parse.name}} <br> 予測対象日時:{{resdata.date}} 値段:{{resdata.predict_target}}円</h3>
      </div>
    </transition>

</div>
</template>

<script>
import axios from '../axios-for-predict.js';

export default {  
  data() {
      return{
      datas:localStorage.getItem('datalist'),
      code:localStorage.getItem('code'),
      datas_parse:JSON.parse(localStorage.getItem('datalist')),
      resdata:"",
      show:false,
      selected: 'どの値を予測したいですか?',
      loading: false
    }
  },
  methods: {
    data_post() {
      if (this.selected.match("どの値を予測したいですか?")){
        alert("予測対象を選んでください")
        this.show = false
      }
      else{
        this.loading = true;
        axios.post(
            '/api/reserve_data/',
        {
            'Content-Type': 'application/json',
            datalist:this.datas,
            code:this.code,
            target:this.selected,
        }
        ).then((response) => {
          console.log(response);
          this.resdata = response.data
          localStorage.clear();
          this.loading = false;
          this.show = true;
        });
      }
    }
  }
};
</script>

<style>
.input-group {
  margin: 5px;
}
</style>