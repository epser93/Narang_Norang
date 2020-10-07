<template>
  <div>
    <top-navigation/>
    <router-view :style="`margin-top: 120px; min-height: ${height}px;`"/>
    <div class="footer">
      <div class="container-fluid footer-copyright text-center"> 
      </div>
      <div class="container-fluid footer-text">
        <p class="mb-1" style="color: grey;">&copy; 2020 Copyright: <a href="https://j3c206.p.ssafy.io/main"> 나랑노랑 </a> </p>
      </div> 
    </div>
  </div>
</template>

<script>
import TopNavigation from '@/components/TopNavigation'

export default {
  name: 'Home',
  components: {
    TopNavigation,
  },
  data() {
    return {
      height: screen.height - 180
    }
  }
}
</script>

<style>
.footer-copyright {
  background-color: #ffffff;
  height: 74px;
  background-image: url("~@/assets/img/footer.png");
  background-size: 270px;
}

.footer-text {
  background-color: #f9da45;
}
</style>