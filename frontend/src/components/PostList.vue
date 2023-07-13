<template>
  <div class="container">
      <div class="row" v-if="posts.length" >
        <transition-group name="post-list">
          <post-list-item
            v-for="post in posts"
            :post="post"
            :key="post.id"
        />
        </transition-group>

      </div>
      <h2 v-else style="color: red;">No posts</h2>
    <hr>
  </div>


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

.post-list-enter-active,
.post-list-leave-active {
  transition: all 0.4s ease;
}
.post-list-enter-from,
.post-list-leave-to {
  opacity: 0;
  transform: translateX(130px);
}
.post-list-move {
  transition: transform 0.4s ease;
}
</style>