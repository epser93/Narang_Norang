<template>
  <div v-if="ebook">
    <div style="width: 80%; margin: 0 auto;">
      <booklet :displayPageNumber="false" :enableSelectPage="false" :displayButton="false" ref="Book">
        <div class="page cover">
          <article class="content" style="background-color: #bca98a;">
            <h1>{{ book_name }}</h1>
          </article>
        </div>
        <div class="page" v-for="(page, i) in pages" :key="i">
          <article class="content" style="background-color: white;">
            <b-icon icon="bookmarks" scale="1.5" class="float-right"></b-icon>
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
  
    <b-button v-if="currentPage != 0" size="lg" variant="secondary" class="mb-2 mx-3"  @click="start">
      <b-icon icon="app" aria-label="Help" v-if="playing"></b-icon>
      <b-icon icon="play" aria-label="Help" v-else></b-icon>
    </b-button>
    <b-button v-else size="lg" variant="secondary" class="mb-2 mx-3">
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
    ...mapState('bookmark', ['bookmark']),
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
      bid: this.$route.params.bid,
      vid: this.$route.params.vid,
      book_name: this.$route.params.bname,
      audio: new Audio(),
      index: 0,
      playing: false,
      perPage: 3,
      currentPage: 0,
    }
  },
  methods: {
    ...mapActions('book', ['getEbook', ]),
    ...mapActions('bookmark', ['getBookmark', 'postBookmark']),
    start() {
      if(this.playing) {
        this.audio.pause();
        this.playing = false;
        
      } else {
        this.playing = true;
        this.audio = new Audio("https://j3c206.p.ssafy.io" + this.ebook[this.index].voice_file)
        this.audio.play();
        this.audio.onended = () => {
          this.index++;
          this.playing = false;
          this.start()
          if (this.index % 3 == 0) {
            if (this.currentPage != (this.pages+2)) {
              this.currentPage = this.currentPage + 1
              this.$refs.Book.nextPage()
            }
          }
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
      this.audio.pause()
      this.playing = false
      if (this.currentPage != 0) {
        this.currentPage = this.currentPage - 1
        this.$refs.Book.prevPage()
      }
      this.index = 3*(this.currentPage-1)
    },
    toNext() {
      this.audio.pause()
      this.playing = false
      if (this.currentPage != (this.pages+2)) {
        this.currentPage = this.currentPage + 1
        this.$refs.Book.nextPage()
      }
      this.index = 3*(this.currentPage-1)
    },
  },
  created() {
    this.getEbook({bid: this.bid, vid: this.vid})
    this.getBookmark(this.bid)
    setTimeout(function() {
      this.currentPage = this.bookmark[0].page-1
      this.index = 3*(this.currentPage-1)
      this.$refs.Book.movePage(this.bookmark[0].page)
    }.bind(this), 200)
  },
  destroyed() {
    this.postBookmark({ bid: this.bid, body: { id: this.currentPage + 1 } })
    this.audio.pause();
  }
}
</script>
