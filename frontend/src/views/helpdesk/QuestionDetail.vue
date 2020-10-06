<template>
	<div class="container" v-if="question">
    <!-- 사용자 질문 -->
    <b-badge v-if="question.is_answer" variant="primary">답변완료</b-badge>
    <b-badge v-else variant="light">미답변</b-badge>
    <div class="col-8 justify-content-center mr-auto ml-auto">
      <h3 class="mb-0">{{ question.title }}</h3>
      <p class="ml-1">{{ question.create_date }}</p>
    </div>
    <hr>
    <div style="min-height: 150px;">
      <p>" {{ question.content }} "</p>
    </div>
    <hr>
    <!-- 답변란 -->

    <div v-if="(!question.is_answer) && (userInfo.is_staff)">
      <b-form-textarea
        id="textarea-large"
        placeholder="답변을 남겨주세요."
        rows="5"
        v-model="form.content"
      ></b-form-textarea>
    </div>
    <div v-if="question.is_answer">
      <p class="mt-1" style="font-weight: bold;">to. {{(question.user.first_name == '') ? question.user.username : question.user.first_name}} 님</p>
      <p>" {{ question.qna_reply[0].content }} "</p>
      <p class="mt-4">from. 나랑노랑</p>
      <hr>
    </div>
    <b-button @click="onRoute('QA')" variant="outline-secondary" class="my-2 mr-2">
      <b-icon icon="arrow-left" aria-hidden="true"></b-icon> 뒤로가기
    </b-button>
    <b-button v-if="(!question.is_answer) && (question.user.id == userInfo.id)" @click="onDelete" variant="outline-danger" class="my-2 mr-2">
      <b-icon icon="x-square" class="pt-1" aria-hidden="true"></b-icon> 삭제하기
    </b-button>
    <b-button v-if="(!question.is_answer) && (question.user.id == userInfo.id)" @click="onUpdate" variant="outline-info" class="my-2 mr-2">
      <b-icon icon="pencil-square" class="pt-1" aria-hidden="true"></b-icon> 수정하기
    </b-button>
      <b-button v-if="(userInfo.is_staff)" @click="onReply" variant="outline-info" class="my-2 mr-2">
      <b-icon icon="pencil-square" class="pt-1" aria-hidden="true"></b-icon> 답변하기
    </b-button>
	</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name:"QuestionDetail",
  computed: {
    ...mapState('user', ['userInfo']),
    ...mapState('help', ['question'])
  },
  data() {
    return {
      form: {
        content: '',
      }
    }
  },
  methods: {
    ...mapActions('help', ['getQuestion', 'delQuestion','postReply']),
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
    onDelete() {
      if (confirm("정말 삭제하시겠습니까??") == true) { 
        this.delQuestion(this.question.id)
      }
    },
    onUpdate() {
			this.$router.push({name:'QAupdate', params:{ qid: this.question.id, update: 'update' }})
		},
    onReply() {
      if (this.form.content) {
        this.postReply({ index: this.question.id, body: this.form })
      } else {
        alert("다시 확인 해주세요.")
      }
    }
  },
  created() {
    const qid = this.$route.params.qid
    this.getQuestion(qid)
  },
}
</script>

<style>
.container {
  cursor: default;
}
</style>