<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-app>
    <v-layout column>

      <v-jumbotron
          :gradient="gradient"
          dark
          src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
      >
        <v-container fill-height>
          <v-layout align-center>
            <v-flex text-xs-center>
              <h3 class="display-3">Welcome to Corpus Operations</h3>
            </v-flex>
          </v-layout>
        </v-container>
      </v-jumbotron>

      <v-timeline class="timeline">
        <v-timeline-item
            v-for="(year, i) in years"
            :key="i"
            :color="year.color"
            small
        >
          <template v-slot:opposite>
        <span
            :class="`headline font-weight-bold ${year.color}--text`"
            v-text="year.year"
        ></span>
          </template>
          <div class="py-3">
            <h2 :class="`headline font-weight-light mb-3 ${year.color}--text`">Lorem ipsum</h2>
            <div>
              Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando
              voluptatibus, vix an salutandi sententiae.
            </div>
          </div>
        </v-timeline-item>
      </v-timeline>

      <div class="network">
        <d3-network
            :net-nodes="nodes"
            nodeLabels="false"
            :net-links="links"
            :options="options">
        </d3-network>
      </div>
    </v-layout>
  </v-app>
</template>

<script>
  import D3Network from 'vue-d3-network'

  export default {
    data: () => ({
      gradient: 'to top right, rgba(63,81,181, .7), rgba(25,32,72, .7)',
      years: [
        {
          color: 'cyan',
          year: '1960'
        },
        {
          color: 'green',
          year: '1970'
        },
        {
          color: 'pink',
          year: '1980'
        },
        {
          color: 'amber',
          year: '1990'
        },
        {
          color: 'orange',
          year: '2000'
        }
      ],
      nodes: [
        {id: 1, name: 'my node 1', _color: '#653D5B'},
        {id: 2, name: 'my node 2', _color: '#653D5B'},
        {id: 3, _color: '#653D5B'},
        {id: 4, _color: '#653D5B'},
        {id: 5, _color: '#653D5B'},
        {id: 6, _color: '#653D5B'},
        {id: 7, _color: '#653D5B'},
        {id: 8, _color: '#653D5B'},
        {id: 9, _color: '#653D5B'},
        {id: 10, _color: '#653D5B'},
        {id: 11, _color: '#653D5B'},
        {id: 12, _color: '#653D5B'},
        {id: 13, _color: '#653D5B'},
        {id: 14, _color: '#653D5B'},
        {id: 15, _color: '#653D5B'}
      ],
      links: [
        {sid: 1, tid: 2, _color: 'black'},
        {sid: 2, tid: 3, _color: 'black'},
        {sid: 3, tid: 4, _color: 'black'},
        {sid: 4, tid: 5, _color: 'black'},
        {sid: 5, tid: 6, _color: 'black'},
        {sid: 6, tid: 7, _color: 'black'},
        {sid: 7, tid: 8, _color: 'black'},
        {sid: 8, tid: 9, _color: 'black'},
        {sid: 9, tid: 10, _color: 'black'},
        {sid: 10, tid: 11, _color: 'black'},
        {sid: 11, tid: 12, _color: 'black'},
        {sid: 12, tid: 13, _color: 'black'},
        {sid: 13, tid: 14, _color: 'black'},
        {sid: 14, tid: 15, _color: 'black'},
        {sid: 15, tid: 1, _color: 'black'}
      ],
      options:
          {
            force: 3000,
            nodeSize: 50,
            nodeLabels: false,
            linkWidth: 20
          }
    }),
    components: {
      D3Network
    }
  }
</script>

<style>

  .timeline {
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column;
    left: 5%;
    width: 90vw;
  }

  .network {
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column;

  }

</style>
