<template>
  
  <div class="container_t">
    <h2>タスク管理ページです</h2>
    <div class="task_get">
    <!--<div id ='wrap'> <p>トークン表示</p></div>-->
      <button type="button" @click="token_log()">確認する</button>
    </div>
    <!--<input type ="text" v-model="this.info">-->
    <!--タスク表示-->
    <div class="ul-align-center">
    <ul>
      <li v-for="item in info" :key="item.title" class="task_list">
        タスク名:{{item.title}} <button type="button" class="button" @click="delete_task(item.id)">削除</button>
      </li>  
    </ul>
    
    <br>
    <!--タスク作成-->
    <h3>タスク作成</h3>
      <label for="title">タスク名:</label>
      <input type="text" id="task" v-model="title">
      <button type="button" @click="new_task()">作成する</button>
    </div>

    </div>
</template>

<script>

import axios from '../axios-for-auth.js';

export default {
  data: function () {
  return {
    //responseの受け取り口を用意
    info: [],
    title: ""
  }
},
  computed: {
    idToken() {
      //tokenを返す
      return this.$store.getters.idToken;
    },

  },
  methods: {
    //getメソッドでタスクを取得
    token_log() {
      console.log(`${this.idToken}`)
        axios.get('/api/tasks/',{
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${this.idToken}`
            }
        })
        .then((response) => {
          
            //console.log(response);       
            //console.log(response.data['1'].id)
            //document.write('<p>'+ response.data + '</p>');
            this.info = response.data
            //document.getElementById('wrap').insertAdjacentHTML('beforeend',response.data['1'].title);

        });
    },
    new_task(){
    const data = {
      title:this.title
    }
    console.log(`${this.idToken}`)
    console.log(this.title)
    axios.post(
      "/api/tasks/", data,
      {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${this.idToken}`
      }
    }
    )
    .then(response => {
      console.log(response);
    })
    .catch(error =>{
      console.log(error);
    })
    this.title = "";
  },


  delete_task(id){
    axios.delete(
      `/api/tasks/${id}`,
      {
        headers:
    {
     'Authorization': `Token ${this.idToken}`
    }
    })
    .then(response => {
      console.log(response);
    })
    .catch(error =>{
      console.log(error);
      alert(error + '\n既に存在しないタスクです')

    })
    this.title = "";
  },


 }
}
</script>

