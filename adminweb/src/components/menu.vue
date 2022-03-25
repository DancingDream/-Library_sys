<template>
    <div >
      <el-menu :default-active="this.$router.currentRoute.path" 
      background-color="#66CC99" text-color="#FFFFFF" active-text-color="#FFFFCC" router>
          <template v-for="(item, index) in menuList">
            <el-menu-item :key="index" :index="item.path">
                <span :class="item.icon"></span> 
                <span slot="title">{{ item.name }}</span>
            </el-menu-item>
          </template>
      </el-menu>
  </div>
</template>

<script>
    export default {
        name: '',
        props:{
            menuList: []
        },
        data() {
            return {
                
            }
        }
    }
</script>

<style scoped>
 /* .fater-left {
    /* position: fixed; 
    top: 0px;
    left: 0;
    bottom: 0;

    }  */
</style>