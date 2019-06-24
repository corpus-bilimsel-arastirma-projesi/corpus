import api from '@/services/api'

export default {
  postPreviewSources(payload) {
    return api.post(`stats/`, payload)
              .then(response => response.data)
  }
}