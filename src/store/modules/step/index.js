import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  UUID: '',
  USER_FILES: []
}

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
}
