<template>
  <div id="app">

    <drag-and-drop
        id="drop1"
        :dropOptions="dropOptions"
        @column-mapping="startColumnMapping"
    ></drag-and-drop>

    <!-- Error deleting file -->

    <transition name="fade">
      <v-alert
          v-if="isError"
          :value="isError"
          type="error"
          dismissible
      >
        There has been an error, when deleting given file.
      </v-alert>
    </transition>

    <!-- Success deleting file -->

    <transition name="fade">
      <v-alert
          v-if="isSuccess"
          :value="isSuccess"
          type="success"
          dismissible
      >
        You have successfully removed given file.
      </v-alert>
    </transition>

    <div v-if="USER_FILES.length > 0">
      <br>
      <h1 style="display: flex; justify-content: center;">You choose files to continue cleaning steps</h1>

      <v-layout row>
        <v-flex xs12 my-3>
          <v-card>
            <v-toolbar color="light-blue" dark>

              <v-toolbar-title>My files</v-toolbar-title>

            </v-toolbar>

            <v-list two-line subheader>

              <v-list-tile
                  v-for="item in USER_FILES"
                  :key="item.title"
                  avatar
                  @click="selectFile(item.title)"
              >
                <v-list-tile>

                  <v-checkbox
                      :value="item.checkbox"
                  ></v-checkbox>

                </v-list-tile>

                <v-list-tile-avatar>
                  <v-icon :class="[item.iconClass]">{{ item.icon }}</v-icon>
                </v-list-tile-avatar>

                <v-list-tile-content>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                  <v-list-tile-sub-title>{{ item.date }}</v-list-tile-sub-title>
                </v-list-tile-content>

                <v-list-tile-action>

                  <v-btn v-on:click.stop.prevent="openDeleteDialog(item.id, item.title)" icon ripple>
                    <v-icon color="grey lighten-1">delete</v-icon>
                  </v-btn>

                </v-list-tile-action>

              </v-list-tile>
            </v-list>
          </v-card>
        </v-flex>
      </v-layout>
    </div>

  </div>
</template>

<script>
  import {mapGetters} from 'vuex'
  import api from '@/services/api'
  import store from '../store/index'
  import DragAndDrop from './operations/DragAndDrop'

  export default {
    name: 'Upload',
    props: {
      isError: Boolean,
      isSuccess: Boolean
    },
    data: () => ({
      dropOptions: {
        url: api.defaults.baseURL + "/file/upload/",
        headers: {Authorization: `Bearer ${store.getters.JWT_ACCESS}`},
        maxFilesize: 10, // MB
        maxFiles: 4,
        chunking: false,
        addRemoveLinks: true
      }
    }),
    components: {
      DragAndDrop
    },
    computed: mapGetters(['USER_FILES']),
    methods: {
      selectFile(title) {
        this.USER_FILES.forEach(x => x.title === title && (x.checkbox = !x.checkbox))

        for (let i = 0; i < this.USER_FILES.length; i++) {
          if(this.USER_FILES[i].checkbox === true) {
            this.$store.commit('SET_IS_READY', true)
            break
          } else {
            this.$store.commit('SET_IS_READY', false)
          }
        }
      },
      openDeleteDialog(id, title) {
        this.$emit("delete-file-modal", id, title)
      },
      startColumnMapping(response) {
        this.$emit('start-column-mapping', response)
      }
    }
  }
</script>

<style scoped>

  #drop1 {
    height: 35vh;
  }

</style>
