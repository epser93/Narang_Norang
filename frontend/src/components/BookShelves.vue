<template>
  <div>
    <div style="width: 100%;">
      <div v-for="book in books" :key="book.id" style="display: inline-block; margin: 0px 50px">
        <img :src="book.thumbnailUrl" alt="book.title" style="width: 100%;">
      </div>
    </div>
    <img src="@/assets/img/bookshelves.png" alt="bookshelves" style="width: 80%;">
	</div>
</template>

<script>
export default {
  name: "BookSelves",
  props: {
    books: {
      type: Array,
    },
  },
  data() {
    return {

    }
  },
};
</script>