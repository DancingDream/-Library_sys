<template>
  <div class="clear">
    <img
      class="logo"
      src="../assets/千库网_图书馆书架_元素编号12863483.png"
      alt=""
    />
    <h1 class="title">图书管理系统</h1>
    <!-- <span>{{ msg }}</span> -->
    <!-- <span class="name"></span> -->
    <el-dropdown @command="handleUser" class="fater-header-user">
      <span class="el-dropdown-link">{{ adminForm.name }} | 个人中心</span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="info"> 信息修改</el-dropdown-item>
        <el-dropdown-item command="pwd"> 修改密码</el-dropdown-item>
        <el-dropdown-item command="exit"> 退出系统</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>

    <el-dialog
      title="修改信息"
      width="600px"
      :append-to-body="true"
      :visible.sync="showUpdInfoFlag"
    >
      <el-form
        label-width="100px"
        :model="adminForm"
        :rules="rules"
        ref="adminForm"
      >
        <el-form-item label="管理员账号:">
          <el-input
            v-model="adminForm.adminID"
            placeholder="请输入用户姓名…"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="姓名:">
          <p>{{ adminForm.name }}</p>
        </el-form-item>
        <el-form-item label="工号:">
          <p>{{ adminForm.jobNum }}</p>
        </el-form-item>
        <el-form-item label="联系电话:" prop="phone">
          <el-input
            v-model="adminForm.phone"
            placeholder="请输入联系电话…"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="创建时间:">
          <p>{{ adminForm.addTime }}</p>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="showUpdInfoFlag = false">取 消</el-button>
        <el-button type="primary" @click="updInfo()">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="修改密码"
      width="600px"
      :append-to-body="true"
      :visible.sync="showUpdPwdFlag"
    >
      <el-form label-width="80px" ref="userPwd" :model="userPwd" :rules="rules">
        <el-form-item label="原始密码" prop="oldPwd">
          <el-input
            type="password"
            v-model="userPwd.oldPwd"
            placeholder="请输入原始密码……"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="修改密码" prop="newPwd">
          <el-input
            type="password"
            v-model="userPwd.newPwd"
            placeholder="请输入修改密码……"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="rePwd">
          <el-input
            type="password"
            v-model="userPwd.rePwd"
            placeholder="请再次确认密码……"
            autocomplete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="showUpdPwdFlag = false">取 消</el-button>
        <el-button type="primary" @click="updPwd('userPwd')">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {
  exit,
  getLoginUser,
  updLoginUserInfo,
  updLoginUserPwd,
} from "../api/index";
import {MD5} from "../js/MD5"

export default {
  name: "",
  data() {
    var checkOldPwd = async (rule, value, callback) => {
      if (value) {
        if (MD5(value) === this.adminForm.passWord) {
          callback();
        } else {
          callback(new Error("密码错误！"));
        }
      } else {
        callback(new Error("原始密码必须输入"));
      }
      callback();
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
      } else if (this.userPwd.newPwd !== this.userPwd.rePwd) {
        this.changeAgainFlag = 2;
        return callback(new Error("密码不一致！"));
      } else {
        this.changeAgainFlag = 1;
        callback();
      }
    };

    return {
      rules: {
        phone: [
          {
            required: true,
            // message: '用户手机号必须输入',
            validator: phoneCheck,
            trigger: "blur",
          },
        ],
        newPwd: [
          {
            required: true,
            // message: '用户密码必须输入',
            validator: pwdCheck,
            trigger: "blur",
          },
        ],
        rePwd: [
          {
            required: true,
            // message: '用户密码必须输入',
            validator: pwdAgainCheck,
            trigger: "blur",
          },
        ],
        oldPwd: [
          {
            required: true,
            validator: checkOldPwd,
            trigger: "blur",
          },
        ],
      },

      adminForm: {
        adminID: "",
        passWord: "",
        name: "",
        jobNum: "",
        phone: "",
        addTime: "",
      },

      userPwd: {
        oldPwd: "",
        newPwd: "",
        rePwd: "",
      },

      showUpdInfoFlag: false,
      showUpdPwdFlag: false,
    };
  },

  components: {},

  methods: {
    //初始化用户数据
    initUserForm() {
      this.adminForm = {
        id: "",
        adminID: "",
        passWord: "",
        name: "",
        jobNum: "",
        phone: "",
        addTime: "",
        token: this.$store.state.token,
      };
      getLoginUser(this.$store.state.token).then((resp) => {
        this.adminForm = resp.data;
      });
    },

    initUserPwd() {
      this.userPwd = {
        oldPwd: "",
        newPwd: "",
        rePwd: "",
      };
    },

    //显示修改信息
    showUpdInfoWin() {
      this.showUpdInfoFlag = true;
    },

    showUpdPwdWin() {
      this.showUpdPwdFlag = true;
      this.initUserPwd();
    },

    //头部个人页
    handleUser(comm) {
      if (comm == "info") {
        this.showUpdInfoWin();
      } else if (comm == "pwd") {
        this.showUpdPwdWin();
      } else if (comm == "exit") {
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
    },

    //更新信息
    updInfo() {
      this.adminForm.token = this.$store.state.token;
      updLoginUserInfo(this.adminForm).then((resp) => {
        this.$message({
          message: resp.msg,
          type: "success",
        });

        this.showUpdInfoFlag = false;
      });
    },

    updPwd(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          updLoginUserPwd(this.$store.state.token, MD5(this.userPwd.newPwd)).then(
            (resp) => {
              this.$message({
                message: resp.msg,
                type: "success",
              });

              this.showUpdPwdFlag = false;
              this.initUserPwd();
            }
          );
        } else {
          return false;
        }
      });
    },
  },

  mounted() {
    this.initUserForm();
  },
};
</script>

<style scoped>
.logo {
  width: 60px;
  position: relative;
  float: left;
}

.title {
  float: left;
  font-size: 20px;
  color: #fff;
}

.fater-header-user {
  position: absolute;
  right: 35px;
  float: right;
  color: #fff;
}

.el-form-item p {
  float: left;
}

.name {
  float: right;
  color: #fff;
}
</style>