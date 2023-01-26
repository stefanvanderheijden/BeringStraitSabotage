<template>
  <div class="playerField">
    <div class="title">--> The Construction Crew &lt;--</div>
    <div
      v-bind:key="player.id"
      v-for="player in $store.state.players"
      class="player"
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
.title {
  text-shadow: 0 0 5px #ffffff;
  margin-top: 10px;
  margin-bottom: 10px;
  color: rgb(210, 218, 223);
  font-size: 2rem;
  text-align: center;
  font: 0.7rem Inconsolata, monospace;
}
.playerField {
  background-color: #5787c6;
  margin: 5px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 35px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: 0 0 20px 0px rgba(0, 0, 0, 0.4);
  border: 2px solid white;
}

.player {
  width: 100%;
  margin-top: 2px;
}
</style>
