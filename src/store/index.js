import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import VueAxios from 'vue-axios'
import stepModule from './modules/step';
import previewModule from './modules/plotly';
import authenticationModule from './modules/authentication';
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

export default new Vuex.Store({
  modules: {
    step: stepModule,
    previewModule: previewModule,
    authentication: authenticationModule,
  },
  plugins: [createPersistedState()],
});
