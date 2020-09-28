<template>
	<div class="container">
    <div class="mr-auto ml-auto" style="width: 80%; margin-top: 50px;">
      <b-progress :value="5" variant="warning" striped :animated="animate" class="mt-2"></b-progress>
    </div>
    <div style="margin-top: 60px;">
      <p class="mt-4">마이크 버튼을 누른 후, 아래의 문장을 녹음해 주세요.</p>
      <h1 style="margin-top: 20px;">"풀을 뜯는 얼룩말"</h1>
      <hr style="width: 80%; ">
      <b-button class="mt-3">
        다음 문장<b-icon class="ml-3" icon="arrow-right-square-fill" scale="2"></b-icon>
      </b-button>
    </div>
    <!-- <div style="positon: fixed; margin-top: 200px;">
      <vue-record-audio @result="onResult" />
      <div v-if="test_audio">
        <button @click="onPlay">
          <b-icon icon="caret-right"></b-icon>
        </button>
      </div>
    </div> -->
    <div style="margin-top: 100px;">
      <div class="record-settings">
        <vue-record-audio :mode="recordMode.audio" @stream="onStream" @result="onResult" />
      </div>
    </div>
    <div class="column mt-4">
      <div class="recorded-audio">
        <div v-for="(record, index) in recordings" :key="index" class="recorded-item">
          <div class="audio-container"><audio :src="record.src" controls /></div>
          <div>
            <button @click="removeRecord(index)">delete</button>
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
export default {
  name:"VoiceRecord",
  data() {
    return {
      // test_audio: '',
      // audio_url: '',
      // audio: '',
      // animate: true,
      recordMode: {
        audio: 'press'
      },
      recordings: []
    }
  },
  methods: {
    // onResult (data) {
    //   this.audio = data
    //   // console.log('The blob data:', data);
    //   // console.log('Downloadable audio', window.URL.createObjectURL(data));
    //   this.audio_url = window.URL.createObjectURL(this.audio)
    //   // console.log(this.audio_url)
    //   // console.log(this.audio)
    //   this.test_audio = new Audio(this.audio_url)
    // },
    // onPlay() {
    //   this.test_audio.play()
    // }
    removeRecord (index) {
      this.recordings.splice(index, 1)
    },
    onStream (stream) {
      console.log('Got a stream object:', stream);
    },
    onResult (data) {
      this.recordings.push({
        src: window.URL.createObjectURL(data)
      })
    }
  }
}
</script>

<style>
/* .vue-audio-recorder {
  background-color: #89aef3;
}

.vue-audio-recorder:hover {
  background-color: #4582f5;
} */

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