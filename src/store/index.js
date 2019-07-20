import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import VueAxios from 'vue-axios'
import previewModule from './modules/plotly';
import stepModule from './modules/operations';
import preparationModule from './modules/preparation'
import authenticationModule from './modules/authentication';
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

export default new Vuex.Store({
  modules: {
    stepModule: stepModule,
    previewModule: previewModule,
    preparationModule: preparationModule,
    authenticationModule: authenticationModule,
  },
  plugins: [createPersistedState()],
});
