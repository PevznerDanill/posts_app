<template>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <router-link class="navbar-brand" to="/">My posts</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
          <li v-if="!isAuthenticated" class="nav-item active">
            <router-link class="nav-link" to="/sign-up">Sign Up <span class="sr-only">(current)</span></router-link>
          </li>
          <li v-if="!isAuthenticated" class="nav-item active">
            <router-link class="nav-link" to="/log-in">Login</router-link>
          </li>
           <li v-if="isAuthenticated" class="nav-item active">
            <a style="cursor: pointer" @click="logOut" class="nav-link">Log out</a>
          </li>

        </ul>
<!--        <form class="form-inline my-2 my-lg-0">-->
<!--          <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">-->
<!--          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>-->
<!--        </form>-->
      </div>
    </nav>
  <div class="app">
    <router-view></router-view>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if ( token ) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  methods: {


  async logOut () {
   try {
        const response = await axios.post('/auth/token/logout/');
        console.log(response)
        if (response.status === 204) {
          this.$store.commit('removeToken')
          axios.defaults.headers.common['Authorization'] = ''
          localStorage.clear()
          this.$router.push('log-in')
        }
      } catch (e) {
        console.log(e)
        alert('Error')
      }}
  },
  computed: {
    isAuthenticated() {
      console.log(this.$store.state.isAuthenticated)
      return this.$store.state.isAuthenticated;
    },
  },
}

</script>
<style>

</style>
