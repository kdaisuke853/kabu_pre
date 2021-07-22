<template>

<div class="container">
  <div v-if="content">
    <h2>株価(1年分)を取得したい銘柄コードを入力してください</h2>
  
  <!--モーダル前
  <div v-if="!show"> 
    <form class="login-form">
    <div class="input-group">
      <button type="button"  @click="post_code()">送信</button>
    </div>

        <label for="code_input2">株価コード:</label>
        <input type="text" id="code_input" v-model="code_input">
        <button type="button"  @click="post_code(),code_set()">送信</button>

    </form>
  </div>
  -->

  <b-form-group id="input-name" label="Code:" label-for="input-name">
    <b-form-input
        id="code_input"
        v-model="code_input"
        placeholder="Enter code"
        required
    ></b-form-input>

  
      <b-button v-b-modal.modal-1 @click="post_code(),$bvModal.show('value_code')" class="m-5">株価取得</b-button>
  </b-form-group>

      <b-modal id="value_code" hide-footer>
          <template #modal-title>
            １年分の株価取得結果
          </template>
          
          <div v-if="show">
            <ul>
              {{value.name}}の株価データ１年分の取得に成功しました。データ予測が可能です。
              <li v-for="(item,index) in value.timestamp" v-bind:key="index" class="task_list">
              値段:{{value.open[index]}}値:{{index}}
              </li>  
            </ul>
          </div>

          <div v-if="!show">
            株価取得に失敗しました。
          </div>

          </b-modal>

    </div>

    <div v-if="!content">
      <h3>現在、{{value.name}}の1年分の株価データを取得ずみです。</h3>
      <b-button v-b-modal.modal-1 @click="datareset()" class="m-5">リセット</b-button>

    </div>

  </div>
</template>

<script>
import axios from '../axios-for-auth.js';
export default {
  data() {
    return {
      code_input: "",
      value: [],
      show :false,
      content :true,
    }
  },
  computed: {
    idToken() {
      //tokenを返す
      return this.$store.getters.idToken;
    },
    value_code: function(){
      return this.value != null ? this.value :''
    },
  },

  methods: {
    post_code() {
      if ( this.code_input.match(/^[0-9]{4}$/) )
      {
      axios.get(
        '/api/outputs',{
        params: {
          
          code_input: this.code_input,
          //returnSecureToken: true
        }
    }).then((response) => {
        console.log(response.data);
        //console.log(response.data.open[0])
        //document.getElementById('wrap').insertAdjacentHTML('beforeend','時間:' + response.data.timestamp[1] + '<br>' + 'open:' + response.data.open['1']);
        //'timestamp': str(df['timestamp']), 'open': df['open'], 'high': df['high'], 'low': df['low'],
        //'close': df['close'], 'volume': df['volume']
        this.value = response.data
        localStorage.setItem('datalist',JSON.stringify(response.data));
        localStorage.setItem('code',JSON.stringify(this.code_input));

        //this.$router.push('/post_data');
        this.show = !this.show
        this.content = false

      }).catch(error => alert(error + '\nErrormessage:このコードは存在しません'));
      //this.code_input = ""
      }
      else
      alert('株価コードを入力してください(数字4桁)')
    },

    datareset(){
      localStorage.clear();
      this.content = true
    }
  }
}
</script>

<style>
.input-group {
  margin: 5px;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>