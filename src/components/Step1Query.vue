<template>
  <div id="app">
    <v-container fluid grid-list-md>
      <v-layout row wrap>
        <v-flex offset-md4 md4>
          <v-layout id="query" column>

            <v-combobox
                v-model="state"
                label="Query"
                :items="states"
                v-on:keyup="enterPressed"
                @input.native="debounce"
            ></v-combobox>

            <div v-for="t in texts">
              <v-text-field
                  v-if="t.bool"
                  v-bind:value="t.text"
                  @click:clear="t.bool = false"
                  readonly
                  single-line
                  solo
                  clearable>
              </v-text-field>
            </div>

            <v-btn color="info">Query from Database</v-btn>

          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  export default {
    data: () => {
      return {
        texts: [],
        state: null,
        states: []
      }
    },
    computed: {},
    components: {},
    methods: {
      enterPressed(e) {
        if (e.key === "Enter" && this.state) {
          this.texts.push({text: this.state, bool: true})
          this.state = null
          this.states = []
        }
      },
      debounce(event) {
        if (event.target.value.length > 1) {
          this.$store.dispatch('QUERY_DATABASE', event.target.value).then(x => this.states = x)
        }
      },
    }
  };
</script>

<style lang="stylus" scoped>

  #app {
    height: 100vh;
  }

  #query {
    margin-top: 5vh;
  }

</style>
