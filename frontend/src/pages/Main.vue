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
   <paginator
     :back="back"
     :next="next"
     :page="page"
     :total-pages="totalPages"
     @changePage="changePage"
     @movePage="movePage"
   >
   </paginator>

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
import Paginator from "@/components/Paginator.vue";


export default {
  components: {
    PostButton,
    PostDialog,
    PostList,
    PostForm,
    Paginator,
  },
  name: "Main",

  data() {
    return {
      posts: [],
      dialogVisible: false,
      isPostsLoading: false,
      totalPages: 0,
      page: 1,
      next: '',
      back: '',
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
    handlePostPage (response) {
      this.next = response.data.next;
      this.back = response.data.previous;
      this.posts = response.data.results;
      this.totalPages = response.data.total_pages;
      this.page = response.data.current_page;

    },
    changePage (pageNumber) {
      this.page = pageNumber;
    },
    async fetchPosts() {
      try {
        const response = await axios.get('/api/posts/', {
          params: {
            page: this.page,
          }
        });
        this.handlePostPage(response);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } catch (e) {
        alert('Error')
      }
    },
    async movePage(url) {
      try {
        const response = await axios.get(url);
        this.handlePostPage(response);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } catch (e) {
        alert('Error')
      }
    }

  },
  mounted() {
    this.fetchPosts();
  },
  computed: {
    ...mapState({
      is_superuser: state => state.isSuperUser,
    })
  },
  watch: {
    page() {
      this.fetchPosts()
    }
  }
}
</script>

<style scoped>

.jumbotron {
  background-color: rgba(0, 0, 0, 0);;
}


</style>