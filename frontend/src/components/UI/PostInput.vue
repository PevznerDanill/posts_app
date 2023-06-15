<template>

  <input @keydown.enter="preventFormSubmission" :value="modelValue" @input="updateInput" class="input">

</template>

<script>

export default {
  name: "post-input",
  props: {
    modelValue: [String, Number]
  },
  methods: {
    updateInput(event) {
      this.$emit('update:modelValue', event.target.value)
    },
    preventFormSubmission(event) {
      if (event.keyCode === 13) {
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
.form-group {
  background-color: white;
}
.col-sm-10 {
  background-color: white;
}
</style>