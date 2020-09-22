<template>
  <div class="container">
    <b-row class="justify-content-lg-center">
      <b-col col lg="8">
        <!-- email 잠금 필요 -->
        <b-form v-if="show">
          <b-form-group
            id="input-group-1"
            label="Email address:"
            label-for="input-1"
            description="We'll never share your email with anyone else.">
            <b-form-input
              id="input-1"
              v-model="form.email"
              type="email"
              required
              placeholder="Enter email"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.name"
              required
              placeholder="Enter name"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Voice:" label-for="input-3">
            <b-form-select
              id="input-3"
              v-model="form.voice"
              :options="voices"
              required
            ></b-form-select>
          </b-form-group>
          <b-button type="submit" variant="info">Submit</b-button>
          <b-button type="reset" variant="danger" class="ml-2">Reset</b-button>
        </b-form>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: "UserInfo",
  data() {
    return {
      form: {
        email: '',
        name: '',
        voice: null,
        checked: [],
      },
      voices: [{ text: 'Select One', value: null }, 'Mama', 'Papa', 'Grandma', 'Grandpa'],
      show: true
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset(evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.name = ''
      this.form.voice = null
      this.form.checked = []
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style>

</style>