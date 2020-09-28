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
					<th scope="col" cols="1">#</th>
					<th scope="col" cols="5">제목</th>
					<th scope="col" cols="2">날짜</th>
					<th scope="col" cols="1">답변</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(question, i) in questions" :key="question.id" @click="onDetail(question.id)">
					<td scope="row">{{i+1}}</td>
					<td>{{question.title}}</td>
					<td>{{question.create_date}}</td>
					<td>{{(question.is_answer) ? "답변완료" : "미답변"}}</td>
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