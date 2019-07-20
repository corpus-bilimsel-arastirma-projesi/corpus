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
            :items="items"
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
            v-model="last"
            label="Replace Word"
            outline
        ></v-text-field>
      </v-flex>

    </v-layout>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      chips: ['aRtificial', 'ArTificial', 'artifiCialll', 'artificiaL'],
      // items: ['Streaming', 'Eating']
    }),

    methods: {
      remove(item) {
        this.chips.splice(this.chips.indexOf(item), 1)
        this.chips = [...this.chips]
      }
    }
  }
</script>