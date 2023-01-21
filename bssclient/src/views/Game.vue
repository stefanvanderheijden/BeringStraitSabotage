<template>
  <div class="cardLanes">
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
    <infoBox />
  </div>

  <playerField> </playerField>
</template>

<script>
import playerField from "../components/playerField.vue";
import cardLane from "../components/cardLane.vue";
import infoBox from "../components/infoBox.vue";
export default {
  name: "GamePage",
  components: {
    playerField,
    cardLane,
    infoBox,
  },
};
</script>

<style scoped>
.cardLanes {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 20px;
  padding-bottom: 150px;
  background-image: url("../assets/iceCold.jpg");
  background-size: cover;
}
</style>
