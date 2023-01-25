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
  methods: {
    setNewMessage() {
      var message = "TEST";

      // message += this.$store.infoBox.defaultMessage;
      this.$store.commit("setNewMessage", message);
    },
  },
};
</script>

<style scoped>
.cardLanes {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;

  padding: 10px;
}
</style>
