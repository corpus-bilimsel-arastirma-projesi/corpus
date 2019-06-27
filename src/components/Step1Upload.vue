<template>
  <div id="app">
    <div>

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

    <transition name="fade">
      <v-alert
          v-if="isPreview"
          :value="isPreview"
          type="success"
          dismissible
      >
        Unable to preview chosen file.
      </v-alert>
    </transition>

    <div v-if="USER_FILES.length > 0">
      <br>
      <h1>You can choose file to continue cleaning steps.</h1>

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
                  @click="selectFile(item.title, item.uuid)"
              >
                <v-list-tile-avatar>
                  <v-icon :class="[item.iconClass]">{{ item.icon }}</v-icon>
                </v-list-tile-avatar>

                <v-list-tile-content>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                  <v-list-tile-sub-title>{{ item.subtitle }}</v-list-tile-sub-title>
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

    <!-- Continue with a file -->

    <v-dialog v-model="previewDialog" fullscreen hide-overlay transition="dialog-bottom-transition">

      <progress-bar v-bind:value="previewProgress"
                    v-bind:message="messageProgress"
                    progressColor="#ff1d5e"/>

      <Preview @back-clicked="backCleanGivenFile"
               @continue-clicked="cleanGivenFile"
               v-bind:selectedFileName="selectedFileName"/>

    </v-dialog>

    <!-- Delete a file -->

    <v-layout row justify-center>
      <v-dialog v-model="deleteDialog" persistent max-width="500">
        <v-card>
          <v-card-title class="headline">Do you want to delete given file?</v-card-title>
          <v-card-text>{{ selectedFileName }} is going to be deleted.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click="deleteDialog = false">Back</v-btn>
            <v-btn color="green darken-1" flat @click="deleteGivenFile">Continue</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>

  </div>
</template>

<script>
  import {uuid} from 'vue-uuid'
  import api from '@/services/api'
  import store from '../store/index'
  import vueDropzone from "vue2-dropzone"
  import Preview from '../components/Preview'
  import {mapMutations, mapGetters} from 'vuex'
  import 'vue2-dropzone/dist/vue2Dropzone.min.css'
  import ProgressBar from '../components/ProgressBar'

  export default {
    data: () => ({
      dropOptions: {
        url: api.defaults.baseURL + "/upload/",
        headers: {Authorization: `Bearer ${store.getters.JWT_ACCESS}`},
        maxFilesize: 10, // MB
        maxFiles: 4,
        chunking: false,
        addRemoveLinks: true
      },
      uuid: null,
      isError: false,
      loading: false,
      isSuccess: false,
      isPreview: false,
      deleteDialog: false,
      selectedFileId: null,
      previewDialog: false,
      messageProgress: null,
      selectedFileName: null,
      previewProgress: false
    }),
    components: {
      vueDropzone,
      Preview,
      ProgressBar
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
      },
      sendingEvent(file, xhr, formData) {
        let uuid = this.$uuid.v1()
        this.SET_UUID(uuid)
        formData.append('remark', "Hello World")
        formData.append('uuid', uuid)
        formData.append('jwt', this.$store.getters.JWT_ACCESS)
      },
      async GET_USER_FILES() {
        let status = await this.$store.dispatch('GET_FILE_NAMES_GIVEN_USER', this.$store.getters.EMAIL)
        if (status === 200) {
          console.log(`User is authenticated.`)
        } else if (status === 404) {
          console.log(`User needs to authenticate!!!`)
        }
      },
      async selectFile(title, uuid) {
        this.messageProgress = 'Processing...'
        this.previewProgress = true

        this.selectedFileName = title
        this.uuid = uuid
        this.SET_UUID(uuid)
        let status = await this.$store.dispatch("POST_PREVIEW_SOURCES", uuid)

        if (status === 200) {
          setTimeout(() => {
            this.previewProgress = false
            this.previewDialog = true
          }, 1000)
        } else if (status === 404) {
          this.previewProgress = false
          this.isPreview = true
          setTimeout(() => {
            this.isPreview = false
          }, 5000)
        }
      },
      openDeleteDialog(id, title) {
        this.deleteDialog = true
        this.selectedFileName = title
        this.selectedFileId = id
      },
      async deleteGivenFile() {
        let res = await this.$store.dispatch('DELETE_FILE_GIVEN_USER', this.selectedFileId)

        if (res.success === true) {
          let temp = this.$store.getters.USER_FILES
          temp = temp.filter(x => x.id !== this.selectedFileId)
          this.SET_USER_FILES(temp)
          this.deleteDialog = false
          this.isSuccess = true
          setTimeout(() => {
            this.isSuccess = false
          }, 5000)
        } else {
          this.deleteDialog = false
          this.isError = true
          setTimeout(() => {
            this.isError = false
          }, 5000)
        }
      },
      cleanGivenFile(payload) {
        this.messageProgress = 'Processing...'
        this.previewProgress = true
        this.$store.dispatch("CLEAN_PARAMETERS", payload).then(() => {
          this.$store.commit("SET_STEP_NUMBER", parseInt(this.$store.getters.STEP_NUMBER) + 1)
          this.previewDialog = false
          this.previewProgress = false
        }).catch(() => {
          this.previewDialog = false
          this.previewProgress = false
        })
      },
      backCleanGivenFile(value) {
        // this.loading = value // TODO: If user does not want to wait processing...
        this.previewDialog = value
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
