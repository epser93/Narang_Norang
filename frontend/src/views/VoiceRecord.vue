<template>
  <div>

    <div v-if="is_loading" class="loading-image" style="margin-top: 280px;">
      <h1>잠시만 기다려 주세요.</h1><b-icon icon="three-dots" animation="cylon" font-scale="4"></b-icon>
    </div>

    <div v-else class="container">
      <div class="mr-auto ml-auto" style="width: 80%; margin-top: 50px;">
        <b-progress :value="index+1" :max="total" variant="warning" striped :animated="true" class="mt-2"></b-progress>
        <h3 class="mt-2">{{ index+1 }} / {{total}}</h3>
      </div>
      <div v-if="script">
        <p class="mt-4">마이크 버튼을 누른 후, 아래의 문장을 녹음해 주세요.</p>
        <h1 style="margin-top: 20px;">{{ script[index].content }}</h1>
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
          <vue-record-audio v-if="now_record" :mode="'press'" @result="onResult" style="pointer-events: none;"/>
          <vue-record-audio v-else :mode="'press'" @result="onResult" />
        </div>
      </div>
      <div class="column mt-4">
        <div class="recorded-audio">
          <div v-if="now_record" class="recorded-item">
            <div class="audio-container"><audio :src="now_record" controls /></div>
              <b-button @click="removeRecord" size="sm" variant="outline-secondary">
                <b-icon icon="x" scale="2" class="pt-1" aria-hidden="true"></b-icon>
              </b-button>
          </div>
          <div v-else>
            <p class="mt-3">녹음된 파일이 없습니다.</p>
          </div>
        </div>
      </div>
      <b-button @click="$router.go(-1)" variant="outline-secondary" class="mr-auto ml-auto mt-4">
        <b-icon icon="arrow-left" aria-hidden="true"></b-icon> 뒤로가기
      </b-button>
    </div>

  </div>
</template>

<script>
import swal from 'sweetalert'
import { mapState, mapActions } from 'vuex'

export default {
  name:"VoiceRecord",
  computed: {
    ...mapState('voice', ['script', 'train']),
    total() {
      return this.script.length
    },
  },
  data() {
    return {
      vid : this.$route.params.vid,
      is_loading: true,
      recordings: new Array(),
      now_record: '',
      index: 0,
    }
  },
  methods: {
    ...mapActions('voice', ['getScript', 'getTrain', 'postCaption', 'delCaption', 'startTrain']),
    removeRecord() {
      swal({
        title: "파일을 삭제하시겠습니까??",
        icon: "warning",
        buttons: ['닫기', '확인'],
      })
      .then((willDelete) => {
        if (willDelete) {
          this.delCaption({ vid: this.vid, cid: this.index + 1 })
          this.recordings[this.index] = ''
          this.now_record =  ''
        }
      })
    },
    onResult(data) {
      const file = new Blob([data], { type: 'audio/wav' })
      this.postCaption({ vid: this.vid, cid: this.index + 1, file: file })
      this.recordings[this.index] = window.URL.createObjectURL(file)
      this.now_record = window.URL.createObjectURL(file)
    },
    toNext() {
      if ((this.index == this.total-1)&&(this.now_record != '')) {
        swal({
          title: "학습을 시작하시겠습니다?",
          text: "(학습을 시작하면 더 이상 수정이 불가합니다.)",
          buttons: ['닫기', '확인'],
        })
        .then((willDelete) => {
          if (willDelete) {
            this.startTrain(this.vid)
          }
        })
      } else if (this.index == this.total-1) {
        swal('마지막 대본입니다.', { buttons: '확인' })
      } else if (this.now_record == '') {
        swal('녹음된 파일이 없습니다', { buttons: '확인' })
      } else {
        this.index++
        this.now_record = this.recordings[this.index]
      }
    },
    toPrev() {
      if (this.index == 0) {
        swal('첫 번째 대본입니다.', { buttons: '확인' })
      } else if (this.now_record == '') {
        swal('녹음된 파일이 없습니다', { buttons: '확인' }) 
      } else {
        this.index--
        this.now_record = this.recordings[this.index]
      }
    },
  },
  created() {
    this.getScript()
    this.getTrain(this.vid)
    setTimeout(function() {
      this.index = this.train.length
      for (var i = 0; i < this.total; i++) {
        if (i < this.index) {
          this.recordings[i] = 'https://j3c206.p.ssafy.io' + this.train[i].train_file
        } else {
          this.recordings[i] = ''
        }
      }
      this.index = (this.index == this.total) ? (this.total - 1) : this.index 
      this.now_record = this.recordings[this.index]
      this.is_loading = false

    }.bind(this), 1500)
  }
}
</script>

<style scoped>
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

@keyframes pulse {
  from {
    background-color: transparent;
    transform: scale(.8)
  }
  to {
    background-color: transparent;
    transform: scale(.9)
  }
}

.loading-image {
  margin-top: 130px;
}
</style>