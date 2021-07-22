<template>
<div class="container">
  <h2>ログイン</h2>
  <form class="login-form">
    <div class="input-group">
      <label for="email">メールアドレス</label>
      <input type="email" id="email" v-model="email">
    </div>
    <div class="input-group">
      <label for="password">パスワード</label>
      <input type="password" id="password" v-model="password">
    </div>
    <div class="input-group">
      <button type="button" @click="login()">送信</button>
    </div>
  </form>
  <button class="btn btn-primary">bootstrap</button>
</div>
</template>

<script>
import axios from '../axios-for-auth.js';
export default {
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    login() {
      axios.post(
        '/accounts:signInWithPassword?key=AIzaSyBq6fuConBcTGJBcLYMDRaFQW1AJaR5ZWs',
        {
          email: this.email,
          password: this.password,
          returnSecureToken: true
        }
      ).then((response) => {
          this.$store.commit('updateIdToken', response.data.idToken);  
          this.$router.push('/');
        console.log(response);
      });
      this.email = "";
      this.password = "";
    }
  }
}
</script>

<style>
.input-group {
  margin: 5px;
}
</style>