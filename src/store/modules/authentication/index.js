import actions from './actions';
import getters from './getters';
import mutations from './mutations';

const state = {
  EMAIL: '',
  JWT_ACCESS: localStorage.getItem('accessToken'),
  JWT_REFRESH: localStorage.getItem('refreshToken'),
  ACCESS_EXPIRY: parseInt(localStorage.getItem("accessExpiry")),
  REFRESH_EXPIRY: parseInt(localStorage.getItem("refreshExpiry")),
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
