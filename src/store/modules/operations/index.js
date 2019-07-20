import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  USER_FILES: [],
  IS_READY: false
}

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
}
