<template>
  <div class="player">
    <div v-if="player.chancellor" class="chancellor">Chancellor</div>
    <div v-if="player.president" class="president">President</div>
    <div class="player-emoticon">{{ player.emoticon }}</div>
    <div class="player-name">{{ player.name }}</div>
    <div class="chair">Chair {{ player.chair_number }}</div>
  </div>
</template>

<script>
export default {
  name: "playerBox",
  components: {},
  props: {
    player: Object,
  },
};
</script>

<style scoped>
.player {
  position: relative;
  padding-top: 16px;
}
.chancellor {
  border-radius: 5px;
  padding: 1px;
  top: 0px;
  position: absolute;
  font-size: 10px;
  text-align: center;
  background-color: yellow;
}
.president {
  border-radius: 5px;

  padding: 1px;
  top: 0px;
  position: absolute;
  font-size: 10px;
  text-align: center;
  background-color: orange;
}
.player-emoticon {
  border: 2px solid grey;
  font-size: 40px;
  text-align: center;
  background-color: white;
  border-radius: 5px;
  margin: 5px;
}

.player-name {
  font-size: 15px;
  text-align: center;
}

.chair {
  font-size: 10px;
  text-align: center;
}
</style>
