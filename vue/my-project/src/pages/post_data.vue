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
        <div v-if="show2">
            <button type="button" @click="predict_output_post()">予測結果を登録する</button>
        </div> 
      </div>
    </transition>

</div>
</template>

<script>
import axios from '../axios-for-predict.js';
import axios2 from '../axios-for-auth';

export default {  
  data() {
      return{
      datas:localStorage.getItem('datalist'),
      code:localStorage.getItem('code'),
      datas_parse:JSON.parse(localStorage.getItem('datalist')),
      resdata:"",
      show:false,
      show2:false,
      selected: 'どの値を予測したいですか?',
      loading: false,
      info: ''
    }
  },
  computed: {
    idToken() {
      return this.$store.getters.idToken;
    },
    login_name: function(){
      return this.info != null ? this.info :''
    }
  },
  created(){
      axios2.get('/api/myself/',{
          headers:{
              Authorization: `Token ${this.idToken}`
          }
      })
      .then((response) => {
          this.info = response.data.username
      })
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
          this.show2 = true;
        });
      }
    },

    token_log() {
      console.log(`${this.idToken}`)
        axios.get('/api/myself/',{
            headers: {
                Authorization: `Token ${this.idToken}`
            }
        })
        .then((response) => {
            console.log(response);       
            //document.write('<p>'+ response.data + '</p>');
            this.info = response.data.username
        });
    },
    predict_output_post(){
      //const date_now = Date.now();
        axios2.post(
            '/api/predict_reg/',
        { 
          'Content-Type': 'application/json',
          predict_date:this.resdata.date,
          name:this.datas_parse.name,
          value:this.resdata.predict_target,
          user:this.login_name,
          target:this.selected,
          //predict_date:'11-11',
          //name:'test',
          //value:'9999'
        },
        ).then((response) => {
          console.log(response);
          this.show2 = false;
          this.$swal({
          icon: 'success',
          text: '登録に成功しました'
          })
        });
    }


  }
};
</script>

<style>
.input-group {
  margin: 5px;
}
</style>