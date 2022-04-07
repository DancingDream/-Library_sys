<template>
    <el-container class="clear">
        <el-header>
            <Header></Header>    
        </el-header>
        
        <el-container >
            <el-aside width="150px">
                <Menu :menuList="this.$store.state.menus.children"></Menu>
            </el-aside>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    import Header from "../components/header.vue";
    import Menu from "../components/menu.vue";

    export default {
        name: '',
        data() {
            return {
               
              isRouterAlive: true
     
            };
        },

        

        components:{
            Header,
            Menu
        },

        methods:{
          reload () {
            this.isRouterAlive = false
            this.$nextTick(function () {
              this.isRouterAlive = true
            })
          }
        }
    }
</script>

<style  scoped>
  .el-header{
    background-color: #66CC99;
    color: #333;
    text-align: center;
    line-height: 60px;
    border-bottom: 1px solid #fff;
    width: 100%;
    position: fixed;
  }

  .el-aside {
    width: 200px !important;
    background-color: #66CC99;
    text-align: center;
    line-height: 200px;
    height: 93.5vh;
    position: fixed;
    top:60px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    /* line-height: 160px; */
    position: fixed;
    top:60px;
    left: 200px;
    height: 93.5vh;
    width: 180vh;
  }
  .el-container{
    height: 100%;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
   



</style>