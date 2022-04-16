<template>
  <div class="login-container">
    <div class="login-win">
      <div class="login-body">
        <h1 class="login-title">账号注册</h1>
        <div class="login-form">
          <el-form :model="registerForm" :rules="rules" ref="registerForm">
            <!-- 注册账号 -->
            <el-form-item prop="adminID">
              <el-input
                type="text"
                v-model="registerForm.adminID"
                suffix-icon="el-icon-user-solid"
                placeholder="请输入您的账号"
              ></el-input>
            </el-form-item>
            <!-- 一次密码 -->
            <el-form-item prop="passWord">
              <el-input
                type="passWord"
                v-model="registerForm.passWord"
                suffix-icon="el-icon-lock"
                placeholder="请输入您的密码"
              ></el-input>
            </el-form-item>
            <!-- 二次密码 -->
            <el-form-item prop="repassWord">
              <el-input
                type="passWord"
                v-model="registerForm.repassWord"
                suffix-icon="el-icon-lock"
                placeholder="请再次输入您的密码"
              ></el-input>
            </el-form-item>
            <el-form-item prop="name">
              <el-input
                type="text"
                v-model="registerForm.name"
                suffix-icon="el-icon-suitcase"
                placeholder="请输入您的姓名"
              ></el-input>
            </el-form-item>
            <el-form-item prop="jobNum">
              <el-input
                type="text"
                v-model="registerForm.jobNum"
                suffix-icon="el-icon-suitcase"
                placeholder="请输入您的工号"
              ></el-input>
            </el-form-item>
            <el-form-item prop="phone">
              <el-input
                type="text"
                v-model="registerForm.phone"
                suffix-icon="el-icon-phone"
                placeholder="请输入您的手机号"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-row :gutter="20">
                <el-col :span="12">
                  <el-button @click="submitForm('registerForm')" type="primary"
                    >管理员注册</el-button
                  >
                </el-col>
                <el-col :span="12">
                  <el-button @click="goLogin" type="primary">返回</el-button>
                </el-col>
              </el-row>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { register } from "../api/index.js";
import { MD5 } from "../js/MD5";

export default {
  data() {
    //一次密码检验合法性
    const pwdCheck = async (rule, value, callback) => {
      let reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,16}$/;
      if (value.length < 6) {
        this.changeFlag = 2;
        return callback(new Error("密码不能少于6位！"));
      } else if (value.length > 16) {
        this.changeFlag = 2;
        return callback(new Error("密码最长不能超过16位！"));
      } else if (!reg.test(value)) {
        this.changeFlag = 2;
        return callback(
          new Error("6-16位字符，同时包括数字和大小写字母三种组合")
        );
      } else {
        this.changeFlag = 1;
        callback();
      }
    };

    //二次密码检验正确性
    const pwdAgainCheck = async (rule, value, callback) => {
      if (value.length < 1) {
        this.changeAgainFlag = 2;
        return callback(new Error("密码不能为空！"));
      } else if (this.registerForm.passWord !== this.registerForm.repassWord) {
        this.changeAgainFlag = 2;
        return callback(new Error("密码不一致！"));
      } else {
        this.changeAgainFlag = 1;
        callback();
      }
    };

    //电话检验
    const phoneCheck = async (rule, value, callback) => {
      let telText = /^1\d{10}$/;
      if (!telText.test(value)) {
        return callback(new Error("请正确输入手机号码"));
      } else {
        callback();
      }
    };

    return {
      changeFlag: 0,
      changeAgainFlag: 0,

      registerForm: {
        adminID: "",
        passWord: "",
        repassWord: "",
        name: "",
        jobNum: "",
        phone: "",
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
            // message: '用户密码必须输入',
            validator: pwdCheck,
            trigger: "blur",
          },
        ],
        repassWord: [
          {
            required: true,
            // message: '用户密码必须输入',
            validator: pwdAgainCheck,
            trigger: "blur",
          },
        ],
        name: [
          {
            required: true,
            message: "用户姓名必须输入",
            trigger: "blur",
          },
        ],
        jobNum: [
          {
            required: true,
            message: "用户工号必须输入",
            trigger: "blur",
          },
        ],
        phone: [
          {
            required: true,
            // message: '用户手机号必须输入',
            validator: phoneCheck,
            trigger: "blur",
          },
        ],
      },
    };
  },

  methods: {
    goLogin() {
      this.$router.push("/");
    },

    //判定是否post是否成功，成功跳转到登陆页
    submitForm(name) {
      console.log(this.registerForm);
      let str;
      this.$refs[name].validate((valid) => {
        if (valid) {
          
          this.registerForm.MD5passWord = MD5(this.registerForm.passWord);
          this.registerForm.passWord = '';
          this.registerForm.repassWord = '';
          register(this.registerForm).then((res) => {
            this.$message({
              message: res.msg,
              type: "success",
            });

            if (res.code == 0) {
              this.$router.push("/");
            } 
          });
        } else {
          this.$message.error("请正确填写信息");
        }
      });
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

a {
  text-decoration: none;
  color: #aaa;
  font-size: 15px;
  float: right;
  padding-left: 0.5rem;
}
a:hover {
  color: coral;
}

.el-button {
  width: 100%;
  margin-top: 10px;
  background-color: #66cc99;
}

.el-form-item {
  margin-bottom: 30px;
}
</style>