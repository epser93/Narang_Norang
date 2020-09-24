<template>
  <div>
    <div style="width: 80%; margin: 0 auto;">
      <booklet :displayPageNumber="false" :enableSelectPage="false" :displayButton="false" ref="Book">
        <div class="page cover">
          <article class="content" style="background-color: #bca98a;">
            <h1>My first book</h1>
          </article>
        </div>
        <div class="page">
          <article class="content" style="background-color: white;">
            <h1 @click="readMe(0)">어느날 엄마 돼지가 말했어요.</h1>
            <p></p>
            <h1 @click="readMe(1)">나는 장주환입니다.</h1>
          </article>
          <article class="content" style="background-color: white;">
            <h1>It is back of page 2</h1>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Augue ut lectus arcu bibendum at varius.
            Ac odio tempor orci dapibus ultrices in iaculis. Euismod in pellentesque massa placerat.
            Arcu felis bibendum ut tristique.
            Orci a scelerisque purus semper eget duis at. Dictum fusce ut placerat orci nulla.
            Rhoncus dolor purus non enim praesent. Auctor neque vitae tempus quam pellentesque nec.
            Vitae turpis massa sed elementum tempus. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor.
            Urna neque viverra justo nec ultrices dui sapien. Arcu cursus vitae congue mauris rhoncus.
            Laoreet sit amet cursus sit amet dictum sit amet. Gravida dictum fusce ut placerat orci nulla.
          </article>
        </div>
        <div class="page">
          <article class="content" style="background-color: white;">
            <h1>It is page 3</h1>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Augue ut lectus arcu bibendum at varius.
            Ac odio tempor orci dapibus ultrices in iaculis. Euismod in pellentesque massa placerat.
            Arcu felis bibendum ut tristique.
            Orci a scelerisque purus semper eget duis at. Dictum fusce ut placerat orci nulla.
            Rhoncus dolor purus non enim praesent. Auctor neque vitae tempus quam pellentesque nec.
            Vitae turpis massa sed elementum tempus. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor.
            Urna neque viverra justo nec ultrices dui sapien. Arcu cursus vitae congue mauris rhoncus.
            Laoreet sit amet cursus sit amet dictum sit amet. Gravida dictum fusce ut placerat orci nulla.
          </article>
          <article class="content" style="background-color: white;">
            <h1>It is back of page 3</h1>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Augue ut lectus arcu bibendum at varius.
            Ac odio tempor orci dapibus ultrices in iaculis. Euismod in pellentesque massa placerat.
            Arcu felis bibendum ut tristique.
            Orci a scelerisque purus semper eget duis at. Dictum fusce ut placerat orci nulla.
            Rhoncus dolor purus non enim praesent. Auctor neque vitae tempus quam pellentesque nec.
            Vitae turpis massa sed elementum tempus. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor.
            Urna neque viverra justo nec ultrices dui sapien. Arcu cursus vitae congue mauris rhoncus.
            Laoreet sit amet cursus sit amet dictum sit amet. Gravida dictum fusce ut placerat orci nulla.
          </article>
        </div>
        <div class="page">
          <article class="content" style="background-color: white;">
            <h1>It is page 4</h1>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Augue ut lectus arcu bibendum at varius.
            Ac odio tempor orci dapibus ultrices in iaculis. Euismod in pellentesque massa placerat.
            Arcu felis bibendum ut tristique.
            Orci a scelerisque purus semper eget duis at. Dictum fusce ut placerat orci nulla.
            Rhoncus dolor purus non enim praesent. Auctor neque vitae tempus quam pellentesque nec.
            Vitae turpis massa sed elementum tempus. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor.
            Urna neque viverra justo nec ultrices dui sapien. Arcu cursus vitae congue mauris rhoncus.
            Laoreet sit amet cursus sit amet dictum sit amet. Gravida dictum fusce ut placerat orci nulla.
          </article>
          <article class="content" style="background-color: white;">
            <h1>It is back of page 4</h1>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Augue ut lectus arcu bibendum at varius.
            Ac odio tempor orci dapibus ultrices in iaculis. Euismod in pellentesque massa placerat.
            Arcu felis bibendum ut tristique.
            Orci a scelerisque purus semper eget duis at. Dictum fusce ut placerat orci nulla.
            Rhoncus dolor purus non enim praesent. Auctor neque vitae tempus quam pellentesque nec.
            Vitae turpis massa sed elementum tempus. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor.
            Urna neque viverra justo nec ultrices dui sapien. Arcu cursus vitae congue mauris rhoncus.
            Laoreet sit amet cursus sit amet dictum sit amet. Gravida dictum fusce ut placerat orci nulla.
          </article>
        </div>
        <div class="page back">
          <article class="content" style="background-color: #bca98a;" />
          <article class="content" style="background-color: #bca98a;" />
        </div>
      </booklet>
    </div>


    <b-button size="lg" variant="primary" class="mb-2 mx-3"  @click="$refs.Book.prevPage()">
      <b-icon icon="arrow-left" aria-label="Help"></b-icon>
    </b-button>
  
    <b-button size="lg" variant="primary" class="mb-2 mx-3"  @click="start">
      <b-icon icon="app" aria-label="Help" v-if="playing"></b-icon>
      <b-icon icon="play" aria-label="Help" v-else></b-icon>
    </b-button>

    <b-button size="lg" variant="primary" class="mb-2 mx-3"  @click="$refs.Book.nextPage()">
      <b-icon icon="arrow-right" aria-label="Help"></b-icon>
    </b-button>

  </div>
</template>

<script>
import booklet  from 'vue-booklet'

import sound1 from "./eval-135000-1.wav"
import sound2 from "./eval-135000-2.wav"

export default {
  name: 'ReadBook',
  components: {
    booklet 
  },
  data() {
    return {
      files: [
        sound1,
        sound2,
      ],
      audio: new Audio(),
      index: 0,
      playing: false,
    }
  },
  methods: {
    start() {
      if(this.playing) {
        this.audio.pause();
        this.playing = false;
        
      } else {
        this.playing = true;
        // 텍스트 하이라이팅
        this.audio = new Audio(this.files[this.index])
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
  }
}
</script>
