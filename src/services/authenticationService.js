import api from '@/services/api'

export default {
  postObtainToken(payload) {
    return api.post(`token/`, payload)
              .then(response => response.data)
  },
  postRefreshToken(payload) {
    return api.post(`token/refresh/`, payload)
              .then(response => response.data)
  },
  postSignup(payload) {
        return api.post(`user/signup/`, payload)
              .then(response => response.data)
  }

}