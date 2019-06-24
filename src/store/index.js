import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import VueAxios from 'vue-axios'
import stepModule from './modules/step';
import queryModule from './modules/query';
import previewModule from './modules/preview';
import authenticationModule from './modules/authentication';
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

export default new Vuex.Store({
  modules: {
    step: stepModule,
    query: queryModule,
    previewModule: previewModule,
    authentication: authenticationModule,
  },
  plugins: [createPersistedState()],
});
