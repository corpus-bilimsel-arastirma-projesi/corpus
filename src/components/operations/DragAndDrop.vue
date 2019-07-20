<template>
  <drop
      ref="drop"
      id="operation-drag-drop"
      :options="dropOptions"
      @vdropzone-complete="afterComplete"
      v-on:vdropzone-sending="sendingEvent"
      :useCustomSlot=true>
    <div class="custom-content">
      <v-icon color="info" :large="true">cloud_upload</v-icon>
      <h3 class="custom-title">Drag and drop to upload content!</h3>
      <div class="subtitle">...or click to select a file from your computer</div>
    </div>
  </drop>
</template>

<script>
  import drop from 'vue2-dropzone'
  import 'vue2-dropzone/dist/vue2Dropzone.min.css'
  import {mapGetters} from 'vuex'

  export default {
    name: 'Uploader',
    props: {
      dropOptions: Object,
    },
    components: {
      drop
    },
    computed: {
      ...mapGetters({
        JWT_ACCESS: 'JWT_ACCESS'
      })
    },
    methods: {
      afterComplete(response) {
        this.$emit('column-mapping', response)
      },
      sendingEvent(file, xhr, formData) {
        formData.append('file_name', file.name)
        formData.append('jwt', this.JWT_ACCESS)
      },
      removeAllFiles() {
        this.$refs.drop.removeAllFiles()
      },
    }
  }

</script>

<style scoped>

  .custom-content {
    margin-top: 13vh;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .custom-title {
    margin-top: 0;
    color: #00b782;
  }

  .subtitle {
    color: #314b5f;
  }

</style>
