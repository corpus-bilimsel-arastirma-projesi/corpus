<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-layout v-if="STEP_NUMBER === '3'" column style="">

    <div class="firstVerticalBar">

      <div class="firstHeader">
        <h3>Word / Frequency Histogram</h3>
      </div>

      <d3-vertical-bar
          style="display: flex;"
          :data="JSON_FILE"
          :options="options"
          width="100%"
          height="700px"> <!-- :margin="margin" -->
      </d3-vertical-bar>

    </div>

    <div class="firstTable">

      <v-data-table
          :headers="headers"
          :items="JSON_TABLE"
          class="elevation-1"
          style="padding-bottom: 50px"
      >
        <template v-slot:items="props">
          <td>{{ props.item.number }}</td>
          <td class="text-xs-left">{{ props.item.word }}</td>
          <td class="text-xs-left">{{ props.item.frequency }}</td>
        </template>
      </v-data-table>

    </div>

    <div class="wordCloud">
      <vue-word-cloud :words="WORD_CLOUD">
        <template slot-scope="{text, weight, word}">
          <div v-tooltip="'Word: ' + text + ', Frequency: ' + weight" style="cursor: pointer;" @click="onWordClick(word)">
            {{ text }}
          </div>
        </template>
      </vue-word-cloud>
    </div>

  </v-layout>
</template>

<script>
  import {d3VerticalBar} from 'd3-vs'
  import vueWordCloud from 'vuewordcloud'
  import {mapGetters} from 'vuex'

  export default {
    components: {
      d3VerticalBar,
      vueWordCloud
    },
    data: () => {
      return {
        options: {
          axisXLabel: 'Word',
          axisYLabel: 'Frequency',
          barTitle: d => d.key + ' ' + d.value
        },
        headers: [
          {
            text: 'Number',
            align: 'left',
            sortable: true,
            value: 'number'
          },
          { text: 'Word', value: 'word' },
          { text: 'Frequency', value: 'frequency' }
        ],
      }
    },
    computed: mapGetters(['STEP_NUMBER', 'JSON_FILE', 'JSON_TABLE', 'WORD_CLOUD']),
    methods: {
    }
  }

</script>

<style lang="stylus" scoped>

  .firstHeader {
    padding-left: 50vw - 5px;
    padding-bottom 2.5vh;
    padding-top: 1vw;
  }

  .wordCloud {
    width: 97vw;
    height 100vh;
  }

</style>
