<template>
  <div v-if="trains">
    <b-container>
      <b-row>
        <b-col cols="4" v-for="train in trains" :key="train.id" class="py-3">
          <b-card bg-variant="light" style="cursor: pointer;">
            <b-avatar size="lg" rounded="lg" :text="train.name" variant="light"></b-avatar>
          </b-card>
          <div v-if="!train.is_train" class="mt-2">
            <b-button @click="onRoute(train.id)"><b-icon icon="mic-fill" scale="1.2" class="mr-2"></b-icon></b-button>
            <b-button @click="getId(train.id)" v-b-modal.modal-train><b-icon icon="pencil-square" scale="1.2" class="mr-2"></b-icon></b-button>
            <b-button @click="onDelete(train.id)"><b-icon icon="trash-fill" scale="1.2"></b-icon></b-button>
          </div>
          <h5 v-else class="mt-3"><strong>학습중</strong></h5>
        </b-col>

    <b-modal
      id="modal-train"
      ref="modal"
      title="목소리 이름 변경">

      <form ref="form">
        <b-form-group
          label="수정할 이름"
          label-for="name-input"
          invalid-feedback="이름은 필수 사항입니다."
        >
          <b-form-input
            id="name-input"
            v-model="form.name"
            placeholder="이름을 입력해 주세요."
            required
          ></b-form-input>
        </b-form-group>
      </form>

    <template v-slot:modal-footer="{ cancel, ok }">
      <b-button @click="cancel();" variant="outline-secondary">닫기</b-button>
      <b-button @click="ok(); handleSubmit();" variant="outline-primary">수정</b-button>
    </template>
    
    </b-modal>

        <b-col cols="4" class="py-3">
          <b-card v-b-modal="'new-question'">
            <b-avatar class="plus-icon" size="lg" rounded="lg" icon="plus"></b-avatar>
          </b-card>
        </b-col>
      </b-row>
    </b-container>

    <b-modal :id="'new-question'" title="목소리 녹음하기" no-close-on-backdrop>
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

      <template v-slot:modal-footer="{ cancel }">
        <b-button @click="cancel();" variant="outline-secondary">닫기</b-button>
      </template>
    </b-modal>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name:"NewVoice",
  computed: {
    ...mapState('voice', ['trains']),
  },
  data() {
    return {
      form: {
        name: ''
      },
      id: '',
    }
  },
  methods: {
    ...mapActions('voice', ['getTrains', 'postTrain', 'putTrain', 'delTrain']),
    onREC() {
      if (this.form.name) {
        this.postTrain(this.form)
      }
      else {
        alert('목소리 이름을 입력해주세요.')
      }
    },
    onRoute(vid) {
      if (confirm("이어서 녹음 하시겠습니까?") == true) {
        this.$router.push({name:'REC', params:{vid: vid}})
      }
    },
    getId(tid) {
      this.id = tid
    },
    handleSubmit() {
      this.putTrain({ index: this.id, body: this.form})
      this.form.name = ''
    },
    onDelete(tid) {
			if (confirm("정말 삭제하시겠습니까??") == true) { 
        this.delTrain(tid)
      }
    }
  },
  created() {
    this.getTrains()
  }
}
</script>

<style>
.b-avatar .b-avatar-img, .b-avatar .b-avatar-text {
  width: 200%;
}
</style>