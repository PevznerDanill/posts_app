<template>

  <form @submit.prevent="submitForm" class="form-signin">
    <div class="text-center mb-4">
      <h1 class="h3 mb-3 font-weight-normal">Create an account</h1>
      <p>Better experience. An authenticated user can leave comments</p>
    </div>

    <div class="form-label-group">
      <input v-model="username" type="text" id="inputEmail" class="form-control" placeholder="Username" required autofocus>
      <label for="inputEmail"></label>
    </div>

    <div class="form-label-group">
      <input v-model="password" type="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <label for="inputPassword"></label>
    </div>

    <button class="btn btn-lg btn-primary btn-block" type="submit">Sign up</button>
  </form>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from "axios"
export default {
  name: "SignUp",
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
        const response = await axios.post('/api/auth/users/', formData);
        if (response.status === 201) {
          await axios
              .post('/auth/token/login/', formData)
              .then(response => {
                console.log(response)
                const token = response.data.auth_token
                this.$store.commit('setToken', token)
                axios.defaults.headers.common['Authorization'] = 'Token ' + token
                localStorage.setItem("token", token)
                this.$router.push('/')
              })
              .catch(error => {
                console.log(error)
              })

        }

        console.log(response);
      } catch (e) {
        alert('Error')
      }
    }
  }
}
</script>

<style scoped>

.form-signin {
    width: 100%;
    max-width: 420px;
    padding: 15px;
    margin: 200px auto;
}

</style>