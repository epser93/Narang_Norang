<template>
  <div class="container d-flex">
    <div class="row m-0 p-0">

      <!-- 나랑 -->
      <div class="col-4 float-left" style="margin-top: 70px;">
        <kinesis-container class="float-left">
          <div class="row">
            <kinesis-element class="home" type="rotate" :strength="20" style="width: 25%;">
              <img alt="분홍ㄴ" src="../assets/login_img/분홍ㄴ.png">
            </kinesis-element>
            <kinesis-element class="home" type="depth" :strength="20" style="width: 20%;">
              <img alt="노랑ㅏ" src="../assets/login_img/노랑ㅏ.png">
            </kinesis-element>
          </div>
          <div class="row">
            <kinesis-element class="home" type="depth" :strength="-50" style="width: 30%;">
              <img alt="분홍ㄹ" src="../assets/login_img/분홍ㄹ.png">
            </kinesis-element>
            <kinesis-element class="home" type="depth" :strength="-50" style="width: 25%;">
              <img alt="연두ㅏ" src="../assets/login_img/연두ㅏ.png">
            </kinesis-element>
          </div>
          <kinesis-element class="home" type="depth" :strength="-50" style="margin-top: -60px;">
            <img alt="하늘ㅇ" src="../assets/login_img/하늘ㅇ.png">
          </kinesis-element>
        </kinesis-container>
      </div>

      <!-- 노랑이 + 로그인 버튼 -->
      <div class="col-4 align-items-center" style="margin-top: 100px;">
        <div class="vertical login-main">
          <div>
            <img class="animated pulse infinite" src="@/assets/img/나랑노랑.png" alt="나랑노랑 로고" style="width: 95%;">
          </div>
          <div class="mt-4">
            <img class="kakao-login" src="@/assets/img/kakao_login_large_narrow.png" @click="onClick" alt="카카오 로그인 버튼" style="width: 70%;">
          </div>
        </div>
      </div>

      <!-- 노랑 -->
      <div class="col-4">
        <kinesis-container class="float-right align-items-center">
          <div class="vertical">
            <kinesis-element class="home" type="rotate" :strength="20" style="width: 15%;">
              <img alt="주황ㄴ" src="../assets/login_img/주황ㄴ.png">
            </kinesis-element>
            <kinesis-element class="home" type="depth" :strength="20" style="width: 20%; height: 20%; margin-top: -60px;">
              <img alt="파랑ㅗ" src="../assets/login_img/파랑ㅗ.png">
            </kinesis-element>
          </div>
          <div class="row">
            <kinesis-element class="home" type="depth" :strength="-50" style="width: 20%;">
              <img alt="노랑ㄹ" src="../assets/login_img/노랑ㄹ.png">
            </kinesis-element>
            <kinesis-element class="home" type="depth" :strength="-50" style="width: 20%;">
              <img alt="분홍ㅏ" src="../assets/login_img/분홍ㅏ.png">
            </kinesis-element>
          </div>
          <kinesis-element class="home" type="depth" :strength="-50" style="width: 30%; margin-top: -60px;">
            <img alt="연두ㅇ" src="../assets/login_img/연두ㅇ.png">
          </kinesis-element>
        </kinesis-container>
      </div>
    </div>
  </div>
</template>

<script>
// import About from './About.vue'
import { KinesisContainer, KinesisElement } from 'vue-kinesis'

export default {
  name: 'Login',
  methods: {
    onClick() {
      // 로그 잘 찍힘
      console.log('want to login')
    }
  },
  components: {
    // About,
    KinesisContainer,
    KinesisElement,
  }
}
</script>

<style>
.login-main {
  margin-top: 60px;
}

.kakao-login {
  cursor: pointer;
}
</style>