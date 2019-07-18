<template>
  <v-app style="height: 1000px;">

    <split-pane
        v-on:resize="resize" :min-percent='20' :default-percent='50' split="horizontal"
    >

      <template slot="paneL">

        <Plotly
            style="height: 100%"
            :data="STACKED.data"
            :layout="STACKED.layout"
            :display-mode-bar="true"
        >
        </Plotly>

      </template>
      <template slot="paneR">
        <split-pane split="vertical">
          <template slot="paneL">

            <Plotly
                style="height: 100%"
                :data="PREVIEW_SOURCES.data"
                :layout="PREVIEW_SOURCES.layout"
                :display-mode-bar="true"
            >
            </Plotly>

          </template>
          <template slot="paneR">

            <Plotly
                style="height: 100%"
                :data="MULTIPLE_LINES.data"
                :layout="MULTIPLE_LINES.layout"
                :display-mode-bar="true"
            >
            </Plotly>

          </template>
        </split-pane>
      </template>

    </split-pane>

  </v-app>
</template>

<script>
  import {mapGetters} from "vuex"
  import {Plotly} from 'vue-plotly'
  import splitPane from 'vue-splitpane'

  export default {
    components: {
      Plotly, splitPane
    },
    data: () => {
      return {}
    },
    computed: {
      ...mapGetters({
        PREVIEW_SOURCES: 'PREVIEW_SOURCES',
        STACKED: 'STACKED',
        MULTIPLE_LINES: 'MULTIPLE_LINES'
      }),
    }
  }
</script>