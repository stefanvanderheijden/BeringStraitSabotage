<template>
  <div class="cardLane">
    <cardPosition
      v-bind:key="card.position"
      v-for="card in cardLane"
      :card="card"
      :primaryColor="primaryColor"
      :secondaryColor="secondaryColor"
    />
  </div>
</template>

<script>
import cardPosition from "./cardPosition.vue";
export default {
  name: "cardLane",
  props: {
    primaryColor: String,
    secondaryColor: String,
    cardLane: Object,
  },
  components: {
    cardPosition,
  },
};
</script>

<style scoped>
.cardLane {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 5px 0px;
}
</style>
