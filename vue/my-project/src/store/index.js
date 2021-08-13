import Vue from 'vue';
import Vuex from 'vuex';
import axios from '../axios-for-auth';
import router from '../router'
//import router from '../router';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    idToken: null
  }, 
  getters: {
    idToken: state => state.idToken
  },

  mutations: {
    updateIdToken(state, idToken) { 
      state.idToken = idToken;
    }
  },
  actions: {
    login({ commit }, authData){
      axios.post(
        '/auth/',
        {
          username: authData.username,
          password: authData.password,
          returnSecureToken: true
        }
      ).then((response) => {
        commit('updateIdToken', response.data.token);
        router.push('/after_auth');
      });
    },
    guestlogin({ commit }){
      axios.post(
        '/auth/',
        {
          username: 'guest',
          password: 'guest',
          returnSecureToken: true
        }
      ).then((response) => {
        commit('updateIdToken', response.data.token);
        router.push('/after_auth');
      });
    },

    logout({ commit }) {
      commit('updateIdToken', null);
      //localStorage.removeItem('idToken');
      //localStorage.removeItem('expiryTimeMs');
      //localStorage.removeItem('refreshToken');
      router.replace('/django_auth');
    },
  }
});

        //this.dispatch('setAuthD')
        //this.$store.commit('updateIdToken', response.data.token); 
        //this.$router.push('/');
        //console.log(response);
        //console.log(this.$store)
        //localStorage.setItem("my_token", response.data.token);
        //this.$store.dispatch("auth", {
        // userToken: response.data.token
