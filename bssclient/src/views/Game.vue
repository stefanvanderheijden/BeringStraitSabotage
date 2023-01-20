<template>
  <div>Hello from the game page</div>

  <cardLane
    :cardLane="$store.state.democratic_lane"
    primaryColor="#6DD544"
    secondaryColor="#B6DA93"
  />
  <cardLane
    :cardLane="$store.state.fascist_lane"
    primaryColor="#8D5723"
    secondaryColor="#C2946F"
  />
  <playerField> </playerField>
</template>

<script>
import playerField from "../components/playerField.vue";
import cardLane from "../components/cardLane.vue";
export default {
  name: "GamePage",
  components: {
    playerField,
    cardLane,
  },
};
</script>
