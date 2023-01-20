<template>
  <header>
    <h1>{{ title }}</h1>
    <appButton text="Add Task" color="black" />
  </header>
</template>

<script>
import appButton from "./appButton.vue";
export default {
  name: "appHeader",
  props: {
    title: String,
  },
  components: {
    appButton,
  },
};
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

h1 {
  font-size: medium;
}
</style>
