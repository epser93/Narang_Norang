<template>
  <div v-if="voices">
    <b-container>
      <b-row>
        <b-col cols="4" v-for="voice in voices" :key="voice.id" class="py-3">
          <b-card bg-variant="light">
            <h5 class="mt-3"><strong>{{ voice.name }}</strong></h5>
          </b-card>
          <div v-if="(voice.id != 1) && (voice.id != 2)" class="mt-2">
            <b-button @click="getId(voice.id)" v-b-modal.modal-voice><b-icon icon="pencil-square" scale="1.2" class="mr-2"></b-icon></b-button>
            <b-button @click="onDelete(voice.id)"><b-icon icon="trash-fill" scale="1.2"></b-icon></b-button>
          </div>
        </b-col>
      </b-row>
    </b-container>

    <b-modal
      id="modal-voice"
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
        <b-button @click="cancel(); onCancle();" variant="outline-secondary">닫기</b-button>
        <b-button @click="ok(); onUpdate();" variant="outline-primary">수정</b-button>
      </template>
    
    </b-modal>

  </div>
</template>

<script>
import swal from 'sweetalert'
import { mapState, mapActions } from 'vuex'

export default {
  name:"MyVoice",
  computed: {
    ...mapState('voice', ['voices']),
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
    ...mapActions('voice', ['getVoices', 'putVoice', 'delVoice']),
    getId(vid) {
      this.id = vid
    },
    onUpdate() {
      this.putVoice({ index: this.id, body: this.form})
      this.form.name = ''
    },
    onDelete(vid) {
      swal({
        title: "정말 삭제하시겠습니까??",
        icon: "warning",
        buttons: ['닫기', '확인'],
      })
      .then((willDelete) => {
        if (willDelete) {
          this.delVoice(vid)
        }
      })
    },
    onCancle() {
      this.form.name = ''
    },
  },
  created() {
    this.getVoices()
  }
}
</script>

<style>

</style>