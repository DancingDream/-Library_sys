<template>
    <el-container>
        <el-header>
            <Header></Header>    
        </el-header>
        
        <el-container>
            <el-aside width="200px">
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
                
            };
        },

        components:{
            Header,
            Menu
        },

        methods:{

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
  }

  .el-aside {
    width: 200px !important;
    background-color: #66CC99;
    text-align: center;
    line-height: 200px;
    height: 93.5vh;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    /* line-height: 160px; */
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