<template>
  <div v-if="post" class="container post-container">
    <h1>{{post.title}}</h1>
    <p>{{post.description}}</p>
    <p>{{post.content}}</p>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'
export default {
  name: "PostPage",
  data() {
    return {
      post: null,
    }
  },
  methods: {
    async fetchPost(postId) {
      try {
        const response = await axios.get(`/api/posts/${postId}/`);
        console.log(response)
        this.post = response.data
      } catch (e) {
        alert('Error')
      }
    },
  },
  mounted() {
    const postId = this.$route.params.id;
    this.fetchPost(postId);
  }
}
</script>

<style scoped>
.post-container {
  margin-top: 200px;
}
</style>