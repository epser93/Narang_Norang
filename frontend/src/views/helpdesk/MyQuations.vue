<template>
	<div v-if="quations">
		<b-button variant="outline-secondary" class="mb-2" @click="onRoute('Quation')">
      <b-icon icon="pencil-square" aria-hidden="true"></b-icon> 문의하기
    </b-button>

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
				<tr v-for="quation in quations" :key="quation.id" @click="onDetail(quation.id)">
					<th scope="row">{{quation.id}}</th>
					<td>{{quation.title}}</td>
					<td>{{quation.create_date}}</td>
					<td>{{(quation.is_answer) ? "완료" : "대기"}}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
	name:"MyQuations",
	computed: {
		...mapState('help', ['quations']),
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
		...mapActions('help', ['getQuations']),
		onDetail(qid) {
			this.$router.push({name:'QAdetail', params:{qid: qid}})
		},
		onRoute(name) {
      this.$router.push({name: name}, () => {})
    }
	},
	created() {
		this.getQuations()
	},
}
</script>

<style>

</style>