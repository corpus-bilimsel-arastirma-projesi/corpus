import api from '@/services/api'

export default {
  getValueCounter(payload) {
    return api.get(`plot/?type=value-counter&category=source&number=10&id=${payload}`)
              .then(response => response.data)
  },
  getStack(payload) {
    return api.get(`plot/?type=stacked-plot&category1=date&category2=source&id=${payload}`)
      .then(response => response.data)
  },
  getMultipleLines(payload) {
    return api.get(`plot/?type=multiple-lines-graph&category1=date&category2=source&id=${payload}`)
      .then(response => response.data)
  }
}