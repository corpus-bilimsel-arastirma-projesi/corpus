<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-toolbar>
    <v-toolbar-title>Corpus Operations</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">

      <v-btn flat v-on:click="goToHome">Home</v-btn>

      <v-btn flat v-on:click="goToOperations">Operations</v-btn>

      <v-btn v-if="this.$store.getters.JWT" flat v-on:click="goToProfile">Profile</v-btn>

      <v-menu v-else offset-y>
        <template v-slot:activator="{ on }">
          <v-btn
              flat
              v-on="on"
          >
            Sign Up / Sign In
          </v-btn>
        </template>
        <v-list>
          <v-list-tile
              v-for="(item, index) in items"
              :key="index"
              @click="routeToGiven(item.title)"
          >
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>

    </v-toolbar-items>

    <v-menu class="hidden-md-and-up">
      <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
      <v-list>
        <v-list-tile
            v-for="(item, index) in mobileItems"
            :key="index"
            @click="routeToGiven(item.title)">
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-menu>

  </v-toolbar>
</template>

<script>
  import {mapGetters} from "vuex";

  export default {
    data: () => ({
      items: [
        {title: 'Sign Up'},
        {title: 'Sign In'}
      ],
      mobileItems: [
        {title: 'Home'},
        {title: 'Operations'},
        {title: 'Sign Up'},
        {title: 'Sign In'}
      ]
    }),
    methods: {
      ...mapGetters({
        JWT: 'JWT'
      }),
      goToHome() {
        this.$router.replace({path: '/'})
      },
      goToOperations() {
        this.$router.replace({path: '/operations'})
      },
      goToProfile() {
        this.$router.replace({path: '/profile'})
      },
      routeToGiven(title) {
        if (title === 'Sign Up') {
          this.$router.replace({path: 'sign-up'})
        } else if (title === 'Sign In') {
          this.$router.replace({path: 'sign-in'})
        } else if (title === 'Home') {
          this.$router.replace({path: '/'})
        } else if (title === 'Operations') {
          this.$router.replace({path: 'operations'})
        } else if (title === 'Profile') {
          this.$router.replace({path: 'profile'})
        }
      }
    }
  }
</script>

<style>
</style>
