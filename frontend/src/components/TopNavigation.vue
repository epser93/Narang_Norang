<template>
  <div>
    <b-navbar type="dark" variant="secondary">
      <b-navbar-brand href="#">NavBar</b-navbar-brand>

      <b-navbar-nav class="ml-auto">

				<b-button v-b-toggle.sidebar-right class="my-2 my-sm-0"><b-icon icon="list"></b-icon></b-button>
        
      </b-navbar-nav>
    </b-navbar>

    <b-sidebar id="sidebar-right" title="Sidebar" right shadow :width="sidebar.width">
      <div class="px-3 py-2">
        <b-img src="https://picsum.photos/500/500/?image=54" fluid thumbnail @click="onSide"></b-img>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
export default {
  name: "TopNavigation",
  data() {
    return {
      sidebar: {
        width: '30%'
      }
       
    }
  },
  methods: {
    onSide() {
      this.sidebar.width = '100%'
    }
  }
}
</script>

<style>
</style>