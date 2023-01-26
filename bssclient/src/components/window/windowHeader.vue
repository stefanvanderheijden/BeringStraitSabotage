<template>
  <div class="headerBar">
    <div class="headerTitle">{{ title }}</div>
    <div class="toggleOpen" @click="toggleVisible()">{{ this.toggleText }}</div>
  </div>
</template>

<script>
export default {
  name: "windowHeader",
  props: {
    title: String,
  },
  data() {
    return {
      toggleText: "-",
      visible: true,
    };
  },
  methods: {
    toggleVisible() {
      this.visible = !this.visible;
      this.toggleText = this.visible ? "-" : "+";
      this.$emit("toggleVisible", this.visible);
    },
  },
};
</script>

<style scoped>
.headerBar {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border-bottom: var(--line-thick);
  margin-bottom: 10px;
}

.headerTitle {
  padding: 2px 8px;
  font-size: 0.8rem;
}

.toggleOpen {
  cursor: pointer;
  width: 20px;
  text-align: center;
  padding: 2px 4px;
  border-left: var(--line-thick);
  font-size: 1rem;
}
</style>
