<template>

  <ul class="pagination justify-content-center">
       <li :class="{ 'page-item': true, 'disabled': back === null }">
         <a class="page-link" @click="fetchPostsPage(back)">&lt</a>
       </li>
       <li
           v-for="pageNumber in totalPages"
           :key="pageNumber"
           :class="{ 'page-item': true, 'active': page === pageNumber }"
       ><a class="page-link" @click="changePage(pageNumber)">{{pageNumber}}</a>
       </li>
       <li :class="{ 'page-item': true, 'disabled': next === null }">
         <a class="page-link" @click="fetchPostsPage(next)">&gt</a>
       </li>
     </ul>
</template>

<script>
import axios from "axios";

export default {
  name: "paginator",
  props: {
    back: {
      type: [String, null],
      default: null
    },
    next: {
      type: [String, null],
      default: null
    },
    page: {
      type: Number,
      required: true,
    },
    totalPages: {
      type: Number,
      required: true,
    }
  },
  methods: {
    fetchPostsPage(url) {
      this.$emit('movePage', url)
    },

    changePage (pageNumber) {
      this.$emit('changePage', pageNumber);
    },
  },
}
</script>

<style scoped>

</style>