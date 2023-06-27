<template>
<form @submit.prevent="submitForm" class="form-signin">
    <div class="text-center mb-4">
      <h1 class="h3 mb-3 font-weight-normal">Login</h1>
    </div>

    <div class="form-label-group">
      <input v-model="username" type="text" id="inputEmail" class="form-control" placeholder="Username" required autofocus>
      <label for="inputEmail"></label>
    </div>

    <div class="form-label-group">
      <input v-model="password" type="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <label for="inputPassword"></label>
    </div>

<!--    <div class="checkbox mb-3">-->
<!--      <label>-->
<!--        <input type="checkbox" value="remember-me"> Remember me-->
<!--      </label>-->
<!--    </div>-->
    <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
  </form>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'
export default {
  name: "LogIn",
  data () {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    async submitForm() {
      const formData = {
        username: this.username,
        password: this.password,
      }
      try {
        const response = await axios.post('/auth/token/login/', formData);
        console.log(response)
        if (response.status === 200) {
          const token = response.data.auth_token
          this.$store.commit('setToken', token)
          console.log(this.$store.state.userName)
          this.$router.push('/')
        }
      } catch (e) {
        console.log(e)
        alert('Error')
      }
    }
  }
}
</script>

<style>
.form-signin {
    width: 100%;
    max-width: 420px;
    padding: 15px;
    margin: 200px auto;
}

</style>