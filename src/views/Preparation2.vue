<template>
  <v-app>
    <v-layout row wrap>
      <v-flex xs6>
        <day-month-year style="height: 95%"></day-month-year>
      </v-flex>

      <v-flex xs6>
        <start-word-end-word style="height: 95%"></start-word-end-word>
      </v-flex>

      <v-flex xs6>
        <delete-word style="height: 95%"></delete-word>
      </v-flex>

      <v-flex xs6>
        <delete-contain style="height: 95%"></delete-contain>
      </v-flex>

      <v-flex xs6>
        <delete-beginning style="height: 95%"></delete-beginning>
      </v-flex>

      <v-flex xs6>
        <delete-end style="height: 95%"></delete-end>
      </v-flex>

      <v-flex xs6>
        <replace-word style="height: 95%"></replace-word>
      </v-flex>
    </v-layout>
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