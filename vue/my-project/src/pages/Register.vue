<template>
<div class="container">
  <h2>新規登録</h2>
  <form class="login-form">
    <div class="input-group">
      <label for="email">メールアドレス</label>
      <input type="email" id="email" v-model="email"> 
    </div>
    <div class="input-group">
      <label for="password">パスワード(6文字以上)</label>
      <input type="password" id="password" v-model="password">
    </div>
    <div class="input-group">
      <button type="button" @click="register()">新規登録</button>
    </div>
  </form>
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
    register() {
      axios.post('/accounts:signUp?key=AIzaSyBq6fuConBcTGJBcLYMDRaFQW1AJaR5ZWs',
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