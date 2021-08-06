<template>
<div class="container">
  <h3>株価を取得したい銘柄コードを入力してください</h3>

  <b-form-group id="input-name" label="Code:" label-for="input-name">
    <b-form-input
        id="code_input"
        v-model="code_input"
        placeholder="Enter code"
        required
    >

    </b-form-input>

    <b-button v-b-modal.modal-1 @click="post_code(),$bvModal.show('value_code'), show =!show " class="m-5">株価取得</b-button>
  </b-form-group>
    
    <b-modal id="value_code" hide-footer>
      <template #modal-title>
        株価取得結果
      </template>

      <div v-if="show">
        銘柄名:{{value_code.name}} 現在価格:{{value_code.val}}円({{value_code.time}})
      </div>


      <div v-if="!show">
        株価取得に失敗しました。コードが存在しない可能性があります
      </div>
    
    </b-modal>
</div>
</template>


<script>

import axios from '../axios-for-auth.js';

export default {
  data() {
    return {
      code_input: "",
      value: "",
      show :false
    }
  },
  computed: {
    idToken() {
      //tokenを返す
      return this.$store.getters.idToken;
    },
    value_code: function(){
      //タスクゲットボタンを押す前と押したあとの変数表示部分
      return this.value != null ? this.value :'確認ボタンを押してください'
    },

  },
  methods: {
    post_code() {
      if ( this.code_input.match(/^[0-9]{4}$/) ){
      axios.get(
        '/api/output',{
        params: {
          code_input: this.code_input,
          //returnSecureToken: true
        }
    }).then((response) => {
        console.log(response);
        //document.getElementById('wrap').insertAdjacentHTML('beforeend','株価:' + response.data.val + '時間:' + response.data.time);
        this.value = response.data
        //this.show = !this.show
        console.log(response.data)

        if (response.data === "形式が違います"){
          this.show = false
        }
        
      }).catch(error => this.$swal({
        icon: 'error',
        text: error +'\n株価コードを入力してください(数字4桁)'
          }));

      this.show = false
      this.code_input = ""

    }
  else

    this.$swal({
        icon: 'error',
        text: '株価コードを入力してください(数字4桁)'
        })
      this.show = false
    },

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