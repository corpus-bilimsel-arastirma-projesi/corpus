<template>
  <v-container grid-list-md>

    <h1>Profile</h1>

    <v-layout row wrap>
      <v-flex xs12 sm6 md6>

        <v-text-field
            v-model="EMAIL"
            label="Email"
            solo
            disabled
          ></v-text-field>

      </v-flex>

      <v-flex
          xs12
          sm6
          md6
          align-center
          justify-center
          layout
          text-xs-center
      >
        <v-avatar
            :tile="false"
            :size="140"
            color="grey lighten-4"
        >
          <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar">
        </v-avatar>
      </v-flex>
    </v-layout>

    <v-btn
        color="primary"
        @click="logOut">
      Log Out
    </v-btn>

  </v-container>
</template>

<script>
  import {mapActions, mapGetters, mapMutations} from "vuex";

  export default {
    data: () => ({
      email: null
    }),
    computed: {
      ...mapGetters(['EMAIL', 'JWT_ACCESS'])
    },
    methods: {
      ...mapMutations({
        REMOVE_TOKEN: 'REMOVE_TOKEN'
      }),
      ...mapGetters({
        JWT: 'JWT'
      }),
      ...mapActions({
        REFRESH_TOKEN: 'REFRESH_TOKEN',
        INSPECT_TOKEN: 'INSPECT_TOKEN'
      }),
      logOut() {
        this.REMOVE_TOKEN()

        // console.log(`Token is removed as you can see => ${JWT_ACCESS}`)

        this.$router.replace({path: '/sign-in'})

        // this.INSPECT_TOKEN()
      }
    }
  }
</script>

<style>

</style>