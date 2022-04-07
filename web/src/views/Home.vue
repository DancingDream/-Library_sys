<template>
  <el-container>
    <el-header>
      <img
        class="logo"
        src="../assets/千库网_图书馆书架_元素编号12863483.png"
        alt=""
      />
      <h3 class="title">图书馆</h3>
    </el-header>

    <el-main>
      <el-row :gutter="20">
        <el-col :span="18">
          <div class="grid-content bg-purple">
            <!-- <el-carousel indicator-position="outside">
                  <el-carousel-item v-for="item in 4" :key="item">
                      <h3>{{ item }}</h3>
                  </el-carousel-item>
                </el-carousel> -->

            <p>公告信息</p>
          </div>
        </el-col>
        <el-col :span="6" class="homeButton">
          <div class="grid-content bg-purple">
            <ul>
              <li>
                <el-button type="primary" @click="showBoBook">借书</el-button>
              </li>
              <li>
                <el-button type="primary" @click="showReBook">还书</el-button>
              </li>
              <li><el-button type="primary">注册</el-button></li>
              <li>
                <el-button @click="goBookrack" type="primary">书架</el-button>
              </li>
              <!-- <li><el-button  type="primary" disabled>默认按钮</el-button></li> -->
            </ul>
          </div>
        </el-col>
      </el-row>

      <el-dialog
        width="1000px"
        title="借书/还书"
        :append-to-body="true"
        :visible.sync="showBoRe"
      >
        <el-form ref="boReFrom" :model="boReFrom">
          <el-form-item label="姓名" prop="name">
            <el-input v-model="boReFrom.name"></el-input>
          </el-form-item>

          <el-form-item label="手机号" prop="phone">
            <el-input v-model="boReFrom.phone"></el-input>
          </el-form-item>

          <el-form-item label="书本isbn" prop="isbn">
            <el-input v-model="boReFrom.isbn"></el-input>
          </el-form-item>
        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button type="primary" v-if="reBoState" @click="boBook('boReFrom')"
            >借书</el-button
          >
          <el-button type="primary" v-else @click="reBook('boReFrom')"
            >还书</el-button
          >
          <el-button>取 消</el-button>
        </div>
      </el-dialog>
    </el-main>
  </el-container>
</template>

<script>
import { boBookInfo, reBookInfo } from "../api/index";

export default {
  name: "Home",
  data() {
    return {
      showBoRe: false,
      boReFrom: {
        name: "",
        phone: "",
        isbn: "",
      },
      reBoState: true,
    };
  },
  components: {},
  methods: {
    goBookrack() {
      this.$router.push("./Bookrack");
    },

    //借书界面打开
    showBoBook() {
      this.boReFrom = {};
      this.showBoRe = true;
      this.reBoState = true;
    },

    //还书界面打开
    showReBook() {
      this.boReFrom = {};
      this.showBoRe = true;
      this.reBoState = false;
    },

    //借书操作
    boBook(name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          console.log(this.boReFrom);
          boBookInfo(this.boReFrom).then((res) => {
            this.$message({
              message: res.msg,
              type: "success",
            });
            if (res.code == 0) this.showBoRe = false;
          });
        }
      });
    },

    //还书操作
    reBook(name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          console.log(this.boReFrom);
          reBookInfo(this.boReFrom).then((res) => {
            this.$message({
              message: res.msg,
              type: "success",
            });
            if (res.code == 0) this.showBoRe = false;
          });
        }
      });
    },
  },
};
</script>

<style scoped>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: auto;
  height: auto;
}

.logo {
  width: 60px;
  position: relative;
  float: left;
}

.title {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  float: left;
  padding-left: 0.1rem;
  margin-top: 15px;
  font-size: 20px;
}

.el-main {
  background-color: #e9eef3;
  text-align: center;
  line-height: auto;
  height: 93.5vh;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.homeButton {
  display: flex;
  align-items: center;
  justify-content: center;
}

.homeButton li {
  padding-block-start: 0.1rem;
}

.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.el-button {
  width: 2rem;
}

li {
  padding-bottom: 10px;
}
</style>