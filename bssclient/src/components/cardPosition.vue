<template>
  <div class="card" :style="style"></div>
</template>

<script>
export default {
  name: "cardPosition",
  components: {},
  props: {
    primaryColor: String,
    secondaryColor: String,
    card: Object,
  },
  computed: {
    style() {
      return {
        backgroundColor: this.card.activated
          ? this.primaryColor
          : this.secondaryColor,
      };
    },
  },
};
</script>

<style scoped>
.card {
  text-align: center;
  height: 20px;
  width: 100%;
  margin: 0px 2px;
}
</style>
