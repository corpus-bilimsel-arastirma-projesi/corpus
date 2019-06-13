import axios from 'axios'
// import Cookies from 'js-cookie'

let JWT_ACCESS = localStorage.getItem('a')

export default axios.create({ // TODO: Will be implemented with JWT
  baseURL: '/api',
  // timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': "Bearer "+JWT_ACCESS
  }
})