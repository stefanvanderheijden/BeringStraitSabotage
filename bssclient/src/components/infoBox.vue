// Vue component for the info box

<template>
  <div class="infoBox">
    {{ $store.state.infoBox.message }}
  </div>
</template>

<script>
export default {
  name: "infoBox",
  components: {},
  computed: {},
};
</script>

<style scoped>
.infoBox {
  white-space: pre-wrap;
  margin: 8px;
  color: var(--text-color);
  width: 70%;
  overflow: hidden;
  text-align: left;
  font: 0.8rem Inconsolata, monospace;
  height: 2rem;
}

::selection {
  background: #0080ff;
  text-shadow: none;
}
</style>
