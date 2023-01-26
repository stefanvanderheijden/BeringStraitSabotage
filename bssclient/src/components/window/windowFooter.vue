<template>
  <div class="box">
    <div class="author">{{ author }}</div>
    <div class="scale">{{ scale }}</div>
    <div class="rev">REVISION {{ rev }}</div>
  </div>
</template>

<script>
export default {
  name: "windowFooter",
  props: {
    author: String,
    scale: String,
    rev: String,
  },
};
</script>

<style scoped>
.box {
  position: absolute;
  bottom: 0;
  right: 0;
  border-left: var(--line-thick);
  border-top: var(--line-thick);
  display: grid;
  grid-template-columns: 50px 40px;
  grid-template-rows: 1fr 1fr;
}

.author {
  grid-row: 2;
  grid-column: 2;
  font-size: 0.5rem;
  border-left: var(--line-thick);
  padding: 5px;
  text-align: center;
}

.scale {
  grid-row: 2;
  grid-column: 1;
  font-size: 0.5rem;
  padding: 5px;
}

.rev {
  grid-row: 1;
  grid-column: 1;
  grid-column-end: 3;
  font-size: 0.5rem;
  border-bottom: var(--line-thick);
  padding: 5px;
}
</style>
