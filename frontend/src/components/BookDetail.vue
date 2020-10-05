<template>
  <b-modal :id="`modal-${book.id}`" size="lg">
    <b-container v-if="fairytale">
      <b-row>
        <b-col cols="6">
          <b-card style="min-height: 540px;">
            <img :src="`https://j3c206.p.ssafy.io/${fairytale.image}`" alt="" style="width: 100%; margin-top: 5%;">
          </b-card>
        </b-col>
        <b-col cols="6">
          <b-card style="height: 100%;">
            <div style="">
              <h3>{{ fairytale.title }}</h3>
              <hr>
              <h5>{{ fairytale.summary }}</h5>
            </div>
            <template v-slot:footer>
              <div class="row justify-content-around">
                <!-- 책 읽기 -->
                <b-button @click="onDetail(fairytale.id)" variant="secondary">책 읽기<b-icon class="ml-2" icon="caret-right-fill" scale="1.2"></b-icon></b-button>
                <!-- 즐겨찾기 -->
                <b-button v-if="fairytale.is_liked" @click="changeStar"><b-icon icon="star-fill"></b-icon></b-button>
                <b-button v-else @click="changeStar" variant="secondary"><b-icon icon="star" scale="1.2"></b-icon></b-button>
              </div>
            </template>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <template v-slot:modal-footer="{ cancel }">
      <b-button @click="cancel()">
      </b-button>
    </template>
  </b-modal>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: "BookDetail",
  props: {
    book: {
      type: Object,
    },
  },
  computed: {
		...mapState('book', ['fairytale']),
  },
  data() {
    return {
    }
  },
  methods: {
    ...mapActions('favorite', ['postFavorites']),
    ...mapActions('favorite', ['deleteFavorites']),
		onDetail(bid) {
			this.$router.push({name:'Ebook', params:{bid: bid}})
    },
    changeStar() {
      this.fairytale.is_liked = !this.fairytale.is_liked
      if (this.fairytale.is_liked) {
        this.postFavorites(this.fairytale.id)
      } else {
        this.deleteFavorites(this.fairytale.id)
      }
    },
	},
}
</script>

<style>

</style>