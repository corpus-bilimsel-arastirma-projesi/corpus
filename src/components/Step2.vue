<template>
  <v-layout v-if="STEP_NUMBER === '2'" row style="">

    <div class="wordCloud">
      <vue-word-cloud :words="WORD_CLOUD">
        <template slot-scope="{text, weight, word}">
          <div v-tooltip="'Word: ' + text + ', Frequency: ' + weight" style="cursor: pointer;"
               @click="onWordClick(word)">
            {{ text }}
          </div>
        </template>
      </vue-word-cloud>
    </div>

    <v-divider class="mx-5"
               inset
               vertical></v-divider>

    <div class="checkboxes">

      <h1 style="margin-bottom: 20px;">Select Cleaning Options</h1>

      <div>
        <div v-for="c in checkboxes">
          <v-checkbox
              v-model="c.value"
              :label="c.label"
          ></v-checkbox>
        </div>
      </div>

      <v-text-field
          style=""
          label="How many words do you want to get?"
          v-model="howMany"
          v-on:keyup="enterPressed"
      ></v-text-field>

      <v-btn
          class="continue"
          color="primary"
          @click="isActive"
          :loading="loading"
      >
        SUBMIT
      </v-btn>

    </div>

  </v-layout>
</template>

<script>
  import vueWordCloud from 'vuewordcloud'
  import {mapMutations, mapActions, mapGetters} from 'vuex'

  export default {
    components: {
      vueWordCloud
    },
    data: () => {
      return {
        checkboxes: [
          {label: "Stop Words", value: false},
          {label: "Punctuations", value: false}
        ],
        howMany: 50,
        loading: false
      }
    },
    computed: {
      ...mapGetters({
        STEP_NUMBER: 'STEP_NUMBER',
        WORD_CLOUD: 'WORD_CLOUD',
        UUID: "UUID"
      })
    },
    methods: {
      ...mapMutations({
        POP_WORD_CLOUD: 'POP_WORD_CLOUD',
        SET_READY: 'SET_READY'
      }),
      ...mapActions({}),
      onWordClick(word) {
        this.POP_WORD_CLOUD(word)
      },
      isActive() {
        this.loading = true
        let payload = []
        payload.push(this.UUID)
        let checkboxes = []
        this.checkboxes.forEach(x => {
          if (x.value === true) {
            checkboxes.push(x.label)
          }
        })
        payload.push(checkboxes)
        payload.push(this.howMany)
        this.$store.dispatch("CLEAN_PARAMETERS", payload).then(() => this.loading = false) //TODO: We should get 200 or 404 status responses from action but it does not work
      },
      enterPressed(e) {
        if (e.key === "Enter" && this.howMany) {
          this.isActive()
        }
      },
    }
  }

</script>

<style lang="stylus" scoped>

  .wordCloud {
    width: 80vw;
    height 80vh;
  }

  .checkboxes {
    margin-top: 25vh;
    width: 20vw;
    height 60vh;
    text-align: left;
  }

</style>
