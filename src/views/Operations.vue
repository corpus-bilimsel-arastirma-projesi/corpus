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
            <v-btn color="red darken-1" style="color: white;" v-on:click="deleteFile">Continue</v-btn>
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
                  :key="index"
                  v-for="(column, index) in definedColumns">
                <v-flex xs12 sm6 mr-2>
                  <v-text-field v-bind:value="column.toUpperCase()" solo readonly></v-text-field>
                </v-flex>
                <v-flex xs12 sm6>
                  <v-select
                      :items="userDefinedColumns"
                      label="Choose..."
                      required
                      @input="value => mappedColumns[column] = value"
                  ></v-select>
                </v-flex>
              </v-layout>
            </v-layout>
          </v-container>
          <small>*fill the blanks</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="columnMappingDialog = false">CLOSE</v-btn>
          <v-btn color="green darken-1" style="color: white;" v-on:click="doColumnMapping">SUBMIT</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Warning Column Mapping Need Before Merging -->

    <v-layout row justify-center>
      <v-dialog v-model="errorMergeDialog" persistent max-width="500">
        <v-card>
          <v-card-title class="headline">WARNING</v-card-title>
          <v-card-text>Following files need to be column mapping, before merging!</v-card-text>
          <pre>{{ mergeFileNames }}</pre>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" style="color: white;" @click="errorMergeDialog = false">OKAY</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>

  </v-app>
</template>

<script>
  import Files from '../components/Files'
  import {initSession} from '../session-manager'
  import {mapGetters, mapActions, mapMutations} from 'vuex'
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
        errorMergeDialog: false,
        columnMappingDialog: false,
        definedColumns: ['content', 'date', 'docid', 'source', 'title'],
        userDefinedColumns: [],
        mappedColumns: {}
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
      ...mapMutations({
        SET_FILE_ID: 'SET_FILE_ID'
      }),
      ...mapActions({
        CONCAT_FILES: 'CONCAT_FILES',
        GET_COLUMN_NAMES: 'GET_COLUMN_NAMES',
        POST_COLUMN_MAPPING: 'POST_COLUMN_MAPPING',
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

        if (notReadyFiles.length === 0) {

          if (files.length === 1) {
            this.goNextPage(files[0].id)
          } else if (files.length > 1) {
            this.mergeFileModal = true
            this.mergeFilesIds = files.map(file => file.id)
            this.mergeFileNames = files.map(file => file.title)
          }

        } else if (notReadyFiles.length === 1 && !(files.length > 1)) {
          let file = notReadyFiles[0]
          let response = await this.GET_COLUMN_NAMES(file.id)

          if (response.success === true) {
            this.columnMappingFileId = file.id
            this.userDefinedColumns = response.columns
            this.columnMappingDialog = true
          } else {
            // TODO: WHEN COLUMNS NOT AVAILABLE
          }

        } else {
          this.mergeFileNames = notReadyFiles.map(file => file.title)
          this.errorMergeDialog = true
        }
      },
      async mergeFile() {
        this.mergeFileModal = false
        this.messageProgress = 'Processing...'
        this.previewProgress = true

        let response = await this.CONCAT_FILES([this.mergeFilesIds, this.mergeFileNames])

        if (response.success === true) {
          this.GET_USER_FILES()
          this.previewProgress = false
        } else {
          // TODO: WHEN SOMETHING WRONG ON MERGING PROCESS
        }
      },
      async goNextPage(id) {
        this.messageProgress = 'Processing...'
        this.previewProgress = true

        this.SET_FILE_ID(id)
        this.previewProgress = false
        this.$router.push({path: '/preparation'})
      },
      processColumnMapping(response) {
        console.log(response)
        this.GET_USER_FILES()
      },
      async doColumnMapping() {
        let response = await this.$store.dispatch('POST_COLUMN_MAPPING', {
          columns: this.mappedColumns,
          id: this.columnMappingFileId
        })

        if (response.success === true) {
          this.GET_USER_FILES()
          this.userDefinedColumns = []
          this.columnMappingDialog = false
        } else {
          // TODO: WHEN SOMETHING WRONG ON COLUMN MAPPING PROCESS
        }

      }
    }
  }
</script>

<style lang="stylus" scoped>

</style>
