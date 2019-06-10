import axios from 'axios'
// import Cookies from 'js-cookie'

export default axios.create({ // TODO: Will be implemented with JWT
  baseURL: '/api',
  // timeout: 5000,
  // headers: {
  //   'Content-Type': 'application/json',
  //   'X-CSRFToken': Cookies.get('csrftoken')
  // }
})