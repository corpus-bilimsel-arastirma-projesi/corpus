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
                    :rules="[v => !!v || 'You must agree to continue!']"
                    label="Do you agree?"
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
                    Sign Up
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
  import authenticationService from '@/services/authenticationService' // TODO: Will be used, when it is completed

  export default {
    data: () => ({
      valid: true,
      name: '',
      password: '',
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 6) || 'Password must be greater than 6 characters'
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      checkbox: false
    }),
    methods: {
      validate() {
        if (this.$refs.form.validate()) { // this.$refs.form.validate() && (this.snackbar = true)
          this.snackbar = true
          let payload = []
          payload.push({
            username: this.email,
            password: this.password
          })
          authenticationService.postSignup(payload).then(x => console.log(x))
          console.log('Inside IF')
        }
        console.log('Outside IF')
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
