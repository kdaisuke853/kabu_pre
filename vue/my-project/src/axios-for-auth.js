import axios from 'axios';

const instance = axios.create({
  //baseURL: 'http://127.0.0.1:8000'
  //baseURL: "http://localhost:8001",
  //baseURL: "http://django:8001",
  baseURL: "http://localhost",
  //browserBaseURL: "http://localhost",
});

export default instance;