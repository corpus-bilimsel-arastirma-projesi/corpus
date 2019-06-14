import axios from 'axios'
import store from '../store/index'

const http = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

http.interceptors.request.use (
  function (config) {
    const token = store.getters.JWT_ACCESS || localStorage.getItem('a');
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config
  },
  function (error) {
    return Promise.reject (error)
  }
)

export default http