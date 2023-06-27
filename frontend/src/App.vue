<template>
  <navbar></navbar>

  <div class="app">
    <router-view></router-view>
  </div>
</template>
<script>
import axios from 'axios'
import navbar from "@/components/Navbar.vue";
export default {
  name: 'App',
  components: {
    navbar
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },

}

</script>
<style>

</style>
