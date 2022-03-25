<template>
    <div class="clear">
        <img class="logo" src="../assets/千库网_图书馆书架_元素编号12863483.png" alt="">
        <h1 class="title">图书管理系统</h1>
            <!-- <span>{{ msg }}</span> -->
        <el-dropdown @command="handleUser" class="fater-header-user">
            <span class="el-dropdown-link">个人中心</span>
            <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="info"> 个人信息</el-dropdown-item>
                <el-dropdown-item command="pwd"> 修改密码</el-dropdown-item>
                <el-dropdown-item command="exit"> 退出系统</el-dropdown-item>
            </el-dropdown-menu>
        </el-dropdown>

            <!-- <el-dialog
                title="修改信息" width="600px"
                :append-to-body="true" :visible.sync="showUpdInfoFlag">
                <el-form label-width="80px" :model="userForm">
                    <el-form-item label="用户姓名">
                        <el-input v-model="userForm.name" 
                        placeholder="请输入用户姓名…" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="手机号">
                        <el-input v-model="userForm.phone" 
                        placeholder="请输入手机号…" autocomplete="off"></el-input>
                    </el-form-item>  
                </el-form>
                 <div slot="footer" class="dialog-footer">
                    <el-button @click="showUpdInfoFlag = false">取 消</el-button>
                    <el-button type="primary" @click="updInfo()">确 定</el-button> -->
                <!-- </div> 
            </el-dialog> -->
    </div>
</template>

<script>
    import {exit, getLoginUser} from "../api/index";

    export default {
        name: '',
        data() {
            return {
                userForm: {
                    adminID: "",
                    passWord: "",
                    name: "",
                    jobNum :"",
                    phone :"",
                    addTime :"",
                },
                showUpdInfoFlag: false,
                msg :this.userForm.adminID,
            };
        },

        components:{
            
        },

        methods:{
            initUserForm() {
                this.userForm = {
                    id: "",
                    adminID: "",
                    passWord: "",
                    name: "",
                    jobNum: "",
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
                            sessionStorage.clear();
                            this.$router.push("/");
                        });
                    });
                }
            }
        }
    }
</script>

<style scoped>


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