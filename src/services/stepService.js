import api from '@/services/api'

export default {
  postCleaningStep(payload) {
    return api.post(`cleaning/`, payload)
              .then(response => response.data)
  },
  postFileNamesGivenUser(payload) {
    return api.post(`files/`, payload)
      .then(response => response.data)
  }
}