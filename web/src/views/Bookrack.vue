<template>
  <el-container>
    <el-header>
      <img
        class="logo"
        src="../assets/千库网_图书馆书架_元素编号12863483.png"
        alt=""
      />
      <h3 class="title">图书馆</h3>
      <!-- <el-button plain class="headerButton">返回</el-button> -->
      <el-button plain class="headerButton" @click="goHome">首页</el-button>
    </el-header>

    <el-row class="header">
      <el-col :span="18">
        <div class="grid-content bg-purple">
          <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>书架</el-breadcrumb-item>
            <!-- <el-breadcrumb-item>详情</el-breadcrumb-item> -->
          </el-breadcrumb>
        </div>
      </el-col>

      <el-col :span="6">
        <div class="grid-content bg-purple">
          <el-input placeholder="请输入内容" v-model="fine" clearable>
          </el-input>
        </div>
      </el-col>
    </el-row>
    <div>
      <ul class="infinite-list" v-infinite-scroll="load" style="overflow: auto">
        <li
          class="infinite-list-item clear"
          v-for="(item, index) in activeinHouseList"
          :key="index"
          @click="seeInfo(index)"
        >
          <el-image
            style="width: 250px; height: 250px"
            :src="item.cover"
            :fit="fill"
          ></el-image>
          <div class="p">
            <p>书名：{{ item.bookName }}</p>
            <p>作者：{{ item.author }}</p>
            <p>ISBN：{{ item.ISBN }}</p>
            <p>中国分类法：{{ item.chinaClass }}</p>
            <p>页数：{{ item.page }}</p>
            <p>分类：{{ item.category }}</p>
            <p>出版时间：{{ item.pubDate }}</p>
            <p>出版社：{{ item.pubLisher }}</p>
            <p>语言：{{ item.language }}</p>
          </div>
          <div class="prospectus">
            <p>{{ item.prospectus }}</p>
          </div>
        </li>
      </ul>
    </div>

    <el-dialog
      width="1500px"
      :append-to-body="true"
      :visible.sync="showSeeInfoFlag"
    >
      <el-descriptions title="书本信息">
        <el-descriptions-item label="书名">{{
          this.cacheBookForm.bookName
        }}</el-descriptions-item>
        <el-descriptions-item label="副标题">{{
          this.cacheBookForm.subhead
        }}</el-descriptions-item>
        <el-descriptions-item label="原作名">{{
          this.cacheBookForm.originalName
        }}</el-descriptions-item>
        <el-descriptions-item label="作者">{{
          this.cacheBookForm.author
        }}</el-descriptions-item>
        <el-descriptions-item label="译者">{{
          this.cacheBookForm.translator
        }}</el-descriptions-item>
        <el-descriptions-item label="ISBN">{{
          this.cacheBookForm.ISBN
        }}</el-descriptions-item>
        <el-descriptions-item label="定价">{{
          this.cacheBookForm.price
        }}</el-descriptions-item>
        <el-descriptions-item label="中国分类法">{{
          this.cacheBookForm.chinaClass
        }}</el-descriptions-item>
        <el-descriptions-item label="页数">{{
          this.cacheBookForm.page
        }}</el-descriptions-item>
        <el-descriptions-item label="分类">{{
          this.cacheBookForm.category
        }}</el-descriptions-item>
        <el-descriptions-item label="出版时间">{{
          this.cacheBookForm.pubDate
        }}</el-descriptions-item>
        <el-descriptions-item label="出版社">{{
          this.cacheBookForm.pubLisher
        }}</el-descriptions-item>
        <el-descriptions-item label="出版地">{{
          this.cacheBookForm.pubLisherAdd
        }}</el-descriptions-item>
        <el-descriptions-item label="装帧">{{
          this.cacheBookForm.binding
        }}</el-descriptions-item>
        <el-descriptions-item label="语言">{{
          this.cacheBookForm.language
        }}</el-descriptions-item>
        <el-descriptions-item label="收录位置">{{
          this.cacheBookForm.location
        }}</el-descriptions-item>
        <el-descriptions-item label="总数">{{
          this.cacheBookForm.quantity
        }}</el-descriptions-item>
        <el-descriptions-item label="剩余数">{{
          this.cacheBookForm.surplus
        }}</el-descriptions-item>
        <el-descriptions-item label="封面">
          <el-image
            style="width: 350px; height: 350px"
            :src="this.cacheBookForm.cover"
            :fit="cover"
          >
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </el-descriptions-item>

        <el-descriptions-item label="内容简介" :span="2">{{
          this.cacheBookForm.prospectus
        }}</el-descriptions-item>

        <el-descriptions-item label="权重">{{
          this.cacheBookForm.weight
        }}</el-descriptions-item>
      </el-descriptions>
      <div slot="footer" class="dialog-footer">
        <el-button @click="seeInfoClose">返回</el-button>
      </div>
    </el-dialog>
  </el-container>
</template>

<script>
import { getBooks } from "../api/index";

export default {
  name: "Bookrack",
  data() {
    return {
      fine: "",
      booksForm: [],
      showSeeInfoFlag: false,
      cacheBookForm: {},
    };
  },

  methods: {
    goHome() {
      this.$router.push("./");
    },

    initBooksForm() {
      this.booksForm = [];
      this.activeinHouseList = [];
      getBooks().then((res) => {
        this.booksForm = res.data;
        console.log(this.booksForm);
      });
      this.dataList = this.booksForm;
      this.reloadPart();
    },
    seeInfo(index) {
      this.showSeeInfoFlag = true;
      this.cacheBookForm = this.activeinHouseList[index];
    },

    //关闭详细页
    seeInfoClose() {
      this.showSeeInfoFlag = false;
      this.initNewBook();
    },
  },
  //打开详细页

  computed: {
    activeinHouseList: function () {
      return this.booksForm.filter((item) => {
        return item.state == true;
      });
    },
  },

  mounted() {
    this.initBooksForm();
  },
};
</script>

<style  scoped>
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

.headerButton {
  float: right;
  margin-top: 10px;
  margin-left: 0.1rem;
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
  display: flex;
  align-items: center;
}

.el-breadcrumb-item {
  font-size: 5px;
}

.header {
  padding: 0.1rem 0.2rem;
}

ul {
  float: left;
  /* display: inline-block; */
  width: 100%;
}
ul li {
  /* float: left; */
  display: inline-block;
  width: 100%;
  height: 100%;

  margin-bottom: 14px;
  background-color: #ffffff;
  list-style: none;
}
.el-image {
  float: left;
  padding: 10px 20px;
  z-index: 0;
}
.p {
  float: left;
  padding-top: 20px;
  padding-right: 10px;
  text-align: center;
}
.p p {
  padding-bottom: 5px;
  text-align: left;
  width: 400px;
}

.prospectus {
  float: left;
  width: 1100px;
  height: 150px;
  margin-top: 15px;
  margin-bottom: 15px;
  text-align: left;
}
</style>