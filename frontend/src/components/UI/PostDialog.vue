<template>
  <div class="dialog" v-if="show" @click.stop="hideDialog">
    <div @click.stop class="dialog__content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import toggleMixin from "@/mixins/toggleMixin";

export default {
  name: "post-dialog",
  mixins: [toggleMixin]
}
</script>

<style scoped>
  .dialog {
    z-index: 1;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.5);
    position: fixed;
    display: flex;
    padding: 50px;
  }

  .dialog__content {
    z-index: 1;
    margin: auto;
    padding: 20px;
    background: white;
    border: white;
    border-radius: 12px;
    /*min-height: 500px;*/
    min-width: 500px;

  }
</style>