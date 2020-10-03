<template>
  <b-modal :id="`modal-${book.id}`" size="lg">
    <b-container v-if="fairytale">
      <b-row>
        <b-col cols="6">
          <b-card style="min-height: 540px;">
            <img :src="`https://j3c206.p.ssafy.io/${fairytale.image}`" alt="" style="width: 100%; margin-top: 40%">
          </b-card>
        </b-col>

        <b-col cols="6">
          <b-card style="height: 100%;">
            <div style="margin-top: 40%">
              <h3>{{ fairytale.title }}</h3>
              <h5>{{ fairytale.summary }}</h5>
            </div>
            <template v-slot:footer>
              <div class="row justify-content-around">
                <!-- 책 읽기 -->
                <b-button @click="onDetail(fairytale.id)" variant="secondary">책 읽기<b-icon class="ml-2" icon="caret-right-fill" scale="1.2"></b-icon></b-button>
                <!-- 즐겨찾기 -->
                <b-button v-if="star" @click="changeStar"><b-icon icon="star-fill"></b-icon></b-button>
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
      star: false,
    }
  },
  methods: {
    ...mapActions('favorite', ['postFavorite']),
		onDetail(bid) {
			this.$router.push({name:'Ebook', params:{bid: bid}})
    },
    changeStar() {
      // this.makeToast()
      this.star = !this.star
      if (this.star) {
        this.postFavorite(this.fairytale.id)
      }
    },
    // makeToast() {
    //   if (!this.star) {
    //     this.$bvToast.toast("즐겨찾기에 추가되었습니다.", {
    //       title: `즐겨찾기 ${"추가"}`,
    //       variant: "success",
    //       solid: true,
    //       autoHideDelay: 700,
    //     });
    //   } else {
    //     this.$bvToast.toast("즐겨찾기에서 삭제되었습니다.", {
    //       title: `즐겨찾기 ${"취소"}`,
    //       variant: "danger",
    //       solid: true,
    //       autoHideDelay: 700,
    //     });     
    //   }
    // }
	},
}
</script>

<style>

</style>