<template>
	<div v-if="fairytales">
    <h1 class="mt-4">베스트 셀러</h1>
		<carousel-3d :space="360" :width="240" :height="360" :border="3" :perspective="0" :scaling="0">
			<slide v-for="(slide, i) in slides" :key="i" :index="i">
				<figure>
					<img src="https://placehold.it/240x360" alt="">
				</figure>
			</slide>
		</carousel-3d>

		<h1 class="my-4">이달의 신작</h1>
		<img :src="`https://j3c206.p.ssafy.io${fairytales[0].image}`" alt="" class="mb-4" v-b-modal="`modal-${fairytales[0].id}`" @click="setModal(fairytales[0])">

		<book-detail :book="book"/>
	</div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d';
import { mapState, mapActions } from 'vuex'
import	BookDetail from '@/components/BookDetail'

export default {
	name:"Main",
	components: {
    'carousel-3d': Carousel3d,
		'slide': Slide,
		BookDetail
	},
	computed: {
		...mapState('book', ['fairytales']),
  },
  data() {
    return {
			slides: 7,
			book: {},
    }
	},
	methods: {
		...mapActions('book', ['getFairytales', 'getFairytale']),
		setModal(fairytale) {
			this.book = fairytale
			this.getFairytale(fairytale.id)
		}
	},
	created() {
		this.getFairytales()
	},

}
</script>

<style>

</style>