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

      <split-panes class="default-theme" style="height: 400px">

        <div style="width: 100%; height: 100%;" splitpanes-min="20">
          {{PREVIEW_WORD_CLOUD}}
        </div>

        <div style="width: 100%; height: 100%;">
          {{PREVIEW_VERTICAL_BAR}}
          <!--<div class="word-cloud">-->
          <!--<vue-word-cloud :words="PREVIEW_WORD_CLOUD">-->
          <!--<template slot-scope="{text, weight, word}">-->
          <!--<div v-tooltip="'Word: ' + text + ', Frequency: ' + weight" style="cursor: pointer;">-->
          <!--{{ text }}-->
          <!--</div>-->
          <!--</template>-->
          <!--</vue-word-cloud>-->
          <!--</div>-->
        </div>

      </split-panes>

    </v-list>

    <v-divider></v-divider>

    <v-list three-line subheader>
      <v-subheader>Options</v-subheader>
      <v-layout justify-center align-center>
        <v-flex row xs2 v-for="c in checkboxes">
          <v-checkbox
              v-model="c.value"
              :label="c.label"
          ></v-checkbox>
        </v-flex>
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
      splitPanes,
      vueWordCloud
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
        howMany: 50
      }
    },
    computed: {
      ...mapGetters({
        PREVIEW_WORD_CLOUD: 'PREVIEW_WORD_CLOUD',
        PREVIEW_VERTICAL_BAR: 'PREVIEW_VERTICAL_BAR'
      })
    },
    methods: {
      backClickButton() {
        this.$emit('back-clicked', false)
      },
      continueClickButton() {
        let payload = []
        let checkboxes = []
        payload.push(this.$store.getters.UUID)
        payload.push(checkboxes)
        payload.push(10)
        this.$emit('continue-clicked', payload)
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

  .word-cloud {
    width: 100%;
    height: 90%;
  }
</style>