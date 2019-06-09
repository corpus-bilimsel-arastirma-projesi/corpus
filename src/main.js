import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import UUID from 'vue-uuid';
import Tooltip from 'vue-directive-tooltip';
import 'vue-directive-tooltip/css/index.css';

import 'vuetify/dist/vuetify.min.css'


Vue.use(Vuetify)
Vue.use(UUID);
Vue.use(Tooltip, {
  delay: 50,
  placement: 'top',
  class: '', // ex: 'tooltip-custom tooltip-other-custom'
  triggers: ['hover', 'focus'],
  offset: 2
});

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
