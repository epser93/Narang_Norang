<template>
	<div v-if="fairytales" style="padding-top: 1vw; margin: auto; width: 90%;">
    <h1 class="mt-4">이달의 인기 동화</h1>
	<hr style="width: 264px; border-bottom: 6px solid #89aef3; margin-top: 0;">
		<carousel-3d :space="360" :width="240" :height="360" :border="3" :perspective="0" :scaling="0" :controls-visible="true">
			<slide v-for="(fairytale, i) in fairytales" :key="i" :index="i">
				<figure>
					<img :src="`https://j3c206.p.ssafy.io${fairytale.image}`" alt="" v-b-modal="`modal-${fairytale.id}`" @click="setModal(fairytale)">
				</figure>
			</slide>
		</carousel-3d>
		<!-- <h1 class="my-4">이달의 신작</h1>
		<div v-for="fairytale in fairytales" :key="fairytale.id">
			<img :src="`https://j3c206.p.ssafy.io${fairytale.image}`" alt="" class="mb-4" v-b-modal="`modal-${fairytale.id}`" @click="setModal(fairytale)">
		</div> -->
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
			book: {},
    }
	},
	methods: {
		...mapActions('book', ['getFairytales', 'getFairytale']),
		setModal(fairytale) {
			this.book = fairytale
			this.getFairytale(fairytale.id)
		},
		onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
	},
	created() {
		this.getFairytales()
	},

}
</script>

<style>
</style>