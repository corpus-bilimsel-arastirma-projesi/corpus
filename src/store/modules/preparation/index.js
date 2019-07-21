import actions from './actions'
import getters from './getters'
import mutations from './mutations'

const state = {
  COLUMNS: [],
  FILE_ID: null,
}

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
}
