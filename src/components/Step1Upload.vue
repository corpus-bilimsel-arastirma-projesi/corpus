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

  </div>
</template>

<script>
  import vueDropzone from "vue2-dropzone";
  import 'vue2-dropzone/dist/vue2Dropzone.min.css'
  import { uuid } from 'vue-uuid';
  import {mapMutations} from 'vuex'

  export default {
    data: () => ({
      dropOptions: {
        url: "https://corpuslive.herokuapp.com/api/upload/",
        maxFilesize: 5, // MB
        maxFiles: 4,
        chunking: false,
        addRemoveLinks: true,
        // init: function() {
        //   this.on("addedfile", function(file) { this.sendFileTubi(file); });
        // }
      }
    }),
    components: {
      vueDropzone
    },
    methods: {
      ...mapMutations({
        SET_READY: 'SET_READY',
        SET_WORD_CLOUD: "SET_WORD_CLOUD",
        SET_JSON_TABLE: "SET_JSON_TABLE",
        SET_JSON_FILE: "SET_JSON_FILE",
        SET_UUID: "SET_UUID"
      }),
      removeAllFiles() {
        this.$refs.dropzone.removeAllFiles();
      },
      afterComplete(file) {
        console.log(file);
        console.log(file.status);

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
