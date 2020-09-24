<template>
	<div class="container" v-if="question">
    <!-- 사용자 질문 -->
    <b-badge v-if="question.is_answer" variant="primary">답변완료</b-badge>
    <b-badge v-else variant="light">미답변</b-badge>
    <div class="col-8 justify-content-center mr-auto ml-auto">
      <h3 class="mb-0">{{ question.title }}</h3>
      <p class="ml-2 mt-1">{{ question.create_date }}</p>
    </div>
    <hr>
    <div style="min-height: 300px;">
      <p>" {{ question.content }} "</p>
    </div>
    <hr>
    <!-- 운영자 답변 -->
    <b-button @click="$router.go(-1)" variant="outline-secondary" class="my-2 mr-2">
      <b-icon icon="arrow-left" aria-hidden="true"></b-icon> 뒤로가기
    </b-button>
	</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name:"QuestionDetail",
  computed: {
    ...mapState('help', ['question'])
  },
  data() {
    return {

    }
  },
  methods: {
    ...mapActions('help', ['getQuestion'])
  },
  created() {
    const qid = this.$route.params.qid
    this.getQuestion(qid)
  }
}
</script>

<style>

</style>