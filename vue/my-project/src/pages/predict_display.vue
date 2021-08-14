<template>
<div class="container">
  <h3>予測掲示板</h3>
  <b-button v-b-modal.modal-1 @click="displayed()" class="m-5">表示
  </b-button>

  <table align="center" border="1">
      <tr>
            <th>予測日</th>
            <th>対象銘柄</th>
            <th>予測結果</th>
            <th>予測したユーザ</th>
            <th>予測対象</th>
            <th>予測実行日</th>
      </tr>
      <tr v-for="item in data_display" v-bind:key="item.Name">
        <td>{{item.predict_date}}</td>
        <td>{{item.Name}}</td>
        <td>{{item.Value}}</td>
        <td>{{item.User}}</td>
        <td>{{item.target}}</td>
        <td>{{item.predict_play_date}}</td>
      </tr>
  </table>

</div>
</template>


<script>

import axios from '../axios-for-auth.js';

export default {
  data() {
    return {
      name_input: "",
      value: "",
      data_display:"",
      show :false
    }
  },
computed: {
    idToken() {
      //tokenを返す
      return this.$store.getters.idToken;
    },
  },
  methods: {
      displayed() {
      axios.get('/api/predict_display/',{
          headers:{
              Authorization: `Token ${this.idToken}`
          }
      })
      .then((response) => {
          console.log(response.data)
          //this.data_display = Json.parse(response.data)
          console.log(this.data_display)
          this.data_display = response.data
      }).catch(error => alert(error + '\nErrormessage'));
  },
  }
}
</script>

<style>
</style>