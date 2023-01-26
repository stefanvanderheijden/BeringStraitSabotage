<template>
  <div class="windowMain">
    <windowHeader :title="title" @toggleVisible="toggleVisible" />
    <div v-if="visible">
      <slot></slot> <windowFooter :author="author" :scale="scale" :rev="rev" />
    </div>
  </div>
</template>

<script>
import windowHeader from "./windowHeader.vue";
import windowFooter from "./windowFooter.vue";
export default {
  name: "windowMain",
  components: {
    windowHeader,
    windowFooter,
  },
  props: {
    title: String,
    author: String,
    scale: String,
    rev: String,
  },
  data: function () {
    return {
      visible: true,
    };
  },
  methods: {
    toggleVisible(visibility) {
      this.visible = visibility;
      console.log("toggleVisible: " + visibility);
    },
  },
};
</script>

<style scoped>
.windowMain {
  position: relative;
  background-color: var(--background-color);
  font-family: var(--computer-font);
  color: var(--text-color);
  margin: 5px;
  border: var(--line-thick);
}
</style>
