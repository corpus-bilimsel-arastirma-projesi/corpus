<template>
  <v-card>

    <v-toolbar dark color="primary">
      <v-btn icon dark v-on:click="backClickButton">
        <v-icon>close</v-icon>
      </v-btn>
      <v-toolbar-title>Preview: {{selectedFileName}}</v-toolbar-title>
    </v-toolbar>

    <v-list subheader>

      <v-subheader>Source Comparison</v-subheader>

      <split-panes
          class="default-theme"
          style="height: 400px"
          @resized="handleResize"
          @ready="handleSize"
      >

        <div splitpanes-min="20">

          <highcharts style="width: 100%; height: 100%;"
                      :options="wordCloudData"
                      ref="wordCloudChart">
          </highcharts>

        </div>

        <div splitpanes-min="20">

          <highcharts style="width: 100%; height: 100%;"
                      :options="verticalBarData"
                      ref="verticalBarChart">
          </highcharts>

        </div>

      </split-panes>

    </v-list>

    <v-divider></v-divider>

    <v-list three-line subheader>
      <v-subheader>Options</v-subheader>
      <v-layout justify-center align-center>
        <div v-for="c in checkboxes">
          <v-flex pr-3>
            <v-checkbox
                v-model="c.value"
                :label="c.label"
            ></v-checkbox>
          </v-flex>
        </div>
      </v-layout>

      <v-flex justify-center align-center xs6 offset-xs3 pt-3>
        <v-text-field
            label="How many words do you want to get?"
            v-model="howMany"
        ></v-text-field>
      </v-flex>
    </v-list>

    <v-footer fixed class="pa-3" height="60" dark color="primary">
      <v-btn icon dark v-on:click="backClickButton">
        <v-icon>close</v-icon>
      </v-btn>

      <v-divider></v-divider>

      <v-btn icon dark v-on:click="continueClickButton">
        <v-icon>done</v-icon>
      </v-btn>
    </v-footer>


  </v-card>
</template>

<script>
  import {mapGetters} from "vuex"
  import splitPanes from 'splitpanes'
  import vueWordCloud from 'vuewordcloud'

  export default {
    components: {
      splitPanes, vueWordCloud
    },
    props: {
      selectedFileName: String,
    },
    data: () => {
      return {
        checkboxes: [
          {label: "Stop Words", value: false},
          {label: "Punctuations", value: false}
        ],
        howMany: 50,
        options: {
          title: {
            text: 'Source / Occurrences'
          },

          chart: {
            type: 'column'
          },

          xAxis: {
            categories: []
          },

          series: []
        },
        wordCloudOptions: {
          series: [{
            type: 'wordcloud',
            data: [],
            name: 'Occurrences'
          }],

          title: {
            text: 'WORDCLOUD'
          }
        }
      }
    },
    computed: {
      ...mapGetters({
        PREVIEW_WORD_CLOUD: 'PREVIEW_WORD_CLOUD',
        PREVIEW_VERTICAL_BAR: 'PREVIEW_VERTICAL_BAR',
        PREVIEW_VERTICAL_BAR_CATEGORIES: 'PREVIEW_VERTICAL_BAR_CATEGORIES'
      }),
      verticalBarData: function () {
        let chart = this.options
        chart.xAxis.categories = this.PREVIEW_VERTICAL_BAR_CATEGORIES
        chart.series = [{
          data: this.PREVIEW_VERTICAL_BAR
        }]
        return chart
      },
      wordCloudData: function () {
        let wordCloudOptions = this.wordCloudOptions
        wordCloudOptions.series = [{
          type: 'wordcloud',
          data: this.PREVIEW_WORD_CLOUD,
          name: 'Occurrences'
        }]
        return wordCloudOptions
      }
    },
    methods: {
      backClickButton() {
        this.$emit('back-clicked', false)
      },
      continueClickButton() {
        let payload = []
        let checkboxes = []
        payload.push(this.$store.getters.UUID)
        this.checkboxes.forEach(x => {
          if (x.value === true) {
            checkboxes.push(x.label)
          }
        })
        payload.push(checkboxes)
        payload.push(this.howMany)
        this.$emit('continue-clicked', payload)
      },
      handleResize(event) {
        this.$refs.wordCloudChart.chart.setSize(window.innerWidth * event[0].width / 100, 400, false)
        this.$refs.verticalBarChart.chart.setSize(window.innerWidth * event[1].width / 100, 400, false)
      },
      handleSize() {
        this.$refs.wordCloudChart.chart.setSize(window.innerWidth / 2, 400, false)
        this.$refs.verticalBarChart.chart.setSize(window.innerWidth / 2, 400, false)
      }
    }
  }
</script>

<style scoped>
  @import '~splitpanes/dist/splitpanes.css';

  .splitpanes__pane {
    justify-content: center;
    align-items: center;
    display: flex;
  }

  .splitpanes__pane span {
    font-family: Helvetica, Arial, sans-serif;
    color: #fff;
    font-size: 5em;
    opacity: 0.6;
  }
</style>