import api from '@/services/api'

export default {
  getValueCounter(payload) {
    return api.get(`plot/?type=valueCounter&category=source&number=10&uuid=${payload}`)
              .then(response => response.data)
  },
  getStack(payload) {
    return api.get(`plot/?type=stackedPlot&category1=date&category2=source&uuid=${payload}`)
      .then(response => response.data)
  },
  getMultipleLines(payload) {
    return api.get(`plot/?type=multipleLinesGraph&category1=date&category2=source&uuid=${payload}`)
      .then(response => response.data)
  }
}