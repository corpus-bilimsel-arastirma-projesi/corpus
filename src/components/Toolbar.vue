<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-toolbar>
    <v-toolbar-title>Corpus Operations</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">

      <v-btn flat to="/">Home</v-btn>

      <v-btn v-if="$store.getters.JWT_ACCESS" flat to="/operations">Operations</v-btn>

      <v-btn v-if="$store.getters.JWT_ACCESS" flat to="/profile">Profile</v-btn>

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
              :to="item.link"
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
            v-for="(item, index) in mobileItems($store.getters.JWT_ACCESS)"
            :key="index"
            :to="item.link">
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-menu>

  </v-toolbar>
</template>

<script>

  export default {
    data: () => ({
      items: [
        {title: 'Sign Up', link: '/sign-up'},
        {title: 'Sign In', link: '/sign-in'}
      ],
    }),
    methods: {
      mobileItems(hasToken) {
        return hasToken !== null ? [
          {title: 'Home', link: '/'},
          {title: 'Operations', link: '/operations'},
          {title: 'Profile', link: '/profile'}
        ] : [
          {title: 'Home', link: '/'},
          {title: 'Sign Up', link: '/sign-up'},
          {title: 'Sign In', link: '/sign-in'}
        ]
      }
    }
  }
</script>

<style>
</style>
