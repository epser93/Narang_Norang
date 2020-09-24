<template>
	<div v-if="questions">
    <div>
      <b-button variant="outline-secondary" class="mb-3" @click="onRoute('Question')">
        <b-icon icon="pencil-square" aria-hidden="true"></b-icon> 문의하기
      </b-button>
    </div>

		<table class="table table-hover">
			<thead>
				<tr>
					<th scope="col" cols="2">#</th>
					<th scope="col" cols="5">제목</th>
					<th scope="col" cols="3">날짜</th>
					<th scope="col" cols="2">답변</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="question in questions" :key="question.id" @click="onDetail(question.id)">
					<th scope="row">{{question.id}}</th>
					<td>{{question.title}}</td>
					<td>{{question.create_date}}</td>
					<td>{{(question.is_answer) ? "완료" : "대기"}}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
	name:"MyQuestions",
	computed: {
		...mapState('help', ['questions']),
  },
	data() {
		return {
			// QA
			fields: ['제목', '답변', '날짜'],
			items: [
				{ 날짜: 40, 제목: 'Dickerson', 답변: 'Macdonald' },
				{ 날짜: 21, 제목: 'Larsen', 답변: 'Shaw' },
				{ 날짜: 89, 제목: 'Geneva', 답변: 'Wilson' }
			],
		}
	},
	methods: {
		...mapActions('help', ['getQuestions']),
		onDetail(qid) {
			this.$router.push({name:'QAdetail', params:{qid: qid}})
		},
		onRoute(name) {
      this.$router.push({name: name}, () => {})
    }
	},
	created() {
		this.getQuestions()
	},
}
</script>

<style>

</style>