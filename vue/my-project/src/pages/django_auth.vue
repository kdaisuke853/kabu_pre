<template>
<section class="home-hero">
<div class="container">
  <div class="home-hero__content">
        <div class="center-block">
        <h2 class="m-5">株プレ</h2>
        <b-button v-b-modal.modal-1 @click="$bvModal.show('register-form')" class="m-5">ユーザ登録</b-button>

        <b-modal id="register-form" hide-footer>
        <!--<modal name="modal-content">-->
          <template #modal-title>
            ユーザ登録
          </template>

          <form class="register-form">
          <b-form-group id="input-name" label="Your Name:" label-for="input-name">
            <b-form-input
              id="input_1"
              v-model="username"
              placeholder="Enter name"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-password" label="Password:" label-for="input-password">
            <b-form-input
              id="input_2"
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

        <b-button v-b-modal.modal-1 @click="$bvModal.show('login-form')" class="m-5">ログイン</b-button>

        <b-modal id="login-form" hide-footer>
        <!--<modal name="modal-content">-->
          <template #modal-title>
            Login
          </template>
          
          <form class="login-form">
          <b-form-group id="input-name" label="Your Name:" label-for="input-name">
            <b-form-input
              id="input_3"
              v-model="username"
              placeholder="Enter name"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-password" label="Password:" label-for="input-password">
            <b-form-input
              id="input_4"
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
</section>
</template>

<script>
import axios from '../axios-for-auth.js';

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
      if(!this.username && !this.password){
          this.$swal({
            icon: 'error',
            text: 'ユーザ名とパスワードを入力してください'
        })
      }
      else if(!this.username){
          this.$swal({
            icon: 'error',
            text: 'ユーザ名を入力してください'
        })
      }
      else if(!this.password){
          this.$swal({
            icon: 'error',
            text: 'パスワードを入力してください'
        })
      }
      else if(this.username && this.password){
        this.$store.dispatch('login', {
        username: this.username,
        password: this.password,
        returnSecureToken: true
        });
      this.username = "";
      this.password = "";
      }
    },

    signup() {
      if(!this.username && !this.password){
          this.$swal({
            icon: 'error',
            text: 'ユーザ名とパスワードを入力してください'
        })
      }
      else if(!this.username){
          this.$swal({
            icon: 'error',
            text: 'ユーザ名を入力してください'
        })
      }
      else if(!this.password){
          this.$swal({
            icon: 'error',
            text: 'パスワードを入力してください'
        })
      }
      else if(this.username && this.password){
      axios.post(
        '/api/register/',
        {
          username: this.username,
          password: this.password,
          returnSecureToken: true
        }
      ).then((response) => {
          this.$store.commit('updateIdToken', response.data.idToken);  
        console.log(response);
        this.$swal({
            icon: 'success',
            text: 'ユーザ登録に成功しました'
        })
      }).catch(error => alert(error + '\nErrormessage:ユーザ登録に失敗しました'));

      this.username = "";
      this.password = "";
      }
    },
  }
};
</script>

<style>

</style>