<template>    
  <el-container>
    <el-header>
      <img class="logo" src="../assets/千库网_图书馆书架_元素编号12863483.png" alt="">
      <h3 class="title" >图书馆</h3>
      <el-button plain class="headerButton">返回</el-button>
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
            <el-input
              placeholder="请输入内容"
              v-model="fine"
              clearable>
            </el-input>
          </div>
        </el-col>
    </el-row>
    <div >
      <ul v-for="(item, index) in books" :key="index">
        <li>{{item.bookName}}</li>
        <li>{{item.subhead}}</li>
        <li>{{item.originalName}}</li>
        <li>{{item.author}}</li>
        <li>{{item.translator}}</li>
        <li>{{item.press}}</li>
        <li>{{item.publicationYear}}</li>
        <li>{{item.ISBN}}</li>
        <li>{{item.pagination}}</li>
        <li><img src=item.cover><p>{{console.log(item.cover)}}</p></li>
        <li>{{item.quantity}}</li>
        <li>{{item.surplus}}</li>
        <li>{{item.location}}</li>
      </ul>
    </div>
  </el-container>
</template>

<script>

  import {getBooks} from '../api/index'

  export default {
    name: 'Bookrack',
      data() {
        return {
          fine:'',
          books:[],
        }
      },

      methods:{
        goHome(){
          this.$router.push('./');
        }   
      },

      mounted(){
        getBooks().then(res =>{
          console.log(res);
          this.books = res.data;
          console.log(this.books);
        });
      }
    }
</script>

<style  scoped>

  .el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: auto;
    height: auto;
  }

  .logo{
    width: 60px;
    position: relative;
    float: left;  
  }

  .title{
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    float: left;
    padding-left: 0.1rem;
    margin-top: 15px;
    font-size: 20px;
  }

  .headerButton{
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

  .el-breadcrumb-item{
    font-size: 5px;
  }

  .header{
    padding: 0.1rem 0.2rem;
  }

</style>