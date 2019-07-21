<template>
  <v-card class="ma-2 pa-4">

    <v-layout row wrap>
      <h1>The standard Lorem Ipsum passage</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
        laborum.</p>
    </v-layout>

    <v-layout row>
      <v-flex xs4>
        <v-checkbox v-model="selected" label="Day" value="Day"></v-checkbox>
      </v-flex>
      <v-flex xs4>
        <v-checkbox v-model="selected" label="Month" value="Month"></v-checkbox>
      </v-flex>
      <v-flex xs4>
        <v-checkbox v-model="selected" label="Year" value="Year"></v-checkbox>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>

  import {mapActions, mapGetters} from "vuex"

  export default {
    data() {
      return {
        selected: ['Day']
      }
    },

    computed: {
      ...mapGetters({
        FILE_ID: 'FILE_ID'
      })
    },

    methods: {
      ...mapActions({
        ADD_DATE_COLUMN: 'ADD_DATE_COLUMN'
      }),
      async addDateColumn() {
        this.selected.forEach(async date => {
          let response = await this.ADD_DATE_COLUMN({
            date_var: date.toLowerCase(),
            id: 1
          })
          if (response.success === true) {
            // TODO:
          } else {
            // TODO:
          }
        })
      }
    }
  }

</script>