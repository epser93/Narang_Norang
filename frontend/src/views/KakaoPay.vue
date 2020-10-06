<template>
  <div class="loading-image">
    <h1>결제 진행 중입니다.</h1>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: "KakaoPay",
  methods: {
    ...mapActions('user', ['progressKakaoPay'])
  },
  created() {
    const data = {
      tid: this.$cookies.get('tid'),
      pg_token: this.$route.query.pg_token
    } 
    this.progressKakaoPay(data)
  }
}
</script>

<style>

</style>