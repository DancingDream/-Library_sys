<template>
  <div>
    <p>图书馆书本总量：{{ data.bookNum }}</p>
    <p>今日还书人数：{{ data.reNum }}</p>
    <p>今日借书人数：{{ data.boNum }}</p>
  </div>
</template>

<script>
import { getData } from "../../api/index";

export default {
  name: "",
  data() {
    return {
      data: {},
    };
  },

  methods: {
    initData() {
      getData().then((res) => {
        this.data = res.data;
      });
    },
  },

  mounted() {
    this.initData();
  },
};
</script>

<style scoped>
</style>