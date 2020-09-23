<template>
	<div>
    <b-table :items="items" :fields="fields" :hover="true" :fixed="true">
      <template v-slot:table-caption>This is a table caption.</template>
    </b-table>
	</div>
</template>

<script>
export default {
  name:"MyQuations",
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
	}
}
</script>

<style>

</style>