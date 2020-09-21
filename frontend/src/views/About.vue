<template>
  <kinesis-container>
    <div class="row">
      <kinesis-element class="home" type="rotate" :strength="20" style="width: 15%; height: 20%;">
        <img alt="분홍ㄴ" src="../assets/login_img/분홍ㄴ.png">
      </kinesis-element>
      <kinesis-element class="home" type="depth" :strength="20" style="width: 20%; height: 20%;">
        <img alt="노랑ㅏ" src="../assets/login_img/노랑ㅏ.png">
      </kinesis-element>
    </div>
    <div class="row">
      <kinesis-element class="home" type="depth" :strength="-50" style="width: 20%; height: 20%;">
        <img alt="분홍ㄹ" src="../assets/login_img/분홍ㄹ.png">
      </kinesis-element>
      <kinesis-element class="home" type="depth" :strength="-50" style="width: 20%; height: 20%;">
        <img alt="연두ㅏ" src="../assets/login_img/연두ㅏ.png">
      </kinesis-element>
    </div>
    <kinesis-element class="home" type="depth" :strength="-50" style="width: 30%; height: 20%;">
      <img alt="하늘ㅇ" src="../assets/login_img/하늘ㅇ.png">
    </kinesis-element>

  </kinesis-container>
</template>

<script>
import { KinesisContainer, KinesisElement } from 'vue-kinesis'

export default {
  name: 'About',
  components: {
    KinesisContainer,
    KinesisElement,
  }
}
</script>