<template>
  <div class="insideContainer">
    <div class="containerHeader">
      <div class="headerTitle">{{ title }}</div>
    </div>
  </div>
</template>

<script>
import playerBox from "./playerBox.vue";

export default {
  name: "playerField",
  components: {
    playerBox,
  },
  props: {
    title: string,
  },
};
</script>

<style scoped>
.headerTitle {
  font-size: 20px;
  font-weight: bold;
  color: #ffffff;
}
</style>
