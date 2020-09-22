<template>
	<div>
		<b-button variant="outline-secondary" @click="onRoute('REC')">
      <b-icon icon="mic" aria-hidden="true"></b-icon> 내 목소리 녹음하기
    </b-button>
	</div>
</template>

<script>
export default {
  name:"VoiceCloud",
  methods: {
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    }
  }
}
</script>

<style>

</style>