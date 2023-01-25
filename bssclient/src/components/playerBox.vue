<template>
  <div class="player">
    <div class="lineBottom"></div>
    <div class="vote stdRow">{{ player.id }}</div>
    <div class="icon">{{ player.emoticon }}</div>
    <div class="stdRow name">{{ player.name }}</div>
    <div class="role stdRow">
      <div v-if="player.chancellor">
        {{ $store.state.dictionary.Chancellor }}
      </div>
      <div v-if="player.president">
        {{ $store.state.dictionary.President }}
      </div>
    </div>
    <div class="notHitler stdRow">
      <div v-if="player.confirmed_not_hitler">Not Hitler</div>
    </div>
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
  /* background-color: rgb(34, 56, 77); */
  color: rgb(210, 218, 223);
  position: relative;
  height: 100%;
  display: grid;
  grid-template-columns: 0.1fr 0.5fr 1fr 1fr 1fr;
  font-size: 1rem;
}

.lineBottom {
  width: 100%;
  height: 1px;
  position: absolute;
  bottom: 15px;
  align-self: center;
  text-align: center;
  background: white;
  box-shadow: 0px 0px 5px 0px rgba(255, 255, 255, 0.8);
}

.stdRow {
  height: 1.5rem;
  align-self: center;
  display: flex;
  align-items: center;
  padding: 2px;
  font: 0.7rem Inconsolata, monospace;
  text-shadow: 0 0 5px #ffffff;
}
.vote {
  height: 1.5rem;
  grid-row: 1;
  grid-column: 1;
}

.vote.no {
  background-color: red;
}

.vote.yes {
  background-color: green;
}
.icon {
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  font-size: 2rem;
  text-align: center;
  grid-row: 1;
  grid-column: 2;
  box-shadow: 0px 0px 5px 0px rgba(255, 255, 255, 0.7);
  border: 1px solid white;
  background-color: rgb(10, 14, 18);
  z-index: 10;
  text-shadow: 0 0 5px #ffffff;
}
.name {
  grid-row: 1;
  grid-column: 3;
}
.role {
  grid-row: 1;
  grid-column: 4;
}
.notHitler {
  align-self: center;
  grid-row: 1;
  grid-column: 5;
}
</style>
