<template>
 <div class="form-group row">
    <div class="col-sm-10">
      <button type="submit" class="btn btn-primary"><slot></slot></button>
    </div>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
export default {
  name: "post-button"
}
</script>

<style scoped>

</style>