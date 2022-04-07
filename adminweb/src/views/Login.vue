<template>
  <div class="login-container">
    <div class="login-win">
      <div class="login-body">
        <h1 class="login-title">图书管理系统</h1>
        <div class="login-form">
          <el-form :model="loginForm" :rules="rules" ref="loginForm">
            <el-form-item style="margin-bottom: 30px" prop="adminID">
              <el-input
                type="text"
                v-model="loginForm.adminID"
                suffix-icon="el-icon-user-solid"
                placeholder="请输入您的账号"
              ></el-input>
            </el-form-item>
            <el-form-item prop="passWord">
              <el-input
                type="password"
                v-model="loginForm.passWord"
                suffix-icon="el-icon-lock"
                placeholder="请输入您的密码"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-link :underline="false" target="_blank">找回密码</el-link>
              <el-link :underline="false" target="_blank" @click="goRegister"
                >注册账号</el-link
              >
            </el-form-item>
            <el-form-item>
              <el-button
                style="width: 100%; background-color: #66cc99"
                @click="submitForm('loginForm')"
                type="primary"
                >用户登录</el-button
              >
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { login } from "../api/index.js";
import initMenu from "../utils/menu";

export default {
  data() {
    return {
      loginForm: {
        adminID: "",
        passWord: "",
      },
      rules: {
        adminID: [
          {
            required: true,
            message: "用户账号必须输入",
            trigger: "blur",
          },
        ],
        passWord: [
          {
            required: true,
            message: "用户密码必须输入",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log(this.loginForm);
          login(this.loginForm).then((res) => {
            this.$store.commit("setToken", res.data.token);
            sessionStorage.setItem("token", res.data.token);
            initMenu(this.$router, this.$store);
            this.$router.push("/index");
          });
        } else return false;
      });
    },
    goRegister() {
      this.$router.push("/Register");
    },
  },
};
</script>

<style  scoped>
.login-container {
  /* background-image: url('../assets/bg.jpg'); */
  background-size: cover;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
}
.login-win {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  height: 300px;
  padding: 15px 25px;
  border-radius: 5px;
  background-color: #fff;
}
.login-body {
  width: 100%;
}
.login-title {
  text-align: center;
  font-size: 25px;
  font-weight: bold;
  color: #66cc99;
  margin-bottom: 45px;
  margin-top: 15px;
}

.el-link {
  /* text-decoration: none; */
  color: #aaa;
  font-size: 15px;
  float: right;
  padding-left: 0.5rem;
}
span:hover {
  color: coral;
}
</style>