<template>
    <el-row class="header">
        <el-col :span="18">
            <div class="grid-content bg-purple">
                <el-breadcrumb separator-class="el-icon-arrow-right">
                    <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
                    <el-breadcrumb-item>活动管理</el-breadcrumb-item>
                    <el-breadcrumb-item>活动列表</el-breadcrumb-item>
                    <el-breadcrumb-item>活动详情</el-breadcrumb-item>
                </el-breadcrumb>
            </div>
        </el-col>

        <el-col :span="6">
          <div class="grid-content bg-purple">
            <el-input
              placeholder="请输入内容"
              v-model="fine"
              clearable>
            </el-input>
          </div>
        </el-col>

        
    </el-row>


</template>

<script>
    export default {
        name: 'Bookrack',
        data() {
            return {
                fine:''
            }
        }
    }
</script>

<style  scoped>
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

  .el-breadcrumb-item{
    font-size: 5px;
  }

  .header{
    padding: 0.1rem 0.2rem;
  }

</style>