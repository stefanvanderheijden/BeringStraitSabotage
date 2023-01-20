<template>
  <div>playerfield</div>
  <div v-bind:key="player.id" v-for="player in $store.state.players">
    <playerBox :player="player" />
  </div>
</template>

<script>
import playerBox from "./playerBox.vue";

export default {
  name: "playerField",
  components: {
    playerBox,
  },
};
</script>

<style scoped></style>
