<template>
	<div class="container">
    <div class="mr-auto ml-auto" style="width: 80%; margin-top: 50px;">
      <b-progress :value="index+1" variant="warning" striped :animated="true" class="mt-2"></b-progress>
    </div>
    <div v-if="script" style="margin-top: 60px;">
      <p class="mt-4">마이크 버튼을 누른 후, 아래의 문장을 녹음해 주세요.</p>
      <h1 style="margin-top: 20px;">{{ test_script[index].content }}</h1>
      <hr style="width: 80%; ">
      <b-button @click="toPrev" class="mt-3">
        <b-icon icon="arrow-left-square-fill" scale="2"></b-icon>
      </b-button>
      <b-button @click="toNext" class="mt-3">
        <b-icon class="ml-3" icon="arrow-right-square-fill" scale="2"></b-icon>
      </b-button>
    </div>

    <div style="margin-top: 100px;">
      <div class="record-settings">
        <!-- <vue-record-audio :mode="'press'" @stream="onStream" @result="onResult" /> -->
        <vue-record-audio :mode="'press'" @result="onResult" />
      </div>
    </div>
    <div class="column mt-4">
      <div class="recorded-audio">
        <div class="recorded-item">
          <div class="audio-container"><audio :src="now_record" controls /></div>
          <div>
            <button @click="removeRecord">delete</button>
          </div>
        </div>
      </div>
    </div>
    <b-button @click="$router.go(-1)" variant="outline-secondary" class="mr-auto ml-auto mt-4">
      <b-icon icon="arrow-left" aria-hidden="true"></b-icon> 뒤로가기
    </b-button>
	</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name:"VoiceRecord",
  computed: {
    ...mapState('voice', ['script']),
    total() {
      // return this.script.length
      return this.test_script.length
    },
  },
  data() {
    return {
      test_script: [
        {
          id: 1,
          content: '첫 번째 대본입니다.'
        },
        {
          id: 2,
          content: '두 번째 대본입니다.'
        },
        {
          id: 3,
          content: '세 번째 대본입니다.'
        },
        {
          id: 4,
          content: '네 번째 대본입니다.'
        },
        {
          id: 5,
          content: '마지막 대본입니다.'
        },
      ],
      recordings: new Array(this.total),
      now_record: this.recordings[0],
      index: 0,
    }
  },
  methods: {
    ...mapActions('voice', ['getScript']),
    removeRecord() {
      this.recordings[this.index] = undefined
    },
    onResult(data) {
      this.recordings[this.index] = window.URL.createObjectURL(data)
      this.now_record = window.URL.createObjectURL(data)
      console.log(this.recordings)
    },
    toNext() {
      if (this.index < this.total-1) {
        this.index++
        this.now_record = this.recordings[this.index]
      } else {
        alert('마지막 대본입니다.')
      }
    },
    toPrev() {
      if (this.index > 0) {
        this.index--
        this.now_record = this.recordings[this.index]
      } else {
        alert('첫 번째 대본입니다.')
      }
    }
  },
  created() {
    this.getScript()
  }
}
</script>

<style>
.vue-audio-recorder {
  margin-right: 16px;
}
.record-settings {
  margin-top: 16px;
  justify-content: flex-end;
}
.recorded-audio {
  margin: 0 auto;
  height: 74px;
  overflow: auto;
  border: thin solid #eee;
  background-color: #f7f7f7;
  padding: 10px 5px;
  border-radius: 15px; 
  width: 80%;
}
.recorded-item {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
}
.audio-container {
  display: flex;
  height: 54px;
  margin-right: 16px;
}
</style>