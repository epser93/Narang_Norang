<template>
  <div>
    <top-navigation/>

        <div id="example">
          <carousel-3d @after-slide-change="onAfterSlideChange" @before-slide-change="onBeforeSlideChange" @last-slide="onLastSlide"
            :space="360" :width="240" :height="360" :border="3" :perspective="0" :scaling="0">
            
            <slide v-for="(slide, i) in slides" :key="i" :index="i">
              <figure>
                <img src="https://placehold.it/240x360">
              </figure>
            </slide>

          </carousel-3d>
        </div>

    <!-- <div id="example">
      <carousel-3d @after-slide-change="onAfterSlideChange" @before-slide-change="onBeforeSlideChange" @last-slide="onLastSlide" :disable3d="true"
        :space="250" :width="240" :height="360" :border="3" :perspective="0" :scaling="0">

        <slide v-for="(slide, i) in slides" :key="i" :index="i">
          <figure>
            <img src="https://placehold.it/360x270">
          </figure>
        </slide>

      </carousel-3d>
    </div> -->
      
  </div>
</template>

<script>
import TopNavigation from '@/components/TopNavigation'
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: 'Home',
  components: {
    TopNavigation,
    'carousel-3d': Carousel3d,
    'slide': Slide
  },
  data() {
    return {
      slides: 7
    }
  },
}
</script>

