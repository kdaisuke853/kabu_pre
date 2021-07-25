
<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand to="/">株プレ</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/sign_up" class="header--link" v-if="!isAuthenticated">ユーザ登録</b-nav-item>
        <b-nav-item to="/django_auth" class="header--link" v-if="!isAuthenticated">ログイン</b-nav-item>
        <!--
        <b-nav-item to="/value_get" class="header--link" v-if="isAuthenticated" >株価取得</b-nav-item>
        <b-nav-item to="/value_gets" class="header--link" v-if="isAuthenticated">株価取得(1年)</b-nav-item>
        -->
        <div v-if="isAuthenticated">
            <b-nav-item-dropdown right>
                <template #button-content>
                  <em>株価取得機能一覧</em>
                </template>
                <b-dropdown-item to="/value_get">今日の株価取得(最新)</b-dropdown-item>
                <b-dropdown-item to="/value_gets">株価取得(直近1年)</b-dropdown-item>
            </b-nav-item-dropdown>
          </div>

        <div v-if="isAuthenticated">
          <b-nav-item-dropdown right>
            <template #button-content>
              <em>株価グラフ表示機能一覧</em>
            </template>
            <b-dropdown-item to="/graph_test">株価グラフ(直近10日間)</b-dropdown-item>
            <b-dropdown-item to="/candle">ローソク足チャート(1年)</b-dropdown-item>
          </b-nav-item-dropdown>
        </div>


        <b-nav-item to="/post_data" class="header--link" v-if="isAuthenticated">株価予測</b-nav-item>
        <b-nav-item to="/search_code" class="header--link" v-if="isAuthenticated">コード検索</b-nav-item>
      </b-navbar-nav>
      
      <b-navbar-nav class="ml-auto">
        <div v-if="isAuthenticated">
          <b-nav-item-dropdown right>
            <template #button-content>
              <em>サブメニュー</em>
            </template>
            <b-dropdown-item to="/django_task">タスク確認</b-dropdown-item>
            <b-dropdown-item href="#" @click="logout()">ログアウト</b-dropdown-item>
          </b-nav-item-dropdown> 
        </div>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <div class="body_content">
    <router-view></router-view>
  </div>
</div>
</template>
  

<script>
export default {
  data(){
    return {
      show: true
    };
  },

  methods: {
    logout() {
      this.$store.dispatch('logout');
    },
  },

  computed: {
      isAuthenticated() {
        return this.$store.getters.idToken != null;
      },
    }
  };

</script>

<style>

@import "./css/style.css";
@import "./css/reset.css";

/* 表示アニメーションをする前のスタイル */
/* はじめ */
.v-enter {
  /* 最初は表示して欲しくないので 0 */
  opacity: 0;
}
/* transition している間 */
.v-enter-active {
  transition: opacity 1s
}
/* おわり */
.v-enter-to {
  /* 終わったら表示して欲しいので 1 */
  opacity: 1;
}

</style>