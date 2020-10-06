<template>
  <div style="margin: auto; width: 90%;">
    <b-input-group size="lg" style="width: 25%; position: absolute; right:15%;">
      <b-form-input type="search" placeholder="책 이름 검색" v-model="search" @keypress.enter="getSearch(search)"></b-form-input>
      <b-input-group-append>
        <b-button text="Button" variant="outline-secondary" @click="getSearch(search)"><b-icon icon="search"></b-icon></b-button>
      </b-input-group-append>
    </b-input-group>

    <b-container style="padding-top: 75px;">
      <b-row>
        <b-col cols="4" v-for="fairytale in fairytales" :key="fairytale.id" style="padding-top: 25px; padding-bottom: 25px;">
          <img :src="`https://j3c206.p.ssafy.io${fairytale.image}`" alt="" class="mb-4" v-b-modal="`modal-${fairytale.id}`" @click="setModal(fairytale)">
          <h5><strong>{{ fairytale.title }}</strong></h5>
        </b-col>
      </b-row>
    </b-container>

		<book-detail :book="book"/>
  </div> 
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import	BookDetail from '@/components/BookDetail'

export default {
  name: "Books",
  components: {
		BookDetail
	},
	computed: {
		...mapState('book', ['fairytales']),
  },
  data() {
    return {
      book: {},
      search: ''
    }
	},
	methods: {
    ...mapMutations('book', ['SET_FAIRYTALES']),
		...mapActions('book', ['getFairytales', 'getFairytale', 'getSearch']),
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
  destroyed() {
    this.SET_FAIRYTALES('')
  }
}
</script>

<style>

</style>