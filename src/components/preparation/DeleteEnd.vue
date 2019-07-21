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

      <v-flex xs12 sm12 class="ml-2">
        <v-text-field
            v-model="end"
            label="Delete End"
            outline
        ></v-text-field>
      </v-flex>

    </v-layout>


    <v-layout row>
      <v-select
          :items="COLUMNS"
          label="Choose..."
          required
          @input="value => column = value"
      ></v-select>
    </v-layout>

  </v-card>
</template>

<script>
  import {mapActions, mapGetters} from "vuex"

  export default {
    data: () => ({
      end: null,
      column: null
    }),

    computed: {
      ...mapGetters({
        FILE_ID: 'FILE_ID',
        COLUMNS: 'COLUMNS'
      })
    },

    methods: {
      ...mapActions({
        DELETE_END: 'DELETE_END'
      }),
      async deleteEnd() {
        let response = await this.DELETE_END({
          end: this.end,
          id: this.FILE_ID,
          column: this.column
        })
        if (response.success === true) {
          // TODO:
        } else {
          // TODO:
        }
      }
    }
  }
</script>