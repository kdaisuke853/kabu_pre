<template>
<div class="container">
  <h3>コード検索</h3>
<!--
  <form class="search-form">
    <div class="input-group">
        <label for="name">検索ワード(曖昧検索)</label>
        <input type="text" id="name_input" v-model="name_input">
        <button type="button" @click="post_name()">検索</button>
    </div>
  </form>
-->
  <b-form-group id="input-name" label="Word:" label-for="input-name">
    <b-form-input
        id="name_input"
        v-model="name_input"
        placeholder="検索ワードを入力してください(曖昧検索)"
        required
    >
    </b-form-input>
    <b-button v-b-modal.modal-1 @click="post_name()" class="m-5">コード検索</b-button>
  </b-form-group>

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
      if(!this.name_input){
          this.$swal({
            icon: 'error',
            text: '検索ワードを入力してください'
        })
      }
      else if(this.name_input){
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
    }
  },
  }
}
</script>

<style>
</style>