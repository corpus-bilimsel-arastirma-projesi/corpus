<template>
  <v-app>
    <Toolbar />
    <router-view/>
  </v-app>
</template>

<script>
  import Toolbar from './components/Toolbar'

  export default {
    components: {
      Toolbar
    },
    name: 'App',
    data() {
      return {
      }
    }
  }
</script>

<style scoped>
</style>
