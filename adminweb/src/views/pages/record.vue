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
        <el-table-column prop="reState" label="借书状态" sortable>
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

    import {getRecord} from '../../api/index'

    export default {
        name: '',
        data() {
            return {
                recordInfos:[],
                // reData:''
            }
        },

        methods:{
          initRecord(){
            let nowDate = new Date;
            let reDate = 0;
            let postponeDate = 0;

            getRecord().then(res =>{
              this.recordInfos = res.data;
              
              for(let i in this.recordInfos){
                if(this.recordInfos[i].state){
                  this.recordInfos[i].reState = '在借中'
                }else{
                  this.recordInfos[i].reState = '已归还'
                }

                if(this.recordInfos[i].returnDate === 'None'){
                  this.recordInfos[i].returnDate = '';
                  reDate = nowDate;
                }else{
                  reDate = this.strToDate(this.recordInfos[i].returnDate)
                }

                postponeDate = this.strToDate(this.recordInfos[i].borrowDate) - reDate
                console.log(postponeDate);
                if(postponeDate <= this.recordInfos[i].deadline){
                  this.recordInfos[i].postpone = '未延期'
                }else{
                  this.recordInfos[i].postpone = '已延期'
                }

              }
              console.log(this.recordInfos);
            })
          },


          strToDate(dateStr){
	          var dateStr = dateStr.replace(/-/g, "/");//现将yyyy-MM-dd类型转换为yyyy/MM/dd
	          var dateTime = Date.parse(dateStr);//将日期字符串转换为表示日期的秒数
	          //注意：Date.parse(dateStr)默认情况下只能转换：月/日/年 格式的字符串，但是经测试年/月/日格式的字符串也能被解析
	          var data = new Date(dateTime);//将日期秒数转换为日期格式
          	return data;
          }
        },

        mounted(){
            this.initRecord();
        }
    }
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