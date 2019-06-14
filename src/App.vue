<template>
  <v-app>
    <Toolbar/>
    <router-view/>
  </v-app>
</template>

<script>
  import Toolbar from './components/Toolbar'
  import {initSession} from "./session-manager"

  export default {
    components: {
      Toolbar
    },
    name: 'App',
    data() {
      return {}
    },
    mounted() {
      initSession()
    },
  }
</script>

<style scoped>
</style>
