<template>
  <div>
    <el-header>
      <el-autocomplete
        class="inline-input"
        v-model="disease"
        :fetch-suggestions="querySearch"
        placeholder="请输入内容"
        :trigger-on-focus="true"
        @select="handleSelect"
        @keyup.enter.native="search"
      ></el-autocomplete>
    </el-header>

    <el-main>
      <el-table :data="userForm" height="780" style="width: 100%">
        <el-table-column prop="userID" label="用户账号" sortable>
        </el-table-column>
        <el-table-column prop="nickName" label="用户昵称" sortable>
        </el-table-column>
        <el-table-column prop="userName" label="用户姓名" sortable>
        </el-table-column>
        <!-- <el-table-column
                prop="gender"
                label="用户性别"
                sortable>
                </el-table-column> -->
        <!-- <el-table-column
                prop="age"
                label="用户年龄"
                sortable>
                </el-table-column> -->
        <el-table-column prop="phone" label="联系电话" sortable>
        </el-table-column>
        <!-- <el-table-column
                prop="address"
                label="联系地址"
                sortable>
                </el-table-column> -->
        <el-table-column prop="email" label="电子邮箱" sortable>
        </el-table-column>
        <el-table-column prop="regDate" label="注册时间" sortable>
        </el-table-column>
        <!-- <el-table-column
                prop="weChat"
                label="微信号"
                sortable>
                </el-table-column> -->
        <!-- <el-table-column
                prop="credit"
                label="信誉分"
                sortable>
                </el-table-column> -->
        <el-table-column prop="borrowingBook" label="已借书本" sortable>
        </el-table-column>
      </el-table>
    </el-main>
  </div>
</template>

<script>
import { getUsers } from "../../api/index";

export default {
  name: "",
  data() {
    return {
      userForm: [],
    };
  },

  methods: {
    initUsers() {
      getUsers().then((res) => {
        this.userForm = res.data;
      });
    },
  },

  mounted() {
    this.initUsers();
  },
};
</script>

<style scoped>
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

.inline-input {
  float: right;
}
</style>