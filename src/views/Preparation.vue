<template>
  <v-app>

    <v-stepper v-model="e6" vertical>

      <v-stepper-step :complete="e6 > 1" step="1">
        Select Date Time
        <small>Summarize if needed</small>
      </v-stepper-step>
      <v-stepper-content step="1">

        <add-date-column ref="addDateColumn"></add-date-column>

        <v-btn color="primary" @click="addDateColumn">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 2" step="2">Choose start word and end word</v-stepper-step>
      <v-stepper-content step="2">

        <delete-between ref="deleteBetween"></delete-between>

        <v-btn color="primary" @click="deleteBetween">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 3" step="3">Select an ad format and name ad unit</v-stepper-step>
      <v-stepper-content step="3">

        <delete-word ref="deleteWord"></delete-word>

        <v-btn color="primary" @click="deleteWord">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 4" step="4">Delete Contain</v-stepper-step>
      <v-stepper-content step="4">

        <delete-contain ref="deleteContain"></delete-contain>

        <v-btn color="primary" @click="deleteContain">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 5" step="5">Delete Beginning</v-stepper-step>
      <v-stepper-content step="5">

        <delete-beginning ref="deleteBeginning"></delete-beginning>

        <v-btn color="primary" @click="deleteBeginning">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 6" step="6">Delete Word</v-stepper-step>
      <v-stepper-content step="6">

        <delete-end ref="deleteEnd"></delete-end>

        <v-btn color="primary" @click="deleteEnd">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step step="7">Replace Word</v-stepper-step>
      <v-stepper-content step="7">

        <replace-word ref="replaceWords"></replace-word>

        <v-btn color="primary" @click="replaceWords">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>

    </v-stepper>

  </v-app>
</template>

<script>
  import AddDateColumn from '../components/preparation/AddDateColumn'
  import DeleteBetween from '../components/preparation/DeleteBetween'
  import DeleteWord from '../components/preparation/DeleteWord'
  import DeleteContain from '../components/preparation/DeleteContain'
  import DeleteBeginning from '../components/preparation/DeleteBeginning'
  import DeleteEnd from '../components/preparation/DeleteEnd'
  import ReplaceWord from '../components/preparation/ReplaceWords'

  export default {
    data() {
      return {
        e6: 1
      }
    },
    components: {
      AddDateColumn, DeleteBetween, DeleteWord, DeleteContain, DeleteBeginning, DeleteEnd, ReplaceWord
    },

    methods: {
      addDateColumn() {
        this.e6 = 2
        this.$refs.addDateColumn.addDateColumn()
      },
      deleteBetween() {
        this.e6 = 3
        this.$refs.deleteBetween.deleteBetween()
      },
      deleteWord() {
        this.e6 = 4
        this.$refs.deleteWord.deleteWord()
      },
      deleteContain() {
        this.e6 = 5
        this.$refs.deleteContain.deleteContain()
      },
      deleteBeginning() {
        this.e6 = 6
        this.$refs.deleteBeginning.deleteBeginning()
      },
      deleteEnd() {
        this.e6 = 7
        this.$refs.deleteEnd.deleteEnd()
      },
      replaceWords() {
        this.e6 = 1
        this.$refs.replaceWords.replaceWords()
      }
    }
  }

</script>

<style scoped>

</style>