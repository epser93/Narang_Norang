<template>
  <div v-if="userInfo">
    <!-- NavBar -->
    <b-navbar class="top-nav">

      <!-- 나랑노랑 -->
      <b-navbar-brand href="#" class="main-narang-norang" @click="onRoute('Main')">
        <div class="row ml-4">
          <p class="main-blue-narang mb-0">나랑</p>
          <p class="main-yellow-norang mb-0">노랑</p>
        </div>
      </b-navbar-brand>
      
      <!-- 나랑노랑 Logo-Image -->
      <b-navbar-brand class="mr-auto ml-auto">
        <img src="../assets/img/나랑노랑.png" alt="" style="width: 100px;">
      </b-navbar-brand>

      <div @click="onRoute('Books')" size="lg" variant="outline-secondary" class="book-plus mr-2" style="position: absolute; right: 8%;">
        <b-icon icon="book" scale="1.5" aria-hidden="true" class="mr-2"></b-icon>책 더보기
      </div>

      <!-- SideBar Nav -->
      <b-navbar-nav class="ml-auto">
				<b-button v-b-toggle.sidebar-right class="my-2 my-sm-0 mr-3"><b-icon icon="list" scale="2.5"></b-icon></b-button>     
      </b-navbar-nav>

    <!-- End NavBar -->
    </b-navbar>

  <!-- SideBar -->
    <b-sidebar id="sidebar-right" right shadow backdrop-variant="dark" backdrop> 
      <!-- Greeting Area -->
      <b-card no-body style="min-height: 100%;">
        <b-card-text class="mt-4 mb-0">
          <b-avatar class="mr-3"></b-avatar>
          <span class="mr-auto" @click="getsubscribes" v-b-modal.kakao-membership>
            {{(userInfo.first_name == '') ? userInfo.username : userInfo.first_name}}님 환영합니다.
          </span>
          <!-- <p style="font-size: 10px; margin-top: 15px;">이름을 클릭하면 결제 내역을 볼 수 있습니다.</p> -->
          <hr>
        </b-card-text>
        <b-card-text v-if="userInfo.is_subscribed" class="my-2">
          <span class="mr-auto" v-b-modal.kakao-membership>나랑노랑 멤버십</span>
          <hr>
        </b-card-text>
        <b-card-text v-else class="my-2">
          <span class="mr-auto" v-b-modal.kakao-pay>나랑노랑 멤버십 이용하기</span>
          <hr>
        </b-card-text>
        <!-- Voice Notice Area -->
        <b-card-body class="pt-0">
          <b-container>
            <strong><b-icon icon="mic-fill" scale="1"></b-icon>
             현재 목소리: {{ current_voice.name }}</strong>
            <hr style="margin-bottom: 0; border-bottom: 1px solid grey;">
            <b-row>
              <b-col cols="6" v-for="voice in voices" :key="voice.id" class="py-3">
                <b-card :bg-variant="voice.id == current_voice.id ? 'primary' : 'secondary'" @click="onChangeVoice(voice.id)" style="cursor: pointer;">
                  <p class="mt-3" style="color: white;"><strong>{{ voice.name }}</strong></p>
                </b-card>
              </b-col>
              <b-col cols="6" class="py-3">
                <b-card @click="onRoute('Voice')">
                  <b-avatar class="plus-icon" size="lg" rounded="lg" icon="plus"></b-avatar>
                </b-card>
              </b-col>
            </b-row>
          </b-container>
        </b-card-body>
        <!-- Menu Area -->
        <b-list-group>
          <b-list-group-item href="#" @click="onRoute('MyBook')">내 서재</b-list-group-item>
          <b-list-group-item href="#" @click="onRoute('UserInfo')">설정</b-list-group-item>
          <b-list-group-item href="#" @click="kakaoLogout()">로그아웃</b-list-group-item>
        </b-list-group>
      </b-card>
      <!-- Footer Area -->
      <template v-slot:footer="{}">
       <div class="d-flex align-items-center px-3 py-2">
        <div class="row ml-1">
          <p class="footer-blue-narang mb-0">나랑</p>
          <p class="footer-yellow-norang mb-0">노랑</p>
        </div>
        <b-button class="ml-auto" @click="onRoute('CS')">
          <b-icon icon="headset" aria-hidden="true"></b-icon> 고객센터
        </b-button>
       </div>
      </template>
    </b-sidebar>

    <b-modal
      id="kakao-pay"
      ref="modal"
      title="나랑노랑 멤버십 구독">
      <img src="@/assets/img/membership.png" style="width: 350px; margin-left: 60px;" alt="">
      <template v-slot:modal-footer="{ ok }">
        <b-button class="mr-auto ml-auto" @click="ok(); startKakaoPay();" variant="outline-primary">매달 4,800원 결제하기</b-button>
      </template>
    </b-modal>

    <b-modal id="kakao-membership" scrollable title="나랑노랑 이용내역" v-if="subscribes">
      <div v-if="(usage_history == 0)">
        <h4>이용 내역이 없습니다.</h4>
      </div>
      <div v-for="subscribe in subscribes" :key="subscribe.id" >
        <hr>
        <p><strong>결제가 완료 되었습니다.</strong></p>
        <p>결제일시: {{ subscribe.start_date }}</p>
        <p>만료일시: {{ subscribe.end_date }}</p>
        <b-button v-if="subscribe.is_return" disabled variant="secondary"> 결제 취소됨</b-button>
        <b-button v-else @click="onRefund(subscribe.tid)" variant="outline-danger"> 환불하기 </b-button>
        <hr>
      </div>

      <template v-slot:modal-footer="{ cancel }">
        <b-button @click="cancel();" variant="outline-secondary">닫기</b-button>
      </template>
    </b-modal>
  </div>
</template>

<script>
import cookies from 'vue-cookies'
import { mapState, mapActions } from 'vuex'

export default {
  name: "TopNavigation",
  computed: {
    ...mapState('user', ['userInfo', 'subscribes']),
    ...mapState('voice', ['voices']),
    usage_history() {
      return this.subscribes.length
    },
    current_voice()  {
      for(var i=0; i<this.voices.length; i++) {
        if(this.voices[i].id == this.userInfo.current_voice) {
          return this.voices[i]
        } 
      } return { name: '' }
    }
  },
  methods: {
    ...mapActions('user', ['getUserInfo', 'startKakaoPay', 'getsubscribes', 'delsubscribe']),
    ...mapActions('voice', ['getVoices', 'postVoice']),
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
    kakaoLogout() {
      if (!window.Kakao.Auth.getAccessToken()) {
        cookies.remove('auth-token')
        window.location.reload(true)
        alert("로그아웃 되었습니다.")
        return
      }
      window.Kakao.Auth.logout(function() {
        // console.log('logout ok\naccess token -> ' + window.Kakao.Auth.getAccessToken())
        cookies.remove('auth-token')
        window.location.reload(true)
        alert("로그아웃 되었습니다.")
      })
    },
    onRefund(tid) {
      if (confirm("정말 결제를 취소하시겠습니까??") == true) { 
        this.delsubscribe({ tid: tid})
      }
    },
    onChangeVoice(vid) {
      if (confirm("목소리를 변경하시겠습니까??") == true) { 
        if (this.current_voice.id == vid) {
          alert("현재 목소리로는 변경할 수 없습니다.")
        } else {
          this.postVoice(vid)
        }
      }
    },
  },
  created() {
    this.getUserInfo()
    this.getVoices()
  }
}
</script>

<style>
.main-narang-norang {
  font-family: 'Jua', sans-serif;
  margin-right: 15vw;
}

.main-narang-norang:hover {
  cursor: pointer;
}

.main-blue-narang {
  color: #89aef3;
  font-size: 40px;
}

.main-yellow-norang {
  color: #f9da45;
  font-size: 40px;
}

.btn-secondary {
  color: grey;
  border: none;
  border-color: none;
  background-color: white;
}

.btn-secondary:hover {
  color: grey;
  border: none;
  border-color: none;
  background-color: white;
}

.btn-secondary:focus {
  color: grey;
  border: none;
  border-color: white;
  background-color: white;
}

.footer-blue-narang {
  color: #89aef3;  
  font-family: 'Jua', sans-serif;
  font-size: 20px;
}

.footer-yellow-norang {
  color: #f9da45; 
  font-family: 'Jua', sans-serif; 
  font-size: 20px;
}

.plus-icon {
  color: grey;
  background-color: white;
}

.plus-icon:hover {
  cursor: pointer;
}

.top-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: white;
  z-index: 7;
}

.book-plus:hover {
  cursor: pointer;
}
</style>