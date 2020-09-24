<template>
  <div>
    <button v-on:click="start">play</button>
    <vuetify-audio id="audio" :file="file" color="success" :ended="printConsole"></vuetify-audio>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        file: "http://127.0.0.1:8000/media/eval-135000.wav",
        count: 0,
        audio: new Audio(),
        check: true,
      }
    },
    components: {
        VuetifyAudio: () => import('vuetify-audio'),
    },
    methods: {
      start() {
        if(this.check === false) {
          this.audio.pause();
          console.log("재생중");
          this.check = true;
          return;
        }
        this.check = false;
        // 텍스트 하이라이팅
        this.audio = new Audio("http://127.0.0.1:8000/media/eval-135000.wav")
        this.audio.onended = () => {
          this.count++;
          this.check = true;
          this.start()
        }
        this.audio.play();
      },
      printConsole() {
        console.log('끝');
      },
    }
  }
</script>
