<template>
  <div v-if="userInfo" class="container">
    <b-row class="justify-content-lg-center">
      <b-col col lg="8">
        <!-- email 잠금 필요 -->
        <b-form v-if="show">
          <b-form-group
            id="input-group-1"
            label="이름:"
            label-for="input-1"
            description="이름은 수정 불가합니다.">
            <b-form-input
              id="input-1"
              v-model="form.name"
              type="text"
              disabled
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.nickname"
              required
            ></b-form-input>
          </b-form-group>

          <b-button variant="info" @click="onChange()">Submit</b-button>
        </b-form>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "UserInfo",
  computed: {
    ...mapState('user', ['userInfo'])
  },
  data() {
    return {
      form: {
        name: '',
        nickname: '',
      },
      show: true,
    }
  },
  methods: {
    ...mapActions('user', [ 'putUserInfo']),
    onChange() {
      this.putUserInfo(this.form.nickname)
    },
  },
  created() {
    setTimeout(function() {
      this.form.name = this.userInfo.username
      this.form.nickname = this.userInfo.first_name
    }.bind(this), 200)
  }
}
</script>

<style>

</style>