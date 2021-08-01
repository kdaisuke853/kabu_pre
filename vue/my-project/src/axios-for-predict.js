import axios from 'axios';

const instance = axios.create({
  //本番用
  //baseURL: "https://kabupresub.com",
  //検証
  baseURL: "http://localhost:8010",
});

export default instance;