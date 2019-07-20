<template>
  <v-app>

    <!-- Content -->

    <v-layout column>
      <div class="container">
        <h1 style="display: flex; justify-content: center;">UPLOAD JSON FILE</h1>
        <files
            :is-error="isError"
            :is-success="isSuccess"
            @start-column-mapping="processColumnMapping"
            @delete-file-modal="openDeleteFileModal"
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

    <!-- Column Mapping -->

    <v-dialog v-model="columnMappingDialog" persistent max-width="800px">
      <v-card>
        <v-card-title>
          <span class="headline">Column Mapping</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-layout row wrap>

              <v-layout
                  v-for="(column, index) in definedColumns"
                  :key="index">

                <v-flex xs12 sm6 mr-2>
                  <v-text-field v-bind:value="column.toUpperCase()" solo readonly></v-text-field>
                </v-flex>
                <v-flex xs12 sm6>
                  <v-select
                      :items="userDefinedColumns"
                      label="Choose..."
                      required
                      @input="event => temp[index] = event"
                  ></v-select>
                </v-flex>

              </v-layout>

            </v-layout>

            <v-btn v-on:click="show">SHOW</v-btn>

          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="columnMappingDialog = false">Close</v-btn>
          <v-btn color="blue darken-1" flat @click="doColumnMapping">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-app>
</template>

<script>
  import Files from '../components/Files'
  import {mapGetters, mapActions} from 'vuex'
  import {initSession} from '../session-manager'
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
        columnMappingDialog: false,
        definedColumns: ['content', 'date', 'docid', 'source', 'title'],
        userDefinedColumns: [],
        temp: []
      }
    },
    computed: {
      ...mapGetters({
        USER_FILES: 'USER_FILES'
      }),
    },
    mounted() {
      initSession()
      this.GET_USER_FILES()
    },
    methods: {
      ...mapActions({
        CONCAT_FILES: 'CONCAT_FILES',
        GET_COLUMN_NAMES: 'GET_COLUMN_NAMES',
        POST_COLUMN_MAPPING: 'POST_COLUMN_MAPPING',
        GET_PREVIEW_SOURCES: 'GET_PREVIEW_SOURCES',
        DELETE_FILE_GIVEN_USER: 'DELETE_FILE_GIVEN_USER',
        GET_FILE_NAMES_GIVEN_USER: 'GET_FILE_NAMES_GIVEN_USER',
      }),
      async GET_USER_FILES() {
        let status = await this.GET_FILE_NAMES_GIVEN_USER(this.$store.getters.EMAIL)
        if (status === 200) {
          console.log(`User is authenticated.`)
        } else if (status === 404) {
          console.log(`User needs to authenticate!!!`)
        }
      },
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
      async continueClick() {
        let files = this.USER_FILES.filter(x => x.checkbox === true)

        let notReadyFiles = files.filter(x => x.isReady === false)

        if (notReadyFiles.length === 1) {
          let data = await this.GET_COLUMN_NAMES(notReadyFiles[0].id)

          this.idof = notReadyFiles[0].id

          this.userDefinedColumns = data.columns

          this.columnMappingDialog = true

        } else {
          if (files.length === 1) {
            this.goNextPage(files[0].id)
          } else if (files.length > 1) {
            this.mergeFileModal = true
            this.mergeFilesIds = files.map(file => file.id)
            this.mergeFileNames = files.map(file => file.title)
          }
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

      },
      processColumnMapping(response) {
        console.log(response)
        this.GET_USER_FILES()
      },
      async doColumnMapping() {

        let data = await this.$store.dispatch('POST_COLUMN_MAPPING', [...this.temp, this.idof])

        console.log(data)
      },
      show() {
        console.log(this.temp)
      }
    }
  }
</script>

<style lang="stylus" scoped>

</style>
