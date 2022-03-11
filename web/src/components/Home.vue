<template>
    <el-container>
        <el-header>
            <img class="logo" src="../assets/千库网_图书馆书架_元素编号12863483.png" alt="">
            <h3 class="title" >图书馆</h3>
        </el-header>

        <el-main>
            <el-row :gutter="20">
                <el-col :span="18">
                    <div class="grid-content bg-purple">
                        <el-carousel indicator-position="outside">
                            <el-carousel-item v-for="item in 4" :key="item">
                                <h3>{{ item }}</h3>
                            </el-carousel-item>
                        </el-carousel>
                    </div>
                </el-col>
                <el-col :span="6" class="homeButton">
                    <div class="grid-content bg-purple">
                        <ul>
                            <li><el-button  type="primary" disabled>借书/还书</el-button></li>
                            <li><el-button  type="primary" disabled>注册</el-button></li>
                            <li><el-button  type="primary" disabled @click="goBookrack()">书架</el-button></li>
                            <!-- <li><el-button  type="primary" disabled>默认按钮</el-button></li> -->
                        </ul>
                    </div>
                </el-col>
            </el-row>
        </el-main>
    </el-container>

    
</template>

<script>
    export default {
        name: 'Home',
        data() {
            return {
                
            }
        },
        methods:{
            goBookrack(){
                this.$router.push('./Bookrack')
            }
        }
    }
</script>

<style scoped>
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

.el-main {
  background-color: #e9eef3;
  text-align: center;
  line-height: auto;
  height: auto;
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

.homeButton{
  display: flex;
  align-items: center;
  justify-content: center;
}

.homeButton li{
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

.el-button{
  width: 2rem;
}
</style>