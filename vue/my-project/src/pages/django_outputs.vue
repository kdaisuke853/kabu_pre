<template>

<div class="container">
  <div v-if="content">
    <h2>株価(1年分)を取得したい銘柄コードを入力してください</h2>
  
  <!--モーダル前
  <div v-if="!show"> 
    <form class="login-form">
    <div class="input-group">
      <button type="button"  @click="post_code()">送信</button>
    </div>

        <label for="code_input2">株価コード:</label>
        <input type="text" id="code_input" v-model="code_input">
        <button type="button"  @click="post_code(),code_set()">送信</button>

    </form>
  </div>
  -->

  <b-form-group id="input-name" label="Code:" label-for="input-name">
    <b-form-input
        id="code_input"
        v-model="code_input"
        placeholder="Enter code"
        required
    ></b-form-input>

  
      <b-button v-b-modal.modal-1 @click="post_code(),$bvModal.show('value_code')" class="m-5">株価取得</b-button>
  </b-form-group>

      <b-modal id="value_code" hide-footer>
          <template #modal-title>
            １年分の株価取得結果
          </template>
          
          <div v-if="show">
            <ul>
              {{value.name}}の株価データ１年分の取得に成功しました。データ予測が可能です。
              <li v-for="(item,index) in value.timestamp" v-bind:key="index" class="task_list">
              値段:{{value.open[index]}}値:{{index}}
              </li>  
            </ul>
          </div>

          <div v-if="!show">
            株価取得に失敗しました。コードが存在しない可能性があります
          </div>

          </b-modal>

    </div>

    <div v-if="!content">
      <h4>現在、{{value.name}}の1年分の株価データを取得ずみです。</h4>
        <div class="cards">
          <b-card-group deck>
            <div>
              <b-card
                title="Yahoo finace"
                img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRASmZmK6i8gCvKyiBgv5qIs_u1jj8_PaXqA&usqp=CAU"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
              >
                <b-card-text>
                  取得した銘柄のWebページです(Yahoo finace)
                </b-card-text>

                <b-button v-bind:href="'https://finance.yahoo.co.jp/quote/'+this.code_input+'.T'" variant="primary" 
                target="_blank" rel="noopener noreferrer">Go website</b-button>
              </b-card>
            </div>

            <div>
              <b-card
                title="株探"
                img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO0ixTVaB4iXAbwm8TvXVdmWFC_tRlkvXV8VvzRC2AJA39h5zXGpmIMfXaPlLD1pkwXQ&usqp=CAU"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
              >
                <b-card-text>
                  取得した銘柄のWebページです(株探)
                </b-card-text>

                <b-button v-bind:href="'https://kabutan.jp/stock/?code='+this.code_input" variant="primary" 
                target="_blank" rel="noopener noreferrer">Go website</b-button>
              </b-card>
            </div>
            <div>
              <b-card
                title="MINKABU"
                img-src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTewLe-aAYA1rxp_qi0YV3iIeIajaxV19nqHQ&usqp=CAU"
                img-alt="Image"
                img-top
                tag="article"
                style="width: 20rem;"
                class="mb-2"
              >
                <b-card-text>
                  取得した銘柄のWebページです(みんかぶ)
                </b-card-text>

                <b-button v-bind:href="'https://minkabu.jp/stock/'+this.code_input" variant="primary" 
                target="_blank" rel="noopener noreferrer">Go website</b-button>
              </b-card>
              </div>
          </b-card-group>
      </div>
      <b-button v-b-modal.modal-1 @click="datareset()" class="m-5">リセット</b-button>

    </div>

  </div>
</template>

<script>
import axios from '../axios-for-auth.js';

export default {
  data() {
    return {
      code_input: "",
      value: [],
      show :false,
      content :true,
    }
  },
  computed: {
    idToken() {
      //tokenを返す
      return this.$store.getters.idToken;
    },
    value_code: function(){
      return this.value != null ? this.value :''
    },
  },

  methods: {
    post_code() {
      if ( this.code_input.match(/^[0-9]{4}$/) )
      {
      axios.get(
        '/api/outputs',{
        params: {
          
          code_input: this.code_input,
          //returnSecureToken: true
        }
    }).then((response) => {
        console.log(response.data);
        this.value = response.data
        if (response.data === "形式が違います"){
          this.$swal({
              icon: "info",
              text: '株価コードを入力してください(数字4桁)'
          })
          this.show = false
        }
        else{
          localStorage.setItem('datalist',JSON.stringify(response.data));
          localStorage.setItem('code',JSON.stringify(this.code_input));
          this.show = true
          this.content = false
        }
      })

      //this.code_input = ""
      }
      else
        this.$swal({
          icon: 'error',
          text: '株価コードを入力してください(数字4桁)'
        })
    },

    datareset(){
      localStorage.clear();
      this.content = true
    }
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