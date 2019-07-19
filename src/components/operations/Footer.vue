<template>
  <v-footer fixed class="pa-3 operation-footer" height="60" flat>
    <v-btn class="operation-button" color="info" v-on:click="continueClick">
      {{buttonName}}
    </v-btn>
  </v-footer>
</template>

<script>

  export default {
    name: "OperationFooter",
    components: {},
    data: () => ({}),
    props: {
      buttonName: {type: String, default: 'Continue'},
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