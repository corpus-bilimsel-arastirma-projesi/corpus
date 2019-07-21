<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-card class="ma-2 pa-4">

    <v-layout row wrap>
      <h1>The standard Lorem Ipsum passage</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
        laborum.</p>
    </v-layout>

    <v-layout row wrap>

      <v-flex xs12 sm12>
        <v-combobox
            v-model="chips"
            label="Your favorite hobbies"
            chips
            clearable
            prepend-icon="filter_list"
            solo
            multiple
        >
          <template v-slot:selection="data">
            <v-chip
                :selected="data.selected"
                close
                @input="remove(data.item)"
                color="red"
                text-color="white"
            >
              <strong>{{ data.item }}</strong>&nbsp;
              <!--<span>(interest)</span>-->
            </v-chip>
          </template>
        </v-combobox>
      </v-flex>

      <v-flex xs12 sm12 class="ml-2">
        <v-text-field
            v-model="targetWord"
            label="Replace Word"
            outline
        ></v-text-field>
      </v-flex>

    </v-layout>
  </v-card>
</template>

<script>
  import {mapActions, mapGetters} from "vuex"

  export default {
    data: () => ({
      targetWord: null,
      chips: ['aRtificial', 'ArTificial', 'artifiCialll', 'artificiaL'],
    }),

    computed: {
      ...mapGetters({
        FILE_ID: 'FILE_ID'
      })
    },

    methods: {
      ...mapActions({
        REPLACE_WORDS: 'REPLACE_WORDS'
      }),
      remove(item) {
        this.chips.splice(this.chips.indexOf(item), 1)
        this.chips = [...this.chips]
      },
      async replaceWords() {
        let response = await this.REPLACE_WORDS({
          word_list: this.chips,
          target_word: this.targetWord,
          id: 1
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