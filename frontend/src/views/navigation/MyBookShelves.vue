<template>
<div>
  <!-- 읽고 있어요 -->
  <div class="mt-4">
    <h2 class="mb-4">읽고 있어요 <b-icon icon="book"></b-icon></h2>
    <b-container fluid class="p-2">
      <b-row>
        <b-col v-for="bookmark in bookmarks" :key="bookmark.fairytale.id">
          <b-img thumbnail class="thumbnail" 
          fluid :src="`https://j3c206.p.ssafy.io${bookmark.fairytale.image}`" 
          alt="Image 1"
          v-b-modal="`modal-${bookmark.fairytale.id}`"
          @click="setModal(bookmark.fairytale)">
          </b-img>
        </b-col>
      </b-row>
    </b-container>
    <hr>
  </div>

<!-- 보고 싶어요 -->
  <div v-if="favorites" style="margin-top: 6vmin;">
    <h2 class="mb-4">보고 싶어요 <b-icon icon="bookmark-heart"></b-icon></h2>
    <b-container fluid class="p-2">
      <b-row>
        <b-col v-for="favorite in favorites" :key="favorite.id">
          <b-img thumbnail class="thumbnail" 
          fluid :src="`https://j3c206.p.ssafy.io${favorite.image}`" 
          alt="Image 1"
          v-b-modal="`modal-${favorite.id}`"
          @click="setModal(favorite)">
          </b-img>
        </b-col>
      </b-row>
    </b-container>
    <hr>
  </div>

  <book-detail :book="book"/>

</div>
</template>

<script>
// import BookShelves from "@/components/BookShelves.vue"
import { mapState, mapActions } from 'vuex'
import	BookDetail from '@/components/BookDetail'

export default {
  name:"MyBookShelves",
  components: {
		BookDetail
  },
  computed: {
    ...mapState('bookmark', ['bookmarks']),
    ...mapState('favorite', ['favorites']),
  },
  data() {
    return {
      book: {},
    }
  },
  methods: {
    ...mapActions('bookmark', ['getBookmarks']),
    ...mapActions('favorite', ['getFavorites']),
    ...mapActions('book', ['getFairytale']),
		setModal(favorite) {
			this.book = favorite
			this.getFairytale(favorite.id)
		}
  },
  created() {
    this.getBookmarks()
    this.getFavorites()
  }
}
</script>

<style scoped>
.thumbnail {
  box-shadow: 4px 10px 5px #00000063;
}

hr {
  margin-top: -2rem;
  margin-bottom: 1rem;
  border-top: 8vmin solid #b07112b0;
  width: 170vmin;
}
</style>