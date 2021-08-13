<template>
<section class="home-hero">
<div class="mytop">
  <div class="top_content">
    <div class="top_font">
      <p class="top_msg">
        株価確認をより簡単に<br>
        機械学習をより身近に<br>
      </p>
      <p class="top_name">
      株価情報アプリ「株プレ」
      </p>
      <b-button v-b-modal.modal-1 @click="$bvModal.show('register-form')" class="m-5">ユーザ登録</b-button>
      <b-button v-b-modal.modal-1 @click="$bvModal.show('login-form')" class="m-5">ログイン</b-button>
      <b-button v-b-modal.modal-1 @click="guestlogin()" class="m-5">ゲストログイン</b-button>
    </div>
  </div>
</div>

<div class="container">
  <div class="home-hero__content">
        <div class="center-block">
        <v-main>
        <div class="discription">
          <h2>株プレとは</h2>
          <p class="discription__comment">
            現在の株価取得、1年間の株価取得を1クリックでできる「株価情報アプリ」です。<br>
            取得した株価情報を元にグラフ表示や株価の予測をすることも可能です。<br>
          </p>
        </div>
        <hr>
        <div class="features">
          <h2>株プレの主な機能</h2>
          <b-container class="d-flex justify-content">
            <b-card-group deck>
            <div class="features_list">
              <div>
                <b-card
                  title="株価取得機能"
                  img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
                  img-alt="Image"
                  img-top
                  tag="article"
                  style="max-width: 20rem;"
                  class="mb-2"
                  border-variant="dark"
                >
                  <b-card-text>
                    最新の株価取得や直近1年間の株価を取得できます。<br><br><br>
                  </b-card-text>
                </b-card>
              </div>
              <div>
                <b-card
                  title="株価グラフ"
                  img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
                  img-alt="Image"
                  img-top
                  tag="article"
                  style="max-width: 20rem;"
                  class="mb-2"
                  border-variant="dark"
                >
                  <b-card-text>
                    最新10日間の株価のグラフを始値・終値・高値・安値を選択して表示や1年間分の株価チャートを表示することができます。
                  </b-card-text>

                </b-card>
              </div>
              <div>
              <b-card
                title="株価予測"
                img-src="https://static.amanaimages.com/imgroom/rf_preview640/10319/10319000078.jpg"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
                border-variant="dark"
              >
                <b-card-text>
                  時系列予測を1クリックで実施し、予測した最新の日時の株価を表示させることができます。始値・終値・高値・安値を選択可能です。
                </b-card-text>
              </b-card>
              </div>
            </div>
            </b-card-group>
          </b-container>
          <hr>
        </div>

        <!--
        <div class="button_top">
          <b-button v-b-modal.modal-1 @click="$bvModal.show('register-form')" class="m-5">ユーザ登録</b-button>
          <b-button v-b-modal.modal-1 @click="$bvModal.show('login-form')" class="m-5">ログイン</b-button>
        </div>
        -->
      </v-main>

      
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
    guestlogin() {
        this.$store.dispatch('guestlogin', {
        returnSecureToken: true
        });
      }
    },
  };
</script>

<style>

</style>