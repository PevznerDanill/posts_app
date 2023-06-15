<template>
  <div class="col-md-4">
    <h2>{{ post.title }}</h2>
    <p>{{post.description}}</p>
    <p><router-link class="btn btn-secondary" :to="`/posts/${post.id}`" role="button">Read post</router-link></p>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
export default {
  props: {
    post: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style>

</style>