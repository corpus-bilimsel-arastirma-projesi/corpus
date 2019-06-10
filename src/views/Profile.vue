<template>
  <div>
    <h1>Profile</h1>

    <v-btn
        color="primary"
        @click="logOut">
      Log Out
    </v-btn>
  </div>
</template>

<script>
  import {mapGetters, mapMutations} from "vuex";

  export default {
    data() {
      return {}
    },
    methods: {
      ...mapMutations({
        REMOVE_TOKEN: 'REMOVE_TOKEN'
      }),
      ...mapGetters({
        JWT: 'JWT'
      }),
      logOut() {
        this.REMOVE_TOKEN()

        console.log(`Token is removed as you can see => ${this.$store.getters.JWT}`)

        this.$router.push({path: '/sign-in'})
      }
    }
  }
</script>

<style>

</style>