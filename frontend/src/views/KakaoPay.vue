<template>
    <div v-if="is_loading" class="loading-image" style="margin-top: 280px;">
      <h1>결제를 진행 중입니다.</h1><b-icon icon="three-dots" animation="cylon" font-scale="4"></b-icon>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: "KakaoPay",
  data() {
    return {
      is_loading: true,
    }
  },
  methods: {
    ...mapActions('user', ['progressKakaoPay'])
  },
  created() {
    const data = {
      tid: this.$cookies.get('tid'),
      pg_token: this.$route.query.pg_token
    } 
    this.progressKakaoPay(data)
    setTimeout(function() {
      this.is_loading = false
    }.bind(this), 1500)
  }
}
</script>

<style>
  .loading-image {
    margin-top: 130px;
  }
</style>