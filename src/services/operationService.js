import api from '@/services/api'

export default {
  getColumnNames(payload) {
    return api.get(`file/column-names/${payload}/`)
  },
  postColumnMapping(payload) {
    return api.post(`file/column-mapping/`, payload)
      .then(response => response.data)
  },
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