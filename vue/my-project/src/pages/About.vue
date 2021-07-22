<template>
  <div class="container">
    <h2>詳細ページです</h2>
    <p>ログインが必要なページです</p>
    <button type="button" @click="logout()">ログアウトする</button>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.commit('updateIdToken', null);
      this.$router.push('/login');
    }
  }
}
</script>