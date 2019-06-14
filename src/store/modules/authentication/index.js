import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  EMAIL: '',
  JWT_ACCESS: localStorage.getItem('a'),
  JWT_REFRESH: localStorage.getItem('r'),
  TOKENS_EXPIRY: parseInt(localStorage.getItem("tokensExpiry")),
  ENDPOINTS: {
    OBTAIN_JWT: 'token/',
    REFRESH_JWT: 'token/refresh/'
  }
}

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
};
