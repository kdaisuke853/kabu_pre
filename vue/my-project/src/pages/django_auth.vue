<template>
<div class="container">
  <div class="bg_image">
    <h2>ログイン</h2>
      <div class="center-block">
        <b-button v-b-modal.modal-1 @click="$bvModal.show('login-form')" class="m-5">ログイン</b-button>

        <b-modal id="login-form" hide-footer>
        <!--<modal name="modal-content">-->
          <template #modal-title>
            Login
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
            <b-button v-b-modal.modal-1 @click="login()">送信</b-button>
          </div>
          
          </form>
        <!--</modal>-->
        </b-modal>
      </div>
  </div>
</div>
</template>

<script>


//import axios from '../axios-for-auth.js';
export default {
  data() {
    return {
      username: "",
      password: "",
      showContent: false,
    };
  },
  methods: {
    login() {
        this.$store.dispatch('login', {
        username: this.username,
        password: this.password,
        returnSecureToken: true
        });
      //axios.post(
      //  '/auth/',
      //  {
      //    username: this.username,
      //    password: this.password,
      //    returnSecureToken: true
      //  }
      //).then((response) => {
      //    this.$store.commit('updateIdToken', response.data.token); 
          //this.$router.push('/');
      //  console.log(response);
      //  console.log(this.$store)
        //localStorage.setItem("my_token", response.data.token);
     //   this.$store.dispatch("auth", {
      //    userToken: response.data.token
      //  });
     // });
      this.username = "";
      this.password = "";
      //this.$router.push('/django_task');
    },
  }
};
</script>

<style>
.input-group {
  margin: 5px;
}
</style>