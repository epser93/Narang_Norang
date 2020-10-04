<template>
	<div>
    <div class="mt-4">
      <h3>진행 방법은 다음과 같습니다.</h3>
      <div class="mt-4">
        <p>1. 마이크 버튼을 클릭하면 녹음을 시작합니다.</p>
        <p>2. 녹음을 시작하면 제시된 문장을 읽어주세요.</p>
        <p>3. 문장을 다 읽으셨다면 버튼을 한번 더 눌러 종료해주세요.</p>
        <p>4. 목소리를 들어보고 다시 녹음하고 싶다면 왼쪽 버튼을 눌러주세요.</p>
        <p>5. 저장하고 싶다면 오른쪽 버튼을 누르고 다음으로 넘어가주세요.</p>
        <p>6. 총 100개의 스크립트가 준비되어 있으며, 예상 소요 시간은 3시간입니다.</p>
      </div>
    </div>

    <b-form-input
      v-model="form.name"
      required
      placeholder="목소리 이름을 입력해주세요."
      style="width 50%;"
    ></b-form-input>

		<b-button class="mt-4" variant="outline-secondary" @click="onREC()">
      <b-icon icon="mic" aria-hidden="true"></b-icon> 네, 녹음할게요.
    </b-button>
	</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name:"VoiceCloud",
  data() {
    return {
      form: {
        name: ''
      }
    }
  },
  methods: {
    ...mapActions('voice', ['postTrain']),
    onREC() {
      if (this.form.name) {
        this.postTrain(this.form)
      }
      else {
        alert('목소리 이름을 입력해주세요.')
      }
    },
  },

}
</script>

<style>

</style>