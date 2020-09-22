<template>
  <div>
    <!-- NavBar -->
    <b-navbar>

      <!-- 나랑노랑 -->
      <b-navbar-brand class="main-narang-norang" @click="onRoute('Main')">
        <div class="row ml-4">
          <p class="main-blue-narang mb-0">나랑</p>
          <p class="main-yellow-norang mb-0">노랑</p>
        </div>
      </b-navbar-brand>
      
      <!-- 나랑노랑 Logo-Image -->
      <b-navbar-brand class="mr-auto ml-auto">
        <img src="../assets/img/나랑노랑.png" alt="" style="width: 80px;">
      </b-navbar-brand>

      <!-- SideBar Nav -->
      <b-navbar-nav class="ml-auto">
				<b-button v-b-toggle.sidebar-right class="my-2 my-sm-0 mr-3"><b-icon icon="list" scale="2.5"></b-icon></b-button>       
      </b-navbar-nav>

    <!-- End NavBar -->
    </b-navbar>

    <b-sidebar id="sidebar-right" right shadow backdrop-variant="dark" backdrop> 

      <b-card no-body style="min-height: 100%;">
        <b-card-text class="mt-4 mb-0">
          <b-avatar class="mr-3"></b-avatar>
          <span class="mr-auto"> ~ 님 환영합니다.</span>
          <hr>
        </b-card-text>

        <b-card-body class="p-2">
          <b-container>
            <strong>현재 목소리 - 엄마</strong>
            <b-row>
              <b-col cols="6" class="py-3">
                <b-card bg-variant="info">
                  <b-avatar size="lg" rounded="lg" text="엄마" variant="info"></b-avatar>
                </b-card>
              </b-col>
              <b-col cols="6" class="py-3">
                <b-card>
                  <b-avatar size="lg" rounded="lg" src="https://placekitten.com/300/300"></b-avatar>
                </b-card>
              </b-col>
              <b-col cols="6" class="py-3">
                <b-card>
                  <b-avatar class="plus-icon" size="lg" rounded="lg" icon="plus"></b-avatar>
                </b-card>
              </b-col>
            </b-row>
          </b-container>
        </b-card-body>

        <b-list-group>
          <b-list-group-item href="#" @click="onRoute('MyBook')">내 서재</b-list-group-item>
          <b-list-group-item href="#" @click="onRoute('Voice')">새로운 목소리</b-list-group-item>
          <!-- <b-list-group-item href="#">Not yet...</b-list-group-item> -->
        </b-list-group>
      </b-card>

      <template v-slot:footer="{}">
       <div class="d-flex align-items-center px-3 py-2">
        <div class="row ml-1">
          <p class="footer-blue-narang mb-0">나랑</p>
          <p class="footer-yellow-norang mb-0">노랑</p>
        </div>
        <b-button class="ml-auto" v-b-modal.cs @click="onRoute('CS')">
          <b-icon icon="headset" aria-hidden="true"></b-icon> 고객센터
        </b-button>
       </div>
      </template>

    </b-sidebar>

  </div>
</template>

<script>

export default {
  name: "TopNavigation",
  data() {
    return {   
    }
  },
  methods: {
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    }
  }
}
</script>

<style>
.main-narang-norang {
  font-family: 'Jua', sans-serif;
  margin-right: 15vw;
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
</style>