<template>
  <div class="container">
    <h2>ようこそ</h2>
    <h2>{{ login_name }}さん</h2>
    <!--<input type ="text" v-model="this.info">-->
      <h2 class="m-5">株プレ(利用者メニュー)</h2>
    <h1>メニューを選んでください</h1>
    <h2>coffee : <router-link to="/value_get"><font-awesome-icon icon="coffee" to="/value_get" /></router-link></h2>
    <h2>github : <font-awesome-icon :icon="['fab', 'github']" /></h2>
    <h2>linkedin : <font-awesome-icon :icon="['fab', 'linkedin']" /></h2>
    <h2>グラフ(10日間) : <router-link to="/graph_test"><font-awesome-icon :icon="['fas', 'chart-bar']" /></router-link></h2>
    <h2>キャンドルチャート(1年) : <router-link to="/candle"><font-awesome-icon :icon="['fas', 'chart-bar']" /></router-link></h2>
  </div>
</template>

<script>

import axios from '../axios-for-auth.js';
export default {
  data: function () {
  return {
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
      axios.get('/api/myself/',{
          headers:{
              Authorization: `Token ${this.idToken}`
          }
      })
      .then((response) => {
          this.info = response.data.username
      })
  },
  methods: {
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
  }
}
</script>
