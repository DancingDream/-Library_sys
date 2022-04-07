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
      <el-button @click="addBookMenu">添加书本</el-button>
    </el-header>
    <el-main v-if="isReloadData" class="clear">
      <ul class="infinite-list" v-infinite-scroll="load" style="overflow: auto">
        <li
          class="infinite-list-item clear"
          v-for="(item, index) in activeinHouseList"
          :key="index"
        >
          <el-image
            @click="seeInfo(index)"
            style="width: 250px; height: 250px"
            :src="item.cover"
            :fit="fill"
          ></el-image>
          <div class="p" @click="seeInfo(index)">
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
          <div class="prospectus" @click="seeInfo(index)">
            <p>{{ item.prospectus }}</p>
          </div>

          <div class="amenButton">
            <el-button
              type="danger"
              icon="el-icon-delete"
              circle
              @click="remove(index)"
            ></el-button>
            <el-button
              type="primary"
              icon="el-icon-edit"
              circle
              @click="amenBookMenuIndex(index)"
            ></el-button>
          </div>
        </li>
      </ul>
    </el-main>

    <el-dialog
      title="添加修改"
      width="1500px"
      :append-to-body="true"
      :visible.sync="showAddInfoFlag"
    >
      <el-form label-width="80px" :model="cacheBookForm">
        <el-form-item label="ISBN">
          <el-input
            name="isbn"
            v-model="cacheBookForm.ISBN"
            placeholder="请输入ISBN"
            autocomplete="off"
            @blur="postNewISBN()"
          ></el-input>
        </el-form-item>
        <el-form-item label="书名">
          <el-input
            v-model="cacheBookForm.bookName"
            placeholder="请输入书名"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="副标题">
          <el-input
            v-model="cacheBookForm.subhead"
            placeholder="请输入副标题"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="原作名">
          <el-input
            v-model="cacheBookForm.originalName"
            placeholder="请输入原作名"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="作者">
          <el-input
            v-model="cacheBookForm.author"
            placeholder="请输入作者"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="译者">
          <el-input
            v-model="cacheBookForm.translator"
            placeholder="请输入译者"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="封面">
          <el-image
            style="width: 100px; height: 100px"
            :src="this.cacheBookForm.cover"
            :fit="cover"
          >
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </el-form-item>
        <el-form-item label="定价">
          <el-input
            v-model="cacheBookForm.price"
            placeholder="请输入定价"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="中国分类法">
          <el-input
            v-model="cacheBookForm.chinaClass"
            placeholder="请输入中国分类法"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="页数">
          <el-input
            v-model="cacheBookForm.page"
            placeholder="请输入页数"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="分类">
          <el-input
            v-model="cacheBookForm.category"
            placeholder="请输入分类"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="出版时间">
          <el-input
            v-model="cacheBookForm.pubDate"
            placeholder="请输入出版时间"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="出版社">
          <el-input
            v-model="cacheBookForm.pubLisher"
            placeholder="请输入出版社"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="出版地">
          <el-input
            v-model="cacheBookForm.pubLisherAdd"
            placeholder="请输入出版地"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="装帧">
          <el-input
            v-model="cacheBookForm.binding"
            placeholder="请输入装帧"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="语言">
          <el-input
            v-model="cacheBookForm.language"
            placeholder="请输入语言"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="内容简介">
          <el-input
            v-model="cacheBookForm.prospectus"
            placeholder="请输入内容简介"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="收录位置">
          <el-input
            v-model="cacheBookForm.location"
            placeholder="请输入收录位置"
            autocomplete="off"
            :disabled="!this.cacheBookForm.state"
          ></el-input>
        </el-form-item>
        <el-form-item label="总数">
          <el-input
            v-model="cacheBookForm.quantity"
            placeholder="请输入总数"
            autocomplete="off"
            :disabled="!this.cacheBookForm.state"
          ></el-input>
        </el-form-item>

        <el-form-item label="权重">
          <el-input
            v-model="cacheBookForm.weight"
            placeholder="请输入权重"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-radio-group v-model="cacheBookForm.state">
          <el-radio :label="true">已添加</el-radio>
          <el-radio :label="false">未添加</el-radio>
        </el-radio-group>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addBookMenuClose">取 消</el-button>
        <el-button type="primary" @click="addNewBookInfo">确 定</el-button>
      </div>
    </el-dialog>

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
        <el-descriptions-item label="是否添加书本">
          <p v-if="this.cacheBookForm.state">已添加</p>
          <p v-else>未添加</p>
        </el-descriptions-item>
      </el-descriptions>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="amenBookMenu()">修 改</el-button>
        <el-button @click="seeInfoClose">取 消</el-button>
      </div>
    </el-dialog>

    <el-backtop
      target=".page-component__scroll .el-scrollbar__wrap"
    ></el-backtop>
  </div>
</template>

<script>
import { getBooks, fineNewBook, addBook } from "../../api/index";

export default {
  name: "",
  data() {
    return {
      //后端传入书本单
      booksForm: [],
      //添加表单
      cacheBookForm: {
        bookName: "",
        subhead: "",
        originalName: "",
        author: "",
        translator: "",
        ISBN: "",
        cover: "",
        price: "",
        chinaClass: "",
        page: "",
        category: "",
        pubDate: "",
        pubLisher: "",
        pubLisherAdd: "",
        binding: "",
        language: "",
        prospectus: "",
        location: "",
        quantity: "",
        surplus: "",
        weight: "",
        state: "",
      },

      fineISBNForm: {
        isbn: "",
      },

      showAddInfoFlag: false,
      showSeeInfoFlag: false,

      dataList: "",
      dialogImageUrl: "",

      diseaseList: [], //这个值是需要匹配的值
      disease: "", //这个值是用户正在输入的值
      // activeinHouseList: [],

      isReloadData: true,
    };
  },

  methods: {
    reloadPart() {
      this.isReloadData = false;
      this.$nextTick(() => {
        this.isReloadData = true;
      });
    },

    //初始化界面书本信息
    initBooksForm() {
      console.log(123);
      this.booksForm = [];
      this.activeinHouseList = [];
      getBooks().then((res) => {
        this.booksForm = res.data;
        console.log(this.booksForm);
      });
      this.dataList = this.booksForm;
      this.reloadPart();
    },

    //初始化添加界面书本信息
    initNewBook() {
      this.cacheBookForm = {};
      this.initBooksForm();
    },

    //打开添加界面
    addBookMenu() {
      this.showAddInfoFlag = true;
      this.initNewBook();
    },

    //关闭添加界面
    addBookMenuClose() {
      this.showAddInfoFlag = false;
    },

    //列表打开修改界面
    amenBookMenuIndex(index) {
      this.cacheBookForm = this.activeinHouseList[index];
      this.showAddInfoFlag = true;
    },

    //详细页打开修改界面
    amenBookMenu() {
      this.showAddInfoFlag = true;
    },

    //打开详细页
    seeInfo(index) {
      this.showSeeInfoFlag = true;
      this.cacheBookForm = this.activeinHouseList[index];
    },

    //关闭详细页
    seeInfoClose() {
      this.showSeeInfoFlag = false;
      this.initNewBook();
    },

    remove(index) {
      this.activeinHouseList[index].state = false;
      this.addNewBookInfo();
    },

    //后台请求新isbn查找
    postNewISBN() {
      if (!this.cacheBookForm.ISBN == "") {
        fineNewBook(this.cacheBookForm.ISBN).then((res) => {
          let page;
          // console.log(this.newBooksForm);
          if (res.data[0].page == null) page = 0;
          else page = res.data[0].page;
          this.cacheBookForm = res.data[0];
          this.cacheBookForm.page = page;
          console.log(this.cacheBookForm.cover);
          this.dialogImageUrl = this.cacheBookForm.cover;
          console.log(this.dialogImageUrl);
        });
      }
    },

    //添加新书确认
    addNewBookInfo() {
      console.log(this.cacheBookForm);
      if (this.cacheBookForm.state == false) {
        this.cacheBookForm.quantity = 0;
        this.cacheBookForm.surplus = 0;
        this.cacheBookForm.weight = 0;
        this.cacheBookForm.location = "";
      } else {
        this.cacheBookForm.surplus = this.cacheBookForm.quantity;
      }

      addBook(this.cacheBookForm).then((res) => {
        this.$message({
          message: res.msg,
          type: "success",
        });
      });
      this.showAddInfoFlag = false;

      this.initBooksForm();
      this.dialogImageUrl = "";
      console.log(this.booksForm);
    },

    querySearch(queryString, cb) {
      const diseaseList = this.diseaseList;
      const results = queryString
        ? diseaseList.filter(this.createFilter(queryString))
        : diseaseList;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter(queryString) {
      return (disease) => {
        return (
          disease.value.toLowerCase().indexOf(queryString.toLowerCase()) !== -1
        ); // 改为===0 就是筛选的数据只是首字匹配的列表项，需要包含输入字的所有列表项改为！==-1)
      };
    },
    handleSelect(item) {
      console.log(item);
    },
  },

  watch: {},

  computed: {
    activeinHouseList: function () {
      return this.booksForm.filter((item) => {
        return item.state == true;
      });
    },
  },

  mounted() {
    this.initBooksForm();
    console.log(this.booksForm);
  },
};
</script>

<style scoped>
.el-main {
  padding: 0%;
}
/* button{
    
    float: right;
} */

.bookHeader {
  width: 15rem;
  float: right;
  height: 40px;
  padding-left: 0.5rem;
}

.el-divider {
  border-top: 5px;
}

/* .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  } */

.el-header {
  padding-right: 20px;
  height: 40px;
  position: sticky;
  top: -1px;
  background-color: #e9eef3;
  z-index: 5;
  padding: 0%;
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

.amenButton .el-button {
  margin: 10px;
}
.el-button {
  margin-left: 10px;
  float: right;
}
.prospectus {
  float: left;
  width: 750px;
  height: 150px;
  margin-top: 15px;
  margin-bottom: 15px;
  text-align: left;
}
</style>