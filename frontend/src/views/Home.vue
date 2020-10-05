<template>
  <div>
    <top-navigation/>
    <router-view style="margin-top: 100px;"/>
  </div>
</template>

<script>
import TopNavigation from '@/components/TopNavigation'

export default {
  name: 'Home',
  components: {
    TopNavigation,
  }
}
</script>

