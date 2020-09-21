<template>
	<div>
    <h1 class="mt-4">베스트 셀러</h1>
		<carousel-3d :space="360" :width="240" :height="360" :border="3" :perspective="0" :scaling="0">
			<slide v-for="(slide, i) in slides" :key="i" :index="i">
				<figure>
					<img src="https://placehold.it/240x360" alt="" v-b-modal="`modal-${i}`" @click="setModal(i)">
				</figure>
			</slide>
		</carousel-3d>

		<b-modal :id="`modal-${mid}`" size="lg">
			<b-container>
				<b-row>
					<b-col cols="6">
						<img src="https://placehold.it/240x360" alt="" style="width: 100%;">
					</b-col>

					<b-col cols="6">
						<b-card style="height: 100%;">


							<template v-slot:footer>
								<b-button block variant="secondary">책 보러 가기</b-button>
							</template>
						</b-card>
					</b-col>
				</b-row>
			</b-container>

			<template v-slot:modal-footer="{ cancel }">
				<b-button @click="cancel()">
					닫기
				</b-button>
			</template>
		</b-modal>
	</div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
	name:"Main",
	components: {
    'carousel-3d': Carousel3d,
    'slide': Slide
  },
  data() {
    return {
			slides: 8,
			mid: null,
    }
	},
	methods: {
		setModal(mid) {
			this.mid = mid
		}
	}

}
</script>

<style>

</style>