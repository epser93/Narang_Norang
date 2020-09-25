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
              <b-button @click="onDetail(fairytale.id)" variant="secondary">책 읽기<b-icon class="ml-2" icon="caret-right-fill" scale="1.2"></b-icon></b-button>
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
import { mapState } from 'vuex'

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
		onDetail(bid) {
			this.$router.push({name:'Ebook', params:{bid: bid}})
		},
	},
}
</script>

<style>

</style>