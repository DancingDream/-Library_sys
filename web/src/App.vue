<template>
  <div id="app">
    <Home />
    <Bookrack />
  </div>
</template>

<script>

import Home from '@/components/Home'
import Bookrack from '@/views/Bookrack'

export default {
  name:"app",
  components:{
    Home,
    Bookrack
  }
}

    Home</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


</style>
