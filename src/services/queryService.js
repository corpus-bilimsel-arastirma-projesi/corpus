import api from '@/services/api'

export default {
  postFileNames(payload) {
    return api.post(`query/`, payload)
              .then(response => response.data)
  }
}