import api from '@/services/api'

export default {
  postFileNamesGivenUser(payload) {
    return api.post(`files/`, payload)
      .then(response => response.data)
  },
  deleteGivenFileName(payload) {
    return api.delete(`files/`, payload)
      .then(response => response.data)
  }
}