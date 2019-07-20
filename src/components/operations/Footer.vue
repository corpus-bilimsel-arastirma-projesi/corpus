<template>
  <v-footer fixed class="pa-3 operation-footer" height="60" flat>
    <v-btn :disabled="!IS_READY" class="operation-button" color="info" v-on:click="continueClick">
      {{buttonName}}
    </v-btn>
  </v-footer>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: "OperationFooter",
    components: {},
    data: () => ({}),
    props: {
      buttonName: {type: String, default: 'Continue'},
    },
    computed: {
      ...mapGetters({
        IS_READY: 'IS_READY'
      })
    },
    methods: {
      continueClick() {
        this.$emit('continue-click')
      }
    }
  }

</script>

<style scoped>

  .operation-footer {
    display: flex;
    justify-content: center;
  }

  .operation-button {
    width: 50%;
  }

</style>