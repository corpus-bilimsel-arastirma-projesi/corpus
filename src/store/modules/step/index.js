import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  STEP_NUMBER: '1',
  JSON_FILE: '',
  JSON_TABLE: '',
  WORD_CLOUD: '',
  READY: false,
  UUID: '',
  BUTTON_NAME: 'Cancel'
};

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
};
