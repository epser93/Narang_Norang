<template>
  <div>
    <flipbook class="flipbook" :pages="pages" :zooms="null" v-slot="flipbook">
      <button @click="flipbook.flipLeft">Previous Page</button>
      <button @click="flipbook.flipRight">Next Page</button>
    </flipbook>
  </div>
</template>

<script>
import Flipbook from "flipbook-vue";

export default {
  name: "Ebook",
  components: {
    Flipbook,
  },
  data() {
    return {
      pages: [
        null,
				'http://placekitten.com/100/151',
				'http://placekitten.com/g/100/151',
				'http://placekitten.com/100/152',
				'http://placekitten.com/g/100/152'
      ],
    };
  },
};
</script>

<style scoped>
.flipbook {
  width: 90vw;
  height: 90vh;
}
</style>