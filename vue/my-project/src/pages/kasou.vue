<template>
  <div class="container">
    <h2>仮想通貨取得ページです</h2>
    <button type="button" @click="token_log()">取得する</button>
    <!--<input type ="text" v-model="this.info">-->
    <h2>{{ test }}</h2>
  </div>
</template>

<script>

import axios from 'axios';
export default {
  data: function () {
  return {
    info: null
  }
},
  computed: {
    test: function(){
      return this.info != null ? this.info :'no value'
    }
  },
  methods: {
    token_log() {
        axios.get('https://api.coindesk.com/v1/bpi/currentprice.json',{
        })
        .then((response) => {
            console.log(response);       
            //document.write('<p>'+ response.data + '</p>');
            this.info = response.data
            document.getElementById('wrap').insertAdjacentHTML('beforeend',response);
        });
    },
  }
}
</script>

{{}}