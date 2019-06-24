import actions from './actions'
import getters from './getters'
import mutations from './mutations'

const state = {
  PREVIEW_WORD_CLOUD: null,
  SET_PREVIEW_VERTICAL_BAR: null
}

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
}
