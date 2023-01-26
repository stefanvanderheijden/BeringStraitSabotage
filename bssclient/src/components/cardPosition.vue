<template>
  <div
    class="card"
    :class="{ focus: isFocus, striped: card.activated }"
    @click="setNewMessage()"
    @focus="handleFocus"
    @focusout="handleFocusOut"
    tabindex="-1"
  >
    <div v-if="card.special">...!</div>
  </div>
</template>

<script>
export default {
  name: "cardPosition",
  components: {},
  data: function () {
    return {
      isActive: false,
      isFocus: false,
    };
  },
  props: {
    primaryColor: String,
    secondaryColor: String,
    card: Object,
  },
  methods: {
    setNewMessage() {
      var message = "";
      if (this.card.activated) {
        message += "Position already activated. \n";
      }

      message += this.card.description;
      this.$store.commit("setNewMessage", message);
    },

    handleFocus() {
      this.isFocus = true;
    },
    handleFocusOut() {
      this.isFocus = false;
    },
  },
};
</script>

<style scoped>
.card {
  height: 25px;
  text-align: center;
  color: var(--text-color);
  cursor: pointer;
  width: 100%;
  border: var(--line-thick);
  margin: 4px;
}

.nonStriped {
  background-image: none;
}

.striped {
  background-image: linear-gradient(
    -45deg,
    rgb(255, 255, 255) 25%,
    transparent 25%,
    transparent 50%,
    rgb(255, 255, 255) 50%,
    rgb(255, 255, 255) 75%,
    transparent 75%,
    transparent
  );
  background-size: 6px 6px;
}

.focus {
  outline: 1px solid white;
}
</style>
