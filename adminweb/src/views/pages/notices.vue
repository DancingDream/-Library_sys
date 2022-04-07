<template>
  <div>
    <el-header>
      <el-button class="headerButton" @click="addNotice()">添加通知</el-button>
    </el-header>
    <el-main>
      <el-table :data="noticeForm" height="780" border style="width: 100%">
        <el-table-column prop="amenTime" label="修改日期" width="180">
        </el-table-column>
        <el-table-column prop="title" label="标题" width="180">
        </el-table-column>
        <el-table-column prop="text" label="正文"> </el-table-column>
        <el-table-column prop="setEdit" label="编辑" width="180">
        </el-table-column>
        <el-table-column fixed="right" label="操作" width="180">
          <template slot-scope="scope">
            <el-button @click="seeInfo(scope.row)" type="text" size="small"
              >查看</el-button
            >
            <el-button type="text" @click="amenInfo(scope.row)" size="small"
              >编辑</el-button
            >
            <el-button @click="deleInfo(scope.row)" type="text" size="small"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-main>

    <el-dialog
      title="通知管理"
      width="1000px"
      :append-to-body="true"
      :visible.sync="amenNotice"
    >
      <el-form ref="amenNoticeFrom" :model="amenNoticeFrom" label-width="80px">
        <el-form-item label="标题">
          <el-input
            v-model="amenNoticeFrom.title"
            clearable
            placeholder="请输入标题"
          ></el-input>
        </el-form-item>
        <el-form-item label="公告">
          <el-input
            v-model="amenNoticeFrom.text"
            clearable
            type="textarea"
            autosize
            placeholder="请输入公告"
          ></el-input>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="addBookMenu" v-if="addNoticeState"
          >添加</el-button
        >
        <el-button type="primary" @click="amenBookMenu()" v-if="amenNoticeState"
          >修 改</el-button
        >
        <el-button @click="amenBookMenuClose()">取 消</el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="查看通知"
      width="1000px"
      :append-to-body="true"
      :visible.sync="showInfo"
    >
      <el-form ref="amenNoticeFrom" :model="amenNoticeFrom" label-width="80px">
        <el-form-item label="标题">
          <p>{{ amenNoticeFrom.title }}</p>
        </el-form-item>
        <el-form-item label="公告">
          <p>{{ amenNoticeFrom.text }}</p>
        </el-form-item>
        <el-form-item label="时间">
          <p>{{ amenNoticeFrom.amenTime }}</p>
        </el-form-item>
        <el-form-item label="管理员">
          <p>{{ amenNoticeFrom.setEdit }}</p>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
    
<script>
import { getNotice, addNotice, amenNotice } from "../../api/index";

export default {
  name: "",
  data() {
    return {
      noticeForm: [],
      amenNoticeFrom: {
        title: "",
        text: "",
        token: "",
      },
      amenNotice: false,
      showInfo: false,

      addNoticeState: false,
      amenNoticeState: false,
    };
  },

  methods: {
    //初始化添加修改数据
    initAddNotice() {
      this.amenNoticeFrom = {};
    },

    //初始公告数据
    initNotice() {
      getNotice().then((res) => {
        this.noticeForm = res.data;
      });
    },

    //添加界面
    addNotice() {
      this.initAddNotice();
      this.amenNotice = true;
      this.addNoticeState = true;
      this.amenNoticeState = false;
    },

    //修改界面
    amenInfo(index) {
      this.initAddNotice();
      this.amenNotice = true;
      this.amenNoticeState = true;
      this.addNoticeState = false;

      this.amenNoticeFrom = index;
      console.log(this.amenNoticeFrom);
    },

    //添加修改页面关闭
    amenBookMenuClose() {
      this.addNoticeState = false;
      this.amenNoticeState = false;
      this.amenNotice = false;
    },

    //发送添加信息
    addBookMenu() {
      this.amenNoticeFrom.token = this.$store.state.token;
      console.log(this.amenNoticeFrom);
      addNotice(this.amenNoticeFrom).then((res) => {
        this.$message({
          message: res.msg,
          type: "success",
        });
      });
      this.addNoticeState = false;
      this.amenNotice = false;
      this.initNotice();
      this.initAddNotice();
    },

    amenBookMenu() {
      this.amenNoticeFrom.token = this.$store.state.token;
      amenNotice(this.amenNoticeFrom).then((res) => {
        this.$message({
          message: res.msg,
          type: "success",
        });
      });
      this.showInfo = false;
      this.initAddNotice();
      this.initNotice();
    },

    //查看公告
    seeInfo(index) {
      this.showInfo = true;
      this.amenNoticeFrom = index;
    },

    //删除公告
    deleInfo(index) {},
  },

  mounted() {
    this.initNotice();
  },
};
</script>

<style scoped>
.headerButton {
  margin-left: 10px;
  float: right;
}

.el-header {
  padding-right: 20px;
  height: 40px;
  position: sticky;
  top: -1px;
  background-color: #e9eef3;
  z-index: 5;
  padding: 0%;
}

.el-main {
  padding: 0%;
}
</style>