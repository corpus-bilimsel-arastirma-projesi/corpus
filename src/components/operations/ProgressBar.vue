<template>
  <v-layout row justify-center>
    <v-dialog v-model="value" persistent content content-class="centered-dialog">
      <v-container fill-height>
        <v-layout column justify-center align-center>
          <spring-spinner :animation-duration="1500" :size="64" :color="progressColor"/>
          <!--<v-progress-circular indeterminate :size="70" :width="7" :color="progressColor"></v-progress-circular>-->
          <!-- https://epic-spinners.epicmax.co/#/ TODO: You can find bunch of spinner. -->
          <!-- TODO: Also you can use v-dialog with persistent property! -->
          <h1 v-if="message != null">{{message}}</h1>
        </v-layout>
      </v-container>
    </v-dialog>
  </v-layout>
</template>

<script>
  import {
    SpringSpinner
  } from 'epic-spinners'

  export default {
    name: "Loading",
    components: {
      SpringSpinner
    },
    data: () => {
      return {}
    },
    props: {
      value: {type: Boolean, default: false},
      message: {type: String, default: null},
      progressColor: {type: String, default: 'purple'},
    },
  }
</script>

<style>
  .dialog.centered-dialog,
  .v-dialog.centered-dialog {
    background: #282c2dad;
    box-shadow: none;
    border-radius: 6px;
    width: auto;
    color: whitesmoke;
  }
</style>