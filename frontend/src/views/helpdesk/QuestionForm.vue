<template>
  <div>
    <h2 class="mt-2">1 : 1 문의하기</h2>
    <p style="color: grey; font-size: 14px;">나랑노랑을 사용하시면서 불편한 사항이나 개선의견이 있다면 문의해주세요.</p>
    <b-container style="min-height: 400px;">
      <b-row class="mt-2">
        <b-col cols="12">
          <b-form-input v-model="form.title" id="input-lg" size="lg" placeholder="제목을 적어주세요."></b-form-input>
        </b-col>
      </b-row>
      <b-row class="mt-2">
        <b-col cols="12">
          <b-form-textarea
            id="textarea-large"
            size="lg"
            placeholder="문의하실 내용을 적어주세요."
            rows="10"
            v-model="form.content"
          ></b-form-textarea>
        </b-col>
      </b-row>
    </b-container>
    <p class="mt-2" style="color: grey; font-size: 14px;">"언제나 나랑노랑을 이용해주셔서 감사합니다."</p>
    <b-button @click="$router.go(-1)" variant="outline-secondary" class="my-2 mr-2">
      <b-icon icon="arrow-left" aria-hidden="true"></b-icon> 뒤로가기
    </b-button>
    <b-button v-if="this.update" @click="onUpdate()" variant="outline-info" class="my-2">
      <b-icon icon="pencil-square" aria-hidden="true"></b-icon> 수정하기
    </b-button>
    <b-button v-else @click="onSubmit()" variant="outline-info" class="my-2">
      <b-icon icon="pencil-square" aria-hidden="true"></b-icon> 작성하기
    </b-button>
  </div>
</template>

<script>
import swal from 'sweetalert'
import { mapState, mapActions } from 'vuex'

export default {
  name:"QuestionForm",
  computed: {
    ...mapState('help', ['question'])
  },
  data() {
    return {
      update: false,
      form: {
        title: "",
        content: "",
      }
    }
  },
  methods: {
    ...mapActions('help', ['postQuestion', 'putQuestion']),
    onSubmit() {
      if (this.form.title && this.form.content) {
        this.postQuestion(this.form)
      } else {
        swal("다시 확인 해주세요.", { buttons: '확인' })
      }
    },
    onUpdate() {
      if (this.form.title && this.form.content) {
        this.putQuestion({ index: this.$route.params.qid, body: this.form})
      } else {
        swal("다시 확인 해주세요.", { buttons: '확인' })
      }
    }
  },
  created() {
    if (this.$route.params.update == 'update') {
      this.update = true
      this.form.title = this.question.title
      this.form.content = this.question.content
    }
  }
}
</script>

<style>
input::placeholder {
  font-size: 16px;
}

textarea::placeholder {
  font-size: 16px;
}
</style>