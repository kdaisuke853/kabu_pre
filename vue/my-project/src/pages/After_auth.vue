<template>
  <div class="container">
    <h2>ようこそ</h2>
    <h2>{{ login_name }}さん</h2>

    <button type="button" @click="token_log()">確認する</button>
    <!--<input type ="text" v-model="this.info">-->

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
