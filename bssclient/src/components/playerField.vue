<template>
  <div class="playerField">
    <div
      class="player-box"
      v-bind:key="player.id"
      v-for="player in $store.state.players"
    >
      <playerBox :player="player" />
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
};
</script>

<style scoped>
.player-box {
  background: lightgrey;
  border-radius: 5px;
  min-width: 20%;

  margin: 5px;
}
.playerField {
  border: 1px solid black;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
</style>
