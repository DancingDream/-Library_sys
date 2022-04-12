<template>
  <div>
    <el-header>
      <el-autocomplete
        class="inline-input bookHeader"
        v-model="disease"
        :fetch-suggestions="querySearch"
        placeholder="请输入内容"
        :trigger-on-focus="true"
        @select="handleSelect"
        @keyup.enter.native="search"
      ></el-autocomplete>
    </el-header>

    <el-main>
      <el-table :data="recordInfos" height="780" style="width: 100%">
        <el-table-column prop="borrowDate" label="借书日期" sortable>
        </el-table-column>
        <el-table-column prop="borrowerBook" label="书籍名" sortable>
        </el-table-column>
        <el-table-column prop="borrowerID" label="借书人" sortable>
        </el-table-column>
        <el-table-column prop="state" label="借书状态" sortable>
        </el-table-column>

        <el-table-column prop="returnDate" label="还书时间" sortable>
        </el-table-column>

        <el-table-column prop="postpone" label="延期时长" sortable>
        </el-table-column>
      </el-table>
    </el-main>
  </div>
</template>

<script>
import { getRecord } from "../../api/index";

export default {
  name: "",
  data() {
    return {
      recordInfos: [],
      // reData:''
    };
  },

  methods: {
    initRecord() {
      getRecord().then((res) => {
        this.recordInfos = res.data;

        for (let i in this.recordInfos) {
          if (res.data[i].state) {
            this.recordInfos[i].state = "在借中";
          } else {
            this.recordInfos[i].state = "已归还";
          }

          if (res.data[i].postpone) {
            this.recordInfos[i].postpone = "已延期";
          } else {
            this.recordInfos[i].postpone = "未延期";
          }
        }
        console.log(this.recordInfos);
      });
    },
  },

  mounted() {
    this.initRecord();
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