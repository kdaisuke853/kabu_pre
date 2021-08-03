import axios from 'axios';

const instance = axios.create({
  //本番用
  baseURL: "https://kabupresub.com",
  //検証用
  //baseURL: "http://localhost",
});

export default instance;