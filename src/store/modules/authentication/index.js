import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  jwt: localStorage.getItem('t'),
  endpoints: {
    obtainJWT: 'http://0.0.0.0:10000/auth/obtain_token', // TODO: obtainJWT endpoint
    refreshJWT: 'http://0.0.0.0:10000/auth/refresh_token' // TODO: refreshJWT endpoint
  }
}

export default {
  namespaced: false,
  state,
  actions,
  getters,
  mutations,
};
