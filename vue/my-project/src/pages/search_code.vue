<template>
<div class="container">
  <h3>コード検索</h3>
  <form class="search-form">
    <div class="input-group">
        <label for="name">検索ワード(曖昧検索)</label>
        <input type="text" id="name_input" v-model="name_input">
        <button type="button" @click="post_name()">検索</button>
    </div>
  </form>

    <table align="center" border="1"> 
        <tr>
            <th>Name</th>
            <th>Code</th>
        </tr>
        <tr v-for="item in value" v-bind:key="item.Name">
            <td>{{item.Name}}</td>
            <td>{{item.Code}}</td>
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
    post_name() {
        axios.get(
            '/api/serach_code',{
            params: {
                name_input:this.name_input,
            }
        }
    ).then((response) => {
        this.value = response.data
      }).catch(error => alert(error + '\nErrormessage'));
      this.name_input = ""
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