<template>

    <form @submit.prevent class="form">
    <h4 class="form-title">New post</h4>
      <post-input
          v-model="post.title"
          type="text"
          placeholder="Title"
      />
      <post-input
          v-model="post.description"
          type="text"
          placeholder="Description"
          style="min-height: 100px;"
      />
      <textarea
          class="input"
          v-model="post.content"
          placeholder="Content"
          @keydown.enter="createNewParagraph"
          style="min-height: 300px;">
      </textarea>

      <post-button style="align-self: flex-start" @click="createPost">Create new post</post-button>
  </form>
</template>

<script>
import PostInput from "@/components/UI/PostInput.vue";
import PostButton from "@/components/UI/PostButton.vue";
export default {
  name: 'post-form',
  components: {
    PostButton,
    PostInput,
  },
  data(){
    return {
      post: {
        title: '',
        description: '',
        content: '',
      }
    }
  },
  methods: {
    createPost(){
      this.$emit('create', this.post)
      this.post = {
        title: "",
        content: "",
        description: "",
      }
    },
    createNewParagraph(event) {
      if (event.keyCode === 13) {
        const textArea = event.target;
        const currentText = textArea.value;
        const selectionStart = textArea.selectionStart;
        const selectionEnd = textArea.selectionEnd;

        const newText = currentText.slice(0, selectionStart) + '\n' + currentText.slice(selectionEnd);
        textArea.value = newText;
        textArea.selectionStart = textArea.selectionEnd = selectionStart + 1;
        event.preventDefault();
      }
    }
  }
}
</script>

<style scoped>

.input {
  display: inline-block;
  width: 100%;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #495057;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  padding: 10px 15px;
  margin-bottom: 15px;
}


</style>