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
        ></files>
      </div>
    </v-layout>

    <!-- Footer -->

    <operation-footer
        @continue-click="continueClick"
        button-name="Continue"
    ></operation-footer>

    <!-- DIALOGS: OUT OF PAGE -->

    <!-- Progress Bar -->

    <progress-bar v-bind:value="previewProgress"
                  v-bind:message="messageProgress"
                  progressColor="#ff1d5e"
    ></progress-bar>

    <!-- Merge Files Modal -->

    <v-layout row justify-center>
      <v-dialog v-model="mergeFileModal" persistent max-width="500">
        <v-card>
          <v-card-title class="headline">Do you want to merge given files?</v-card-title>
          <v-card-text>Following files will be merged</v-card-text>
          <pre>{{ mergeFileNames }}</pre>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click="mergeFileModal = false">Back</v-btn>
            <v-btn color="red darken-1" style="color: white;" @click="mergeFile">Merge Files</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>

    <!-- Delete File Modal -->

    <v-layout row justify-center>
      <v-dialog v-model="deleteFileModal" persistent max-width="500">
        <v-card>
          <v-card-title class="headline">Do you want to delete given file?</v-card-title>
          <v-card-text>{{ deleteFileName }} is going to be deleted.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click="deleteFileModal = false">Back</v-btn>
            <v-btn color="red darken-1" style="color: white;" @click="deleteFile">Continue</v-btn>
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
  import OperationFooter from '../components/operations/Footer'
  import ProgressBar from '../components/operations/ProgressBar'

  export default {
    components: {
      Files, ProgressBar, OperationFooter
    },
    data() {
      return {
        fileId: null,
        deleteFileName: null,
        isError: false,
        isSuccess: false,
        mergeFilesIds: null,
        mergeFileNames: null,
        messageProgress: null,
        mergeFileModal: false,
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
        CONCAT_FILES: 'CONCAT_FILES',
        GET_PREVIEW_SOURCES: 'GET_PREVIEW_SOURCES',
        DELETE_FILE_GIVEN_USER: 'DELETE_FILE_GIVEN_USER',
        GET_FILE_NAMES_GIVEN_USER: 'GET_FILE_NAMES_GIVEN_USER',
      }),
      openDeleteFileModal(id, name) {
        this.fileId = id
        this.deleteFileName = name
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
      continueClick() {
        let files = this.USER_FILES.filter(x => x.checkbox === true)

        if (files.length === 1) {
          this.goNextPage(files[0].id)
        } else if (files.length > 1) {
          this.mergeFileModal = true
          this.mergeFilesIds = files.map(file => file.id)
          this.mergeFileNames = files.map(file => file.title)
        }
      },
      async mergeFile() {
        this.mergeFileModal = false
        this.messageProgress = 'Processing...'
        this.previewProgress = true

        let payload = [this.mergeFilesIds, this.mergeFileNames]

        let response = await this.CONCAT_FILES(payload)

        if (response.success === true) {
          let status = await this.GET_FILE_NAMES_GIVEN_USER(this.$store.getters.EMAIL)
          if (status === 200) {
            this.previewProgress = false
            console.log(`User is authenticated.`) // TODO: Make decision
          } else if (status === 404) {
            this.previewProgress = false
            console.log(`User needs to authenticate!!!`)
          }
        }
      },
      async goNextPage(id) {
        this.messageProgress = 'Processing...'
        this.previewProgress = true

        let status = await this.GET_PREVIEW_SOURCES(id)

        if (status === 200) {
          this.previewProgress = false
          this.$router.push({path: '/plotly'})
        } else {
          setTimeout(() => this.previewProgress = false, 2000) // TODO: Falsy
        }

      }
    }
  }
</script>

<style lang="stylus" scoped>

</style>
