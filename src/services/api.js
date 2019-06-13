import axios from 'axios'
import {store} from '../store/store';

let JWT_ACCESS = localStorage.getItem('a')

const http = axios.create({ // TODO: Will be implemented with JWT
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

http.interceptors.request.use (
  function (config) {
    const token = store.token;
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config
  },
  function (error) {
    return Promise.reject (error)
  }
)

export default http