<template>
  <div class="text-xs-center">
    <transition name="fade">
      <v-alert
          v-if="isAlert"
          :value="isAlert"
          type="success"
          dismissible
      >
        You have succesfully copied to clipboard.
      </v-alert>
    </transition>
    <v-textarea
        id="code-field"
        v-on:click="copyTestingCode"
        height="500"
        v-bind:readonly="true"
        outline
        name="input-7-4"
        label="Data (Click and copy to clipboard)"
        :value="beautifyJSON()"
    ></v-textarea>
    <h1>You can download as</h1>
    <v-radio-group row style="display: inline-block;" v-model="fileType" >
      <v-radio label="txt" value="txt"></v-radio>
      <v-radio label="json" value="json"></v-radio>
      <v-radio label="csv" value="csv"></v-radio>
      <v-radio label="xls" value="xls"></v-radio>
    </v-radio-group>
    <br>
    <v-btn color="success" v-on:click="downloadJsonFile">
      <i style="font-size: large" class="mr-2 fas fa-download"></i>
      Download
    </v-btn>
    <br><br><br><br><br>

  </div>
</template>

<script>
  import exportFromJSON from 'export-from-json'
  import {mapGetters} from 'vuex'

  export default {
    data: () => {
      return {
        isAlert: false,
        fileType: 'txt',
      }
    },
    methods: {
      copyTestingCode() {
        let testingCodeToCopy = document.querySelector('#code-field')
        testingCodeToCopy.setAttribute('type', 'text')
        testingCodeToCopy.select()

        try {
          document.execCommand('copy');
          this.isAlert = true
        } catch (err) {
        }

        testingCodeToCopy.setAttribute('type', 'text')
        window.getSelection().removeAllRanges()
        setTimeout(() => {
          this.isAlert = false
        }, 5000)
      },
      beautifyJSON() {
        const data = this.JSON_TABLE
        const fileName = 'data'
        const exportType = 'txt'

        return exportFromJSON({
          data,
          fileName,
          exportType,
          processor(content, type, fileName) {
            return content
          }
        })
      },
      downloadJsonFile() {
        const data = this.JSON_TABLE
        const fileName = 'data'
        const exportType = this.fileType

        exportFromJSON({data, fileName, exportType})
      }
    },
    computed: {
      ...mapGetters({
        JSON_TABLE: 'JSON_TABLE',
      })
    },
  }
</script>

<style>

  .fade-enter-active, .fade-leave-active {
    transition: opacity 1s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  {
    opacity: 0;
  }

</style>
