import actions from './actions'
import getters from './getters'
import mutations from './mutations'

const state = {
  PREVIEW_SOURCES: null,
  STACKED: null,
  MULTIPLE_LINES: null
}

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
}
