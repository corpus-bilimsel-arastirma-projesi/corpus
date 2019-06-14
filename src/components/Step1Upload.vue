<template>
  <div id="app">

    <div>
      <!--<vue-dropzone-->
      <!--ref="dropzone"-->
      <!--id="drop1"-->
      <!--:options="dropOptions"-->
      <!--@vdropzone-complete="afterComplete"-->
      <!--v-on:vdropzone-sending="sendingEvent">-->
      <!--</vue-dropzone>-->

      <vue-dropzone
          ref="dropzone"
          id="drop1"
          :options="dropOptions"
          @vdropzone-complete="afterComplete"
          v-on:vdropzone-sending="sendingEvent"
          :useCustomSlot=true>
        <div class="dropzone-custom-content">
          <v-icon color="info" :large="true">cloud_upload</v-icon>
          <h3 class="dropzone-custom-title">Drag and drop to upload content!</h3>
          <div class="subtitle">...or click to select a file from your computer</div>
        </div>
      </vue-dropzone>
    </div>

    <!--<v-btn style="margin-top: 50px;" @click="removeAllFiles">Remove All Files</v-btn>-->

    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <v-card>
          <v-toolbar color="light-blue" dark>
            <v-toolbar-side-icon></v-toolbar-side-icon>

            <v-toolbar-title>My files</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>search</v-icon>
            </v-btn>

          </v-toolbar>

          <v-list two-line subheader>

            <v-list-tile
                v-for="item in USER_FILES"
                :key="item.title"
                avatar
                @click="selectFile(item.title)"
            >
              <v-list-tile-avatar>
                <v-icon :class="[item.iconClass]">{{ item.icon }}</v-icon>
              </v-list-tile-avatar>

              <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                <v-list-tile-sub-title>{{ item.subtitle }}</v-list-tile-sub-title>
              </v-list-tile-content>

              <v-list-tile-action>
                <v-btn v-on:click.stop.prevent="openDeleteDialog(item.title)" icon ripple>
                  <v-icon color="grey lighten-1">delete</v-icon>
                </v-btn>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>

    <!-- Continue with a file -->

    <v-layout row justify-center>
      <v-dialog v-model="dialog" persistent max-width="500">
        <v-card>
          <v-card-title class="headline">Do you want to continue with given file?</v-card-title>
          <v-card-text>{{ selectedFileName }} is going to be used.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click="dialog = false">Back</v-btn>
            <v-btn color="green darken-1" flat @click="dialog = false">Continue</v-btn> <!-- TODO: need endpoint -->
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>

    <!-- Delete a file -->

    <v-layout row justify-center>
      <v-dialog v-model="deleteDialog" persistent max-width="500">
        <v-card>
          <v-card-title class="headline">Do you want to delete given file?</v-card-title>
          <v-card-text>{{ selectedFileName }} is going to be deleted.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click="deleteDialog = false">Back</v-btn>
            <v-btn color="green darken-1" flat @click="deleteGivenFile(selectedFileName)">Continue</v-btn> <!-- TODO: need endpoint -->
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>

  </div>
</template>

<script>
  import vueDropzone from "vue2-dropzone";
  import 'vue2-dropzone/dist/vue2Dropzone.min.css'
  import {uuid} from 'vue-uuid';
  import {mapMutations, mapGetters} from 'vuex'
  import api from '@/services/api'
  import store from '../store/index'

  export default {
    data: () => ({
      dropOptions: {
        url: api.defaults.baseURL + "/upload/",
        headers: {Authorization: `Bearer ${store.getters.JWT_ACCESS}`},
        maxFilesize: 5, // MB
        maxFiles: 4,
        chunking: false,
        addRemoveLinks: true
      },
      dialog: false,
      deleteDialog: false,
      selectedFileName: null
    }),
    components: {
      vueDropzone
    },
    mounted: function () {
      this.GET_USER_FILES()
    },
    computed: mapGetters(['USER_FILES']),
    methods: {
      ...mapMutations({
        SET_READY: 'SET_READY',
        SET_WORD_CLOUD: "SET_WORD_CLOUD",
        SET_JSON_TABLE: "SET_JSON_TABLE",
        SET_JSON_FILE: "SET_JSON_FILE",
        SET_UUID: "SET_UUID",
        SET_USER_FILES: "SET_USER_FILES"
      }),
      removeAllFiles() {
        this.$refs.dropzone.removeAllFiles();
      },
      afterComplete(file) {
        console.log(file);
        console.log(file.status);
        this.GET_USER_FILES()

        let payload = []
        let table = []
        let wordCloud = []
        let temp = 1
        let array = JSON.parse("[" + file.xhr.response + "]");
        array[0].forEach(x => {
          payload.push({key: x[0], value: parseInt(x[1])})
          table.push({number: temp, word: x[0], frequency: parseInt(x[1])})
          wordCloud.push({
            text: x[0],
            weight: parseInt(x[1]),
            rotation: 1,
            rotationUnit: 'turn',
            fontFamily: 'Anton',
            fontStyle: 'italic', // normal|italic|oblique|initial|inherit
            fontVariant: '', // normal|small-caps|initial|inherit
            fontWeight: '', // normal|bold|bolder|lighter|number|initial|inherit
            color: '#' + (Math.random().toString(16) + "000000").substring(2, 8)
          })
          temp = temp + 1
        })
        this.SET_WORD_CLOUD(wordCloud)
        this.SET_JSON_TABLE(table)
        this.SET_JSON_FILE(payload)
        this.SET_READY(true)
      },
      sendingEvent(file, xhr, formData) {
        let uuid = this.$uuid.v1()
        this.SET_UUID(uuid)
        formData.append('remark', "Hello World")
        formData.append('uuid', uuid)
        formData.append('jwt', this.$store.getters.JWT_ACCESS)
      },
      GET_USER_FILES() {
        this.$store.dispatch('GET_FILE_NAMES_GIVEN_USER', this.$store.getters.EMAIL).then()
      },
      selectFile(title) {
        this.dialog = true
        this.selectedFileName = title
      },
      openDeleteDialog(title) {
        this.deleteDialog = true
        this.selectedFileName = title
      },
      deleteGivenFile(title) {
        let temp = this.$store.getters.USER_FILES
        temp = temp.filter(x => x.title !== title)
        this.SET_USER_FILES(temp) // TODO: Need endpoint for backend
        this.deleteDialog = false
      }
    }
  };
</script>

<style scoped>

  #drop1 {
    height: 35vh;
  }

  #app {
    height: 100vh;
  }

  .dropzone-custom-content {
    margin-top: 13vh;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .dropzone-custom-title {
    margin-top: 0;
    color: #00b782;
  }

  .subtitle {
    color: #314b5f;
  }

</style>
