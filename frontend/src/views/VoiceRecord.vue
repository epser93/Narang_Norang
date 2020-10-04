<template>
	<div class="container">
    <div class="mr-auto ml-auto" style="width: 80%; margin-top: 50px;">
      <b-progress :value="index+1" :max="total" variant="warning" striped :animated="true" class="mt-2"></b-progress>
    </div>
    <div v-if="script" style="margin-top: 60px;">
      <p class="mt-4">마이크 버튼을 누른 후, 아래의 문장을 녹음해 주세요.</p>
      <h1 style="margin-top: 20px;">{{ test_script[index].content }}</h1>
      <hr style="width: 80%; ">
      <b-button @click="toPrev" class="mt-3">
        <b-icon icon="arrow-left-square-fill" scale="2"></b-icon>
      </b-button>
      <b-button @click="toNext" class="ml-3 mt-3">
        <b-icon icon="arrow-right-square-fill" scale="2"></b-icon>
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
        <div v-if="now_record" class="recorded-item">
          <div class="audio-container"><audio :src="now_record" controls /></div>
          <div>
            <b-button @click="removeRecord" size="sm" variant="outline-secondary">
              <b-icon icon="x" scale="2" class="pt-1" aria-hidden="true"></b-icon>
            </b-button>
          </div>
        </div>
        <div v-else>
          <h4 class="mt-3">녹음된 파일이 없습니다</h4>
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
      recordings: new Array(),
      now_record: '',
      index: 0,
    }
  },
  methods: {
    ...mapActions('voice', ['getScript', 'getTrain']),
    removeRecord() {
      if (confirm("파일을 삭제하시겠습니까??") == true) { 
        this.recordings[this.index] = ''
        this.now_record =  ''
      }
    },
    onResult(data) {
      this.recordings[this.index] = window.URL.createObjectURL(data)
      this.now_record = window.URL.createObjectURL(data)
    },
    toNext() {
      if (this.index == this.total-1) {
        alert('마지막 대본입니다.')
      } else if (this.now_record == '') {
        alert('녹음된 파일이 없습니다')
      } else {
        this.index++
        this.now_record = this.recordings[this.index]
      }
    },
    toPrev() {
      if (this.index == 0) {
        alert('첫 번째 대본입니다.')
      } else if (this.now_record == '') {
        alert('녹음된 파일이 없습니다') 
      } else {
        this.index--
        this.now_record = this.recordings[this.index]
      }
    }
  },
  created() {
    this.getScript()

    const vid = this.$route.params.vid
    this.getTrain(vid)

    for (var i = 0; i <= this.total; i++) {
      this.recordings[i] = ''
    } 
    this.now_record = this.recordings[0]
  }
}
</script>

<style>
.vue-audio-recorder {
  margin-right: 4px;
}
.record-settings {
  margin-top: 16px;
  justify-content: flex-end;
}
.recorded-audio {
  margin: 0 auto;
  height: 78px;
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
}
.audio-container {
  display: flex;
  height: 54px;
  margin-right: 16px;
}
</style>