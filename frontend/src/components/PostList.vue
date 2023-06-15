<template>
  <div v-if="posts.length > 0" class="container">
      <div class="row">
        <post-list-item
            v-for="post in posts"
            :post="post"
            :key="post.id"
        />

      </div>
    <hr>
  </div>

  <h2 v-else style="color: red;">No posts</h2>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import PostListItem from "@/components/PostListItem.vue";
export default {
  components: {PostListItem},
  props: {
    posts: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style scoped>

</style>