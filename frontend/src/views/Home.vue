<template>
  <div>
    <top-navigation/>
    <router-view/>
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

