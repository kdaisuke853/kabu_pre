<template>
  <div>

      <div class="header-fixed">
        <h1 class="header-logo">Myapp</h1>
      </div>
        <nav class="pc-nav"> 
          <ul class="nav-wrap">
            <li class="item"><router-link to="/" class="header--link" v-if="!isAuthenticated">トップ</router-link></li>
            <li class="item"><router-link to="/after_auth" class="header--link" v-if="isAuthenticated">マイページ</router-link></li>
      <!--<router-link to="/about" class="header--link" v-if="isLoggedIn">詳細</router-link>|
      <router-link to="/login" class="header--link" v-if="!isLoggedIn">ログイン</router-link>|
      <router-link to="/register" class="header--link" v-if="!isLoggedIn">新規登録</router-link>|-->
            <li class="item"><router-link to="/django_auth" class="header--link" v-if="!isAuthenticated">ログイン</router-link></li>
            <li class="item"><router-link to="/django_task" class="header--link" v-if="isAuthenticated">タスク確認</router-link></li>
            <li class="item"><router-link to="/value_get" class="header--link" v-if="isAuthenticated" >株価取得</router-link></li>
      <!--<router-link to="/kasou" class="header--link">仮想通貨取得</router-link>|-->
            <li class="item"><router-link to="/value_gets" class="header--link" v-if="isAuthenticated">株価取得(複数)</router-link></li>

            <li class="item"><router-link to="/post_data" class="header--link" v-if="isAuthenticated">株価機械学習</router-link></li>
            <li class="item"><router-link to="/graph_test" class="header--link" v-if="isAuthenticated">株価グラフ</router-link></li>
      <!--<a href="http://127.0.0.1:8000/api/tasks/">test</a>-->
          </ul>
        </nav>
    <div class="body_content">
      <router-view></router-view>
    </div>
  </div>