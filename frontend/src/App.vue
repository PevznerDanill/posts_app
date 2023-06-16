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

    const token = this.$store.state.token

    if ( token ) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },

}

</script>
<style>

</style>
