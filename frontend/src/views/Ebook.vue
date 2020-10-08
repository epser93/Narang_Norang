<template>
  <div>
    <div v-if="is_loading" class="loading-image" style="margin-top: 280px;">
      <h1>잠시만 기다려 주세요.</h1><b-icon icon="three-dots" animation="cylon" font-scale="4"></b-icon>
    </div>

    <div v-else>
      <div style="width: 80%; margin: 0 auto;">
        <booklet :displayPageNumber="false" :enableSelectPage="false" :displayButton="false" :onFlipEnd="this.onFlipEnd" ref="Book">
          <div class="page cover">
            <article class="content" style="background-color: #bca98a;">
              <h1>{{ book_name }}</h1>
            </article>
          </div>
          <div class="page" v-for="(page, i) in pages" :key="i">
            <article class="content" style="background-color: white;">
              <b-icon icon="bookmarks" scale="1.5" class="float-right"></b-icon>
              <div v-for="(item, j) in itemsForList" :key="j">
                <h3 @click="readMe(3*i + j)" class="my-5" :id="`index${3*i + j}`"><text-highlight :queries="queries">
                  {{ item.scenario.content }}
                </text-highlight></h3>
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

      <b-button size="lg" variant="secondary" class="mb-2 mx-3" @click="toPrev()">
        <b-icon icon="arrow-left" aria-label="Help"></b-icon>
      </b-button>
    
      <b-button v-if="(this.nowPage == 0) || (this.nowPage > this.pages)" size="lg" variant="secondary" class="mb-2 mx-3" @click="restart">
        <b-icon icon="app" aria-label="Help" v-if="playing"></b-icon>
        <b-icon icon="play" aria-label="Help" v-else></b-icon>
      </b-button>
      <b-button v-else size="lg" variant="secondary" class="mb-2 mx-3" @click="start">
        <b-icon icon="app" aria-label="Help" v-if="playing"></b-icon>
        <b-icon icon="play" aria-label="Help" v-else></b-icon>
      </b-button>

      <b-button size="lg" variant="secondary" class="mb-2 mx-3"  @click="toNext()">
        <b-icon icon="arrow-right" aria-label="Help"></b-icon>
      </b-button>

    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import booklet  from 'vue-booklet'
import swal from 'sweetalert'

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
        (this.nowPage - 1) * this.perPage,
        this.nowPage * this.perPage,
      );
    },
    queries() {
      return this.ebook[this.index].scenario.content
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
      is_paged: true,
      is_loading: true,
      direction: '',
      perPage: 3,
      nowPage: 0,
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
            if (this.nowPage != (this.pages+2)) {
              this.nowPage = this.nowPage + 1
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
      if ((this.nowPage != 0) && this.is_paged) {
        this.$refs.Book.prevPage()
        this.is_paged = false
        setTimeout(function() {
          this.nowPage = this.nowPage - 1
          this.index = 3*(this.nowPage-1)
        }.bind(this), 350)
      }

    },
    toNext() {
      this.audio.pause()
      this.playing = false
      if ((this.nowPage != (this.pages+2)) && this.is_paged) {
        this.$refs.Book.nextPage()
        this.is_paged = false
        setTimeout(function() {
          this.nowPage = this.nowPage + 1
          this.index = 3*(this.nowPage-1)
        }.bind(this), 150)
      }
    },
    onFlipEnd() {
      this.is_paged = true
    },
    restart() {
      if (this.nowPage > this.pages) {
        this.nowPage = 0
        this.index = 0
        this.$refs.Book.movePage(1)
      } else {
        this.toNext()
        setTimeout(function() {
          this.start()
        }.bind(this), 1000)
      }
    }
  },
  created() {
    this.getEbook({bid: this.bid, vid: this.vid})
    this.getBookmark(this.bid)
    setTimeout(function() {
      this.is_loading = false
      if ((this.bookmark.length == 0) || (this.bookmark[0].page == 1)) {
        this.nowPage = 0
        this.index = 3*(this.nowPage-1)
        this.$refs.Book.movePage(1)
      } else {
        swal({
          title: "이어서 읽으시겠습니까?",
          buttons: ['닫기', '확인'],
        })
        .then((willDelete) => {
          if (willDelete) {
            this.nowPage = this.bookmark[0].page-1 
            this.index = 3*(this.nowPage-1)
            this.$refs.Book.movePage(this.bookmark[0].page)
          } else {
            this.nowPage = 0
            this.index = 3*(this.nowPage-1)
            this.$refs.Book.movePage(1)
          }
        })
      }
    }.bind(this), 1500)
  },
  destroyed() {
    if (this.nowPage > this.pages) {
      this.postBookmark({ bid: this.bid, body: { id: 1 } })
    } else {
      this.postBookmark({ bid: this.bid, body: { id: this.nowPage + 1 } })
    }
    this.audio.pause();
  }
}
</script>

<style>
  .loading-image {
    margin-top: 130px;
  }
  mark, .mark {
    padding: 0;
  }
</style>