<template>
  <div v-if="ebook">
    <div style="width: 80%; margin: 0 auto;">
      <booklet :displayPageNumber="false" :enableSelectPage="false" :displayButton="false" ref="Book">
        <div class="page cover">
          <article class="content" style="background-color: #bca98a;">
            <h1>흥부와 놀부</h1>
          </article>
        </div>
        <div class="page" v-for="(page, i) in pages" :key="i">
          <article class="content" style="background-color: white;">
            <div v-for="(item, j) in itemsForList" :key="j">
              <h2 @click="readMe(3*i + j)" class="my-5" :id="`index${3*i + j}`">{{ item.scenario.content }}</h2>
            </div>
          </article>
          <article class="content" style="background-color: white;">
          </article>
        </div>
        <div class="page back">
          <article class="content" style="background-color: #bca98a;" />
          <article class="content" style="background-color: #bca98a;" />
        </div>
      </booklet>
    </div>

    <b-button @click="$router.go(-1)" variant="outline-secondary" class="my-2 mr-2">
      <b-icon icon="arrow-left" aria-hidden="true"></b-icon> 뒤로가기
    </b-button>

    <b-button size="lg" variant="secondary" class="mb-2 mx-3"  @click="toPrev()">
      <b-icon icon="arrow-left" aria-label="Help"></b-icon>
    </b-button>
  
    <b-button size="lg" variant="secondary" class="mb-2 mx-3"  @click="start">
      <b-icon icon="app" aria-label="Help" v-if="playing"></b-icon>
      <b-icon icon="play" aria-label="Help" v-else></b-icon>
    </b-button>

    <b-button size="lg" variant="secondary" class="mb-2 mx-3"  @click="toNext()">
      <b-icon icon="arrow-right" aria-label="Help"></b-icon>
    </b-button>

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import booklet  from 'vue-booklet'

export default {
  name: 'EBook',
  components: {
    booklet 
  },
  computed: {
    ...mapState('book', ['ebook']),
    rows() {
      return this.ebook.length
    },
    pages() {
      return Math.ceil(this.ebook.length/this.perPage)
    },
    itemsForList() {
      return this.ebook.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage,
      );
    }
  },
  data() {
    return {
      audio: new Audio(),
      index: 0,
      playing: false,
      perPage: 3,
      currentPage: 0,
    }
  },
  methods: {
    ...mapActions('book', ['getEbook']),
    start() {
      if(this.playing) {
        this.audio.pause();
        this.playing = false;
        
      } else {
        this.playing = true;
        this.audio = new Audio("https://j3c206.p.ssafy.io/" + this.ebook[this.index].voice_file)
        this.audio.play();
        this.audio.onended = () => {
          this.index++;
          this.playing = false;
          this.start()
        }
      }
    },
    readMe(i) {
      if(this.playing) {
        this.audio.pause();
        this.playing = false;
      }
      this.index = i
      this.start()
    },
    toPrev() {
      if (this.currentPage != 0) {
        this.currentPage = this.currentPage - 1
        this.$refs.Book.prevPage()
      }
      this.index = 3*(this.currentPage-1)
      this.audio.pause();
      this.playing = false;
    },
    toNext() {
      if (this.currentPage != (this.pages+2)) {
        this.currentPage = this.currentPage + 1
        this.$refs.Book.nextPage()
      }
      this.index = 3*(this.currentPage-1)
      this.audio.pause();
      this.playing = false;
    },
  },
  created() {
    const bid = this.$route.params.bid
    this.getEbook(bid)
    setTimeout(function() {
      this.currentPage = 0
    }.bind(this), 150)
  },
}
</script>
