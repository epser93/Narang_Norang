<template>
  <div>
    <b-modal :id="`modal-${book.id}`" size="lg">
      <b-container v-if="fairytale">
        <b-row>
          <b-col cols="6">
            <b-card style="min-height: 540px;">
              <img :src="`https://j3c206.p.ssafy.io${fairytale.image}`" alt="" style="width: 100%; margin-top: 1vw;">
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
                <p v-if="book.is_pay" class="row justify-content-around">해당 동화는 유료입니다.</p>
                <hr>
                <div class="row justify-content-around">
                  <!-- 책 읽기 -->
                  <b-button v-if="(book.is_pay && !userInfo.is_subscribed)" v-b-modal.kakao-pay-book variant="outline-primary">이용권 구매하기</b-button>
                  <b-button v-else @click="onDetail(fairytale.id)" variant="secondary">책 읽기<b-icon class="ml-2" icon="caret-right-fill" scale="1.2"></b-icon></b-button>
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

    <b-modal
      id="kakao-pay-book"
      ref="modal"
      title="나랑노랑 멤버십 구독">
      <img src="@/assets/img/membership.png" style="width: 350px; margin-left: 60px;" alt="">
      <template v-slot:modal-footer="{ ok }">
        <b-button class="mr-auto ml-auto" @click="ok(); startKakaoPay();" variant="outline-primary">매달 4,800원 결제하기</b-button>
      </template>
    </b-modal>
  </div>
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
    ...mapState('user', ['userInfo']),
		...mapState('book', ['fairytale']),
  },
  data() {
    return {
    }
  },
  methods: {
    ...mapActions('favorite', ['postFavorites', 'deleteFavorites']),
    ...mapActions('user', ['startKakaoPay']),
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