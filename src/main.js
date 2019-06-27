import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import UUID from 'vue-uuid'
import Tooltip from 'vue-directive-tooltip'
import 'vue-directive-tooltip/css/index.css'
import 'vuetify/dist/vuetify.min.css'

/**
 *  BELOW WILL BEE CHANGED
 *  ##########################################
 */

import SmartTable from 'vuejs-smart-table'

Vue.use(SmartTable)

import TextHighlight from 'vue-text-highlight'

Vue.component('text-highlight', TextHighlight)

/**
 * Highchart
 */
import HighchartsVue from 'highcharts-vue'
import Highcharts from 'highcharts'
import exportingModule from 'highcharts/modules/exporting'
import offlineExportingModule from 'highcharts/modules/offline-exporting'
import exportDataModule from 'highcharts/modules/export-data'
import dataModule from 'highcharts/modules/data'
import moreModule from 'highcharts/highcharts-more'
import wordcloud from 'highcharts/modules/wordcloud'
import highcharts3d from 'highcharts/highcharts-3d'
import mapInit from 'highcharts/modules/map'

// Maps
// import { worldmap } from './worldmap';
// import mapAustria from './mapAustria';


// Conf
exportingModule(Highcharts)
offlineExportingModule(Highcharts)
exportDataModule(Highcharts)
dataModule(Highcharts)
moreModule(Highcharts)
wordcloud(Highcharts)
highcharts3d(Highcharts)
mapInit(Highcharts)

// Highcharts.maps.myMapName = worldmap
// Highcharts.maps.geoJSONAustria = mapAustria

Highcharts.setOptions({
  colors: ['#4e79a7', '#edc948', '#e15759', '#76b7b2', '#f28e2b', '#ff9da7', '#FF9655', '#FFF263', '#6AF9C4'],
});

Highcharts.setOptions({
  exporting: {
    buttons: {
      contextButton: {
        menuItems: [
          {
            text: 'Change Types',
            onclick() {
              this.print();
            },
          },
          'printChart',
          'separator',
          'downloadPNG',
          'downloadJPEG',
          'downloadPDF',
          'downloadSVG',
          'separator',
          'downloadCSV',
          'downloadXLS',
          'viewData',
        ],
      },
    },
  },
  credits: false,
});

Vue.use(HighchartsVue)

Vue.prototype.Highcharts = Highcharts

// ##########################################

Vue.use(Vuetify)
Vue.use(UUID)
Vue.use(Tooltip, {
  delay: 50,
  placement: 'top',
  class: '', // ex: 'tooltip-custom tooltip-other-custom'
  triggers: ['hover', 'focus'],
  offset: 2
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
