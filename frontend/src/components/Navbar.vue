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
            <a style="cursor: pointer" @click="logOut" class="nav-link">Log out as {{ userName }}</a>
          </li>

        </ul>
<!--        <form class="form-inline my-2 my-lg-0">-->
<!--          <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">-->
<!--          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>-->
<!--        </form>-->
      </div>
    </nav>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "navbar",
   methods: {
    async logOut () {
      try {
        const response = await axios.post('/auth/token/logout/');
        console.log(response)
        if (response.status === 204) {
          this.$store.commit('removeToken')
          this.$router.push('log-in')
        }
      } catch (e) {
        console.log(e)
        alert('Error')
      }},
  },
  computed: {
    ...mapState({
      isAuthenticated: state => state.isAuthenticated,
      userName: state => state.userName
    }),
  },
}
</script>

<style scoped>

</style>