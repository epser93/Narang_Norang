<template>
  <kinesis-container>

    <kinesis-element class="home" type="rotate" :strength="20">
      <img alt="Vue logo" src="../assets/logo.png">
    </kinesis-element>

    <kinesis-element class="home" type="depth" :strength="20">
      <img alt="Vue logo" src="../assets/logo.png">
    </kinesis-element>

    <kinesis-element class="home" type="depth" :strength="-50">
      <img alt="Vue logo" src="../assets/logo.png">
    </kinesis-element>

  </kinesis-container>
</template>

<script>
import { KinesisContainer, KinesisElement } from 'vue-kinesis'

export default {
  name: 'Home',
  components: {
    KinesisContainer,
    KinesisElement,
  }
}
</script>