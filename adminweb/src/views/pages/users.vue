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
      <el-table
        :data="userForm"
        height="780"
        style="width: 100%"
        :row-class-name="tableRowClassName"
      >
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
        <el-table-column prop="state" label="禁用状态" sortable>
        </el-table-column>
        <el-table-column label="禁用设置" sortable>
          <template slot-scope="scope">
            <el-button
              @click="upUserState(scope.row)"
              :disabled="scope.row.banState"
              type="text"
              size="small"
              >禁用</el-button
            >
            <el-button
              @click="upUserState(scope.row)"
              :disabled="!scope.row.banState"
              type="text"
              size="small"
              >解禁</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-main>
  </div>
</template>

<script>
import { getUsers, updateUserState } from "../../api/index";

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
        for (let i in res.data) {
          if (res.data[i].banState) {
            this.userForm[i].state = "已禁用";
          } else {
            this.userForm[i].state = "未禁用";
          }
        }
      });
    },

    tableRowClassName({ row, rowIndex }) {
      // console.log(row);
      if (!row.banState) {
        return "success-row";
      }
      return "";
    },

    upUserState(index) {
      console.log(index)
      updateUserState(index).then((res) => {
        this.$message({
          message: res.msg,
          type: "success",
        });
      });
      this.initUsers();
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

.el-link {
  margin-right: 10px;
}

.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>