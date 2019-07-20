<template>
  <v-app>

    <v-stepper v-model="e6" vertical>

      <v-stepper-step :complete="e6 > 1" step="1">
        Select Date Time
        <small>Summarize if needed</small>
      </v-stepper-step>
      <v-stepper-content step="1">

        <day-month-year></day-month-year>

        <v-btn color="primary" @click="e6 = 2">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 2" step="2">Choose start word and end word</v-stepper-step>
      <v-stepper-content step="2">

        <start-word-end-word></start-word-end-word>

        <v-btn color="primary" @click="e6 = 3">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 3" step="3">Select an ad format and name ad unit</v-stepper-step>
      <v-stepper-content step="3">

        <delete-word></delete-word>

        <v-btn color="primary" @click="e6 = 4">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 4" step="4">Delete Contain</v-stepper-step>
      <v-stepper-content step="4">

        <delete-contain></delete-contain>

        <v-btn color="primary" @click="e6 = 5">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 5" step="5">Delete Beginning</v-stepper-step>
      <v-stepper-content step="5">

        <delete-beginning></delete-beginning>

        <v-btn color="primary" @click="e6 = 6">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step :complete="e6 > 6" step="6">Delete Word</v-stepper-step>
      <v-stepper-content step="6">

        <delete-end></delete-end>

        <v-btn color="primary" @click="e6 = 7">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>


      <v-stepper-step step="7">Replace Word</v-stepper-step>
      <v-stepper-content step="7">

        <replace-word></replace-word>

        <v-btn color="primary" @click="e6 = 1">Continue</v-btn>
        <v-btn flat>Cancel</v-btn>
      </v-stepper-content>

    </v-stepper>

  </v-app>
</template>

<script>
  import DayMonthYear from '../components/preparation/DayMonthYear'
  import StartWordEndWord from '../components/preparation/StartWordEndWord'
  import DeleteWord from '../components/preparation/DeleteWord'
  import DeleteContain from '../components/preparation/DeleteContain'
  import DeleteBeginning from '../components/preparation/DeleteBeginning'
  import DeleteEnd from '../components/preparation/DeleteEnd'
  import ReplaceWord from '../components/preparation/ReplaceWords'

  export default {
    data() {
      return {
        e6: 1,
        selected: ['Day']
      }
    },
    components: {
      DayMonthYear, StartWordEndWord, DeleteWord, DeleteContain, DeleteBeginning, DeleteEnd, ReplaceWord
    }
  }

</script>

<style scoped>

</style>