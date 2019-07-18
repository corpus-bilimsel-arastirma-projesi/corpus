<template>
  <v-app>

    <!-- Content -->

    <v-layout column>
      <div class="container">
        <h1 style="display: flex; justify-content: center;">UPLOAD JSON FILE</h1>
        <files
            @delete-file-modal="openDeleteFileModal"
            :is-error="isError"
            :is-success="isSuccess"
        >
        </files>
      </div>
    </v-layout>

    <!-- Footer -->

    <v-footer fixed class="pa-3" height="60" flat style="display: flex; justify-content: center;">
      <v-btn color="info" style="width: 50%;" v-on:click="goNextPage">
        CONTINUE
      </v-btn>
    </v-footer>

    <!-- DIALOGS: OUT OF PAGE -->

    <!-- Progress Bar -->

    <progress-bar v-bind:value="previewProgress"
                  v-bind:message="messageProgress"
                  progressColor="#ff1d5e"
    ></progress-bar>

    <!-- Delete File Modal -->

    <v-layout row justify-center>
      <v-dialog v-model="deleteFileModal" persistent max-width="500">
        <v-card>
          <v-card-title class="headline">Do you want to delete given file?</v-card-title>
          <v-card-text>{{ fileName }} is going to be deleted.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click="deleteFileModal = false">Back</v-btn>
            <v-btn color="green darken-1" flat @click="deleteFile">Continue</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>

  </v-app>
</template>

<script>
  import Files from '../components/Files'
  import {mapGetters, mapActions} from 'vuex'
  import {initSession} from "../session-manager"
  import ProgressBar from '../components/operations/ProgressBar'

  export default {
    components: {
      Files, ProgressBar
    },
    data() {
      return {
        fileId: null,
        fileName: null,
        isError: false,
        isSuccess: false,
        messageProgress: null,
        deleteFileModal: false,
        previewProgress: false,
      }
    },
    computed: {
      ...mapGetters({
        USER_FILES: 'USER_FILES'
      }),
    },
    mounted() {
      initSession()
    },
    methods: {
      ...mapActions({
        GET_PREVIEW_SOURCES: 'GET_PREVIEW_SOURCES',
        DELETE_FILE_GIVEN_USER: 'DELETE_FILE_GIVEN_USER',
        GET_FILE_NAMES_GIVEN_USER: 'GET_FILE_NAMES_GIVEN_USER',
      }),
      openDeleteFileModal(id, name) {
        this.fileId = id
        this.fileName = name
        this.deleteFileModal = true
      },
      async deleteFile() {
        let res = await this.DELETE_FILE_GIVEN_USER(this.fileId)

        if (res.success === true) {

          let status = await this.GET_FILE_NAMES_GIVEN_USER(this.$store.getters.EMAIL)
          if (status === 200) {
            console.log(`User is authenticated.`) // TODO: Make decision
          } else if (status === 404) {
            console.log(`User needs to authenticate!!!`)
          }

          this.deleteFileModal = false

          this.isSuccess = true
          setTimeout(() => this.isSuccess = false, 5000)

        } else {
          this.deleteFileModal = false

          this.isError = true
          setTimeout(() => this.isError = false, 5000)

        }
      },
      async goNextPage() {
        this.messageProgress = 'Processing...'
        this.previewProgress = true

        let files = this.USER_FILES.filter(x => x.checkbox === true)

        if (files.length > 0) {
          let status = await this.GET_PREVIEW_SOURCES(files[0].uuid)

          if (status === 200) {
            this.previewProgress = false
            this.$router.push({path: '/plotly'})
          } else {
            setTimeout(() => this.previewProgress = false, 2000) // TODO: Falsy
          }
        } else {
          setTimeout(() => this.previewProgress = false, 2000) // TODO: Falsy
        }
      }
    }
  }
</script>

<style lang="stylus" scoped>

</style>
