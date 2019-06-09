import Vue from 'vue';
import Vuex from 'vuex';
import stepModule from './modules/step';
import queryModule from './modules/query';
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    step: stepModule,
    query: queryModule,
  },
  plugins: [createPersistedState()],
});
