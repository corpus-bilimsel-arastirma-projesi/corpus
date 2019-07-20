import api from '@/services/api'

export default {
  postFileNamesGivenUser(payload) {
    return api.post(`file/`, payload)
      .then(response => response.data)
  },
  deleteGivenFileName(payload) {
    return api.delete(`file/`, payload)
      .then(response => response.data)
  },
  postConcatFiles(payload) {
    return api.post(`file/concat/`, payload)
      .then(response => response.data)
  }
}