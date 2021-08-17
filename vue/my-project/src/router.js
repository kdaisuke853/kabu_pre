import Vue from 'vue';
import Router from 'vue-router';
//import Home from './pages/Home.vue';
import django_auth from './pages/django_auth.vue'
import django_task from './pages/django_task.vue'
import value_get from './pages/value_get.vue'
import store from './store';
import value_gets from './pages/django_outputs'
import after_auth from './pages/After_auth'
import post_data from './pages/post_data'
import graph_test from './pages/graph_test'
import sign_up from './pages/signup_post'
import search_code from './pages/search_code'
import candle from './pages/candlechart.vue'
import Home from './pages/Home.vue'
import predict_display from './pages/predict_display.vue'

Vue.use(Router);

export default new Router({
  //mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "*",
      redirect: '/',
    },
    {
      path: "/",
      component: django_auth,
      beforeEnter(to, from, next){
        if (store.getters.idToken){
          next('/after_auth');
        } else {
          next();
        }
      }
    },
    {
      path: "/description",
      component: Home,
    },
    {
      path: "/after_auth",
      component: after_auth,
      beforeEnter(to, from, next){
        if (store.getters.idToken){
          next();
        } else {
          next('/');
        }
      }
    },
    {
      path: "/django_auth",
      component: django_auth,
      beforeEnter(to, from, next){
        if (store.getters.idToken){
          next('/after_auth');
        } else {
          next();
        }
      }
    },
    {
      path: "/django_task",
      component: django_task,
      beforeEnter(to, from, next){
        if (store.getters.idToken){
          next();
        } else {
          next('/');
        }
      }
    },
    {
      path: "/value_get",
      component: value_get,
      beforeEnter(to, from, next){
        if (store.getters.idToken){
          next();
        } else {
          next('/');
        }
      }
    },
    {
      path: "/value_gets",
      component: value_gets,
      beforeEnter(to, from, next){
        //var strage = localStorage.getItem('datalist');

        if (store.getters.idToken){
          next();

          //if(strage){
          //  alert('1年分のデータは取得済みです。株価予測とグラフを表示機能ができます。');
          //  next('/post_data');
          //} else {
          //  next();
          //}

        } else {
          next('/');
        }

      }
    },
    {
      path: "/sign_up",
      component: sign_up,
      beforeEnter(to, from, next) {
        if (store.getters.idToken) {
          next("/");
        } else {
          next();
        }
      },
    },
    {
      path: "/post_data",
      component: post_data,
      beforeEnter(to, from, next){
        var strage = localStorage.getItem('datalist');
        if (store.getters.idToken){
          next();

          if(strage){
            next();
          } else {
            alert('1年分のデータを取得してください');
            next('/value_gets');
          }

        } else {
          next('/');
        }
      }
    },
    {
      path:"/graph_test",
      component: graph_test,
      beforeEnter(to, from, next){
        var strage = localStorage.getItem('datalist');
        if (store.getters.idToken){
          next();
          if(strage){
            next();
          } else {
            alert('1年分のデータを取得してください');
            next('/value_gets');
          }

        } else {
          next('/');
        }
      }
    },
    {
      path:"/candle",
      component: candle,
      beforeEnter(to, from, next){
        var strage = localStorage.getItem('datalist');
        if (store.getters.idToken){
          next();
          if(strage){
            next();
          } else {
            alert('1年分のデータを取得してください');
            next('/value_gets');
          }

        } else {
          next('/');
        }
      }
    },
    {
      path: "/search_code",
      component: search_code,
      beforeEnter(to, from, next){
        if (store.getters.idToken){
          next();
        } else {
          next('/');
        }
      }
    },
    {
      path: "/predict_display",
      component: predict_display,
      beforeEnter(to, from, next){
        if (store.getters.idToken){
          next();
        } else {
          next('/');
        }
      }
    },
  ],
});