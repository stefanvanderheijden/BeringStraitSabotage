<template>
  <div>
    <div class="title">{{ titleTop }}</div>
    <div class="cardLane">
      <cardPosition
        v-bind:key="card.position"
        v-for="card in cardLane"
        :card="card"
        :primaryColor="primaryColor"
        :secondaryColor="secondaryColor"
      />
    </div>
    <div class="title">{{ titleBottom }}</div>
  </div>
</template>

<script>
import cardPosition from "./cardPosition.vue";
export default {
  name: "cardLane",
  props: {
    titleTop: String,
    titleBottom: String,
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
.title {
  font-size: 0.5rem;
  font-weight: light;
  margin-left: 10px;
}

.cardLane {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding-left: 5px;
  padding-right: 5px;
}
</style>
