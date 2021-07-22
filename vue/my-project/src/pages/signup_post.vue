<template>
<div class="container">
  <h2>ユーザ登録</h2>

  <div class="center-block">
    <b-button v-b-modal.modal-1 @click="$bvModal.show('login-form')" class="m-5">ユーザ登録</b-button>
    
    <b-modal id="login-form" hide-footer>
    <!--<modal name="modal-content">-->
      <template #modal-title>
        ユーザ登録
      </template>

      <form class="login-form">
      <b-form-group id="input-name" label="Your Name:" label-for="input-name">
        <b-form-input
          id="input-2"
          v-model="username"
          placeholder="Enter name"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-password" label="Password:" label-for="input-password">
        <b-form-input
          id="input-2"
          v-model="password"
          placeholder="Enter password"
          required
        ></b-form-input>
      </b-form-group>
       <!--<button type="button" @click="login()">送信</button>-->
      <div class="d-block text-center">
        <b-button v-b-modal.modal-1 @click="signup()">登録</b-button>
      </div>
       
      </form>
    <!--</modal>-->
    </b-modal>

  </div>
  
</div>
</template>

<script>

import axios from '../axios-for-auth.js';

export default {
  data() {
    return {
      username: "",
      password: "",
      //showContent: false,
      errors:[],
    };
  },
  methods: {
    signup() {
      axios.post(
        '/api/register/',
        {
          username: this.username,
          password: this.password,
          returnSecureToken: true
        }
      ).then((response) => {
          this.$store.commit('updateIdToken', response.data.idToken);  
          this.$router.push('/django_auth');
        console.log(response);
      }).catch(error => alert(error + '\nErrormessage:ユーザ登録に失敗しました'));

      this.username = "";
      this.password = "";

    },
  }
};
</script>

<style>
.input-group {
  margin: 5px;
}
</style>