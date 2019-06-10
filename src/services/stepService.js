import api from '@/services/api'

export default {
  postCleaningStep(payload) {
    return api.post(`cleaning/`, payload)
              .then(response => response.data)
  }
}