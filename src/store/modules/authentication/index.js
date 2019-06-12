import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  JWT_ACCESS: localStorage.getItem('a'),
  JWT_REFRESH: localStorage.getItem('r'),
  ENDPOINTS: {
    OBTAIN_JWT: 'token/', // TODO: obtainJWT endpoint
    REFRESH_JWT: 'token/refresh/' // TODO: refreshJWT endpoint
  }
}

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
};
