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
            v-model="last"
            label="Delete Beginning"
            outline
        ></v-text-field>
      </v-flex>

    </v-layout>
  </v-card>
</template>

<script>
  export default {
    data: () => ({})
  }
</script>