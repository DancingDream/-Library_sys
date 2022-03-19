<template>
    <el-container>
        <el-header>
            <img class="logo" src="../assets/千库网_图书馆书架_元素编号12863483.png" alt="">
            <h1 class="title">图书管理系统</h1>
            <el-dropdown @command="handleUser" class="fater-header-user">
                <span class="el-dropdown-link">个人中心</span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="info">个人信息</el-dropdown-item>
                    <el-dropdown-item command="pwd">修改密码</el-dropdown-item>
                    <el-dropdown-item command="exit">退出系统</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </el-header>

        <!-- <el-container>
            <el-aside width="200px">Aside</el-aside>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container> -->
    </el-container>
</template>

<script>
     import {exit } from "../api/index";


    export default {
        name: '',
        data() {
            return {
                
            }
        },

        components:{
            
        },

        methods:{
            initUserForm() {
                this.userForm = {
                    id: "",
                    userName: "",
                    passWord: "",
                    name: "",
                    gender: "",
                    age: "",
                    phone: "",
                    token: this.$store.state.token
                };
            },
            showUpdInfoWin() {
                getLoginUser(this.$store.state.token).then((resp) => {
                    this.initUserForm();
                    this.userForm = resp.data;
                    this.showUpdInfoFlag = true;
            });
    },
            handleUser(comm){
                if(comm == "info"){
                    this.showUpdInfoWin();
                }
                else if(comm == "pwd"){

                }
                else if(comm == "exit"){
                    this.$confirm("确认要退出吗？", "系统提示", {
                        confirmButtonText: "确认",
                        cancelButtonText: "取消",
                        type: "warning",
                    }).then(() => {
                        exit(this.$store.state.token).then(() => {
                        this.$store.commit("clearToken");
                        this.$store.commit("clearMenus");
                        sessionStorage.clear();
                        this.$router.push("/");
                        });
                    });
                }
            }
        }
    }
</script>

<style  scoped>
  .el-header{
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
    border-bottom: 1px solid #fff;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  } 

    .logo{
        width: 60px;
        position: relative;
        float: left;   
    }

  .title{
      float: left;
      font-size: 20px;
      color: #fff;
  }

  .fater-header-user{
    position: absolute;
    right: 35px;
    float: right;
    color: #fff;
  }

</style>