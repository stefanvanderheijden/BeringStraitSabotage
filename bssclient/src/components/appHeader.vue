<template>
  <header>
    <div class="left">{{ title }}</div>
    <div class="right">{{ subtitle }}</div>
  </header>
</template>

<script>
export default {
  name: "appHeader",
  props: {
    title: String,
    subtitle: String,
  },
  components: {},
};
</script>

<style scoped>
header {
  padding-top: 5px;
  position: relative;
  font-family: var(--computer-font);
  color: var(--text-color);
  font-size: 0.5rem;
  height: 15px;
}

.right {
  position: absolute;
  text-align: right;
  right: 10px;
}

.left {
  position: absolute;
  text-align: left;
  left: 10px;
}
</style>
