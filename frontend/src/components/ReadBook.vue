<template>
  <div>
    <div v-for="(file, i) in files" :key="i">
      <p @click="readMe(i)">{{file}}</p>
    </div>
    <button @click="start">{{playing ? "stop" : "play"}}</button>
    <p>{{index}}</p>

    <booklet :displayPageNumber="false" :enableSelectPage="false">
      <div class="page cover">
        <article class="content">
          <h1>My first book</h1>
        </article>
      </div>
      <div class="page">
        <article class="content">
          <h1>Hello World !</h1>
          <p>Using vue-booklet to create a book which can fliped.</p>
          <p>Please feel free to use it.</p>
        </article>
      </div>
      <div class="page">
      <article class="content">
        <h1>Hello World !</h1>
        <p>Using vue-booklet to create a book which can fliped.</p>
        <p>Please feel free to use it.</p>
      </article>
    </div>
    <div class="page">
      <article class="content">
        <h1>Hello World !</h1>
        <p>Using vue-booklet to create a book which can fliped.</p>
        <p>Please feel free to use it.</p>
      </article>
    </div>
    </booklet>
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
        sound1,
        sound2,
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
      } else {
        this.index = i
        this.start()
      }
    },
  }
}
</script>
