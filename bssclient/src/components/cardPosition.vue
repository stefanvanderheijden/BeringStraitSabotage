<template>
  <div
    class="card"
    :class="{ focus: isFocus }"
    :style="style"
    @click="setNewMessage()"
    @focus="handleFocus"
    @focusout="handleFocusOut"
    tabindex="-1"
  >
    <div v-if="card.special">... !</div>
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
  cursor: pointer;
  text-align: center;
  height: 24px;
  width: 100%;
  margin: 0px 2px;
  box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.4);
}

.focus {
  outline: 2px solid white;
}
</style>
