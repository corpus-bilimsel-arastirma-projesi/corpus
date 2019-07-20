<template>
  <v-app>
    <v-layout column>

      <v-flex pt-3 pb-3 xs12>
        <h1 class="text-xs-center">BAPP Project</h1>
      </v-flex>

      <v-carousel>
        <v-carousel-item
            v-for="(item,i) in items"
            :key="i"
            :src="item.src"
        ></v-carousel-item>
      </v-carousel>

    </v-layout>
  </v-app>
</template>

<script>
  import {initSession} from "../session-manager";

  export default {
    data: () => ({
      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg'
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg'
        }
      ]
    }),
    components: {},
    mounted() {
      initSession()
    },
  }
</script>

<style>
</style>
