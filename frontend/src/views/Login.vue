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
            <img src="//k.kakaocdn.net/14/dn/btqCn0WEmI3/nijroPfbpCa4at5EIsjyf0/o.jpg" class="login-img" width="222" @click="loginWithKakao()" />
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
import { KinesisContainer, KinesisElement } from 'vue-kinesis'
import { mapGetters } from 'vuex'
import axios from 'axios'
import cookies from 'vue-cookies'
import swal from 'sweetalert'
import SERVER from '@/api/drf'

export default {
  name: 'Login',
  components: {
    KinesisContainer,
    KinesisElement,
  },
  computed: {
    ...mapGetters('user', ['isLoggedIn'])
  },
  methods: {
    loginWithKakao() {

      window.Kakao.Auth.login({
        success({ access_token }) {
          axios.post(SERVER.URL + SERVER.ROUTER.login,{ "access_token": access_token })
            .then(({ data }) => {
              cookies.set('auth-token', data.token)
              swal({
                title: (data.user.first_name == '') ? data.user.username + '님 환영합니다!!' : data.user.first_name + '님 환영합니다!!', 
                text: "나랑노랑",
                icon: "success",
                buttons: '확인'
              })
              setTimeout(function() {
                window.location.reload(true)
              }.bind(this), 1200)
            })
        },
        fail(err) {
          console.log(err)
        },
      })

    },
  },
}
</script>

<style>
.login-main {
  margin-top: 60px;
}

.login-img {
  cursor: pointer;
}

@keyframes pulse {
  from {
    background-color: transparent;
    transform: scale(.8)
  }
  to {
    background-color: transparent;
    transform: scale(.9)
  }
}
</style>