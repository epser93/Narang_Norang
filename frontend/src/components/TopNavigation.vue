<template>
  <div>
    <b-navbar type="dark" variant="secondary">
      <b-navbar-brand @click="onRoute('Main')">나랑노랑</b-navbar-brand>

      <b-navbar-nav class="ml-auto">

				<b-button v-b-toggle.sidebar-right class="my-2 my-sm-0"><b-icon icon="list"></b-icon></b-button>
        
      </b-navbar-nav>
    </b-navbar>

    <b-sidebar id="sidebar-right" right shadow backdrop-variant="dark" backdrop> 

      <b-card no-body style="min-height: 100%;">
        <b-card-text class="mt-4">
          <b-avatar class="mr-3"></b-avatar>
          <span class="mr-auto"> ~ 님 환영합니다</span>
        </b-card-text>

        <b-card-body>
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
                  <b-avatar size="lg" rounded="lg" icon="plus"></b-avatar>
                </b-card>
              </b-col>
            </b-row>
          </b-container>
        </b-card-body>

        <b-list-group>
          <b-list-group-item v-b-modal.mb @click="onRoute('MyBook')">내 서재</b-list-group-item>
          <b-list-group-item href="#">Not yet...</b-list-group-item>
          <b-list-group-item href="#">Not yet...</b-list-group-item>
        </b-list-group>
      </b-card>

      <template v-slot:footer="{}">
       <div class="d-flex bg-dark text-light align-items-center px-3 py-2">
        <strong class="mr-auto">나랑노랑</strong>
        <b-button v-b-modal.cs @click="onRoute('CS')">
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
</style>