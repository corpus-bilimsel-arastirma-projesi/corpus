import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  JWT: localStorage.getItem('t'),
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
