<template>

 <main role="main">
    <div class="jumbotron">
        <div class="container">
          <h1 class="display-3">My posts</h1>
          <p>These are the posts downloaded from the http://127.0.0.1:8000/api/posts/</p>
          <p v-if="is_superuser"><span class="btn btn-primary btn-lg" @click="showDialog" role="button">Create new post</span></p>
          <post-dialog v-model:show="dialogVisible">
            <post-form
            @create="createPost"
            />
          </post-dialog>
        </div>
    </div>
   <post-list
      :posts="posts"
      v-if="!isPostsLoading"
    />
    <div v-else class="lds-ellipsis">
      <div></div><div></div><div></div><div></div>
    </div>
    <div class="container btn__container">
      <button v-if="next" @click="fetchPostsPage(next)" class="btn btn-primary">
      Next
    </button>
    <button v-if="back" @click="fetchPostsPage(back)" class="btn btn-primary">
      Back
    </button>
    </div>


    </main>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import PostList from "@/components/PostList.vue";
import axios from 'axios';
import PostForm from "@/components/PostForm.vue";
import PostDialog from "@/components/UI/PostDialog.vue";
import PostButton from "@/components/UI/PostButton.vue";
import { mapState } from "vuex";


export default {
  components: {
    PostButton,
    PostDialog,
    PostList,
    PostForm,
  },
  name: "Main",

  data() {
    return {
      posts: [],
      dialogVisible: false,
      isPostsLoading: false,
      next: null,
      back: null,
    }
  },
  methods: {
    showDialog(){
      this.dialogVisible = true;
    },
    async createPost(post){
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/posts/', post);
        if (response.status === 201) {
          post.id = response.data.id;
          this.posts.unshift(post);
          this.dialogVisible = false;
        }
      } catch (e) {
        console.log(e)
        console.log(e.response)
        alert('Error')
      }

    },

    async fetchPosts() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/posts/');
        console.log(response)
        this.next = response.data.next
        this.back = response.data.previous
        this.posts = response.data.results;
      } catch (e) {
        alert('Error')
      }
    },
    async fetchPostsPage(url) {
      try {
        const response = await axios.get(url);
        console.log(response)
        this.next = response.data.next
        this.back = response.data.previous
        this.posts = response.data.results
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } catch (e) {
        alert('Error')
      }
    },

  },
  mounted() {
    this.fetchPosts();
  },
  computed: {
    ...mapState({
      is_superuser: state => state.isSuperUser,
    })
  }
}
</script>

<style scoped>
.page__wrapper {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.page {
  cursor: pointer;
}

.current-page {
  color: blue;
  font-weight: bold;
}

.btn__container {
  display: flex;
  gap: 30px;
}

</style>