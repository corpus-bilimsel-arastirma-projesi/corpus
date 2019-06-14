<template>
  <v-container column>
    <v-form
        ref="form"
        v-model="valid"
        lazy-validation
    >
      <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
      ></v-text-field>

      <v-text-field
          v-model="password"
          :counter="20"
          type="password"
          :rules="passwordRules"
          label="Password"
          required
      ></v-text-field>

      <v-checkbox
          v-model="checkbox"
          label="Remember me?"
          required
      ></v-checkbox>

      <div>
        <v-btn
            @click="reset"
        >
          Clear
        </v-btn>

        <v-btn
            style="float: right;"
            :disabled="!valid"
            color="success"
            @click="validate"
        >
          Sign In
        </v-btn>

        <v-btn
            v-if="false"
            color="warning"
            @click="resetValidation"
        >
          Reset Validation
        </v-btn>
      </div>
    </v-form>
  </v-container>
</template>

<script>
  import {mapActions} from "vuex";

  export default {
    data: () => ({
      valid: true,
      password: '',
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 5) || 'Password must be greater than 6 characters'
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      checkbox: false
    }),
    methods: {
      ...mapActions({
        OBTAIN_TOKEN: 'OBTAIN_TOKEN',
        SET_EMAIL: 'SET_EMAIL'
      }),
      async validate() {
        if (this.$refs.form.validate()) {
          this.snackbar = true

          let status = await this.OBTAIN_TOKEN({
            username: this.email,
            password: this.password
          })

          if(status === 200) {

            this.$router.push({path: '/profile'})
            this.SET_EMAIL(this.email)

          } else {
            this.reset()
            this.resetValidation() // TODO: Should be modal that says: EMAIL or Password WRONG
          }
        }
      },
      reset() {
        this.$refs.form.reset()
      },
      resetValidation() {
        this.$refs.form.resetValidation()
      }
    }
  }
</script>
