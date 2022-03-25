<template>
    <div>
        <el-input class="bookHeader" placeholder="请输入内容" v-model="book"  clearable ></el-input>
        <el-button @click="showAddInfoFlag = true;">添加书本</el-button>
        <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">
            <li v-for="(item,index) in booksForm" class="infinite-list-item" :key="index">{{ item }}</li>
        </ul>
        
        <el-dialog
        title="添加书本" width="1500px"
        :append-to-body="true" :visible.sync="showAddInfoFlag">
            <el-form label-width="80px" :model="newBooksForm">
                <el-form-item label="ISBN">
                    <el-input name="isbn" v-model="newBooksForm.ISBN " 
                        placeholder="请输入ISBN" autocomplete="off"
                        @blur="postNewISBN()"></el-input>
                </el-form-item>
                <el-form-item label="书名">
                    <el-input v-model="newBooksForm.bookName" 
                        placeholder="请输入书名" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="副标题">
                    <el-input v-model="newBooksForm.subhead" 
                        placeholder="请输入副标题" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="原作名">
                    <el-input v-model="newBooksForm.originalName" 
                        placeholder="请输入原作名" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="作者">
                    <el-input v-model="newBooksForm.author" 
                        placeholder="请输入作者" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="译者">
                    <el-input v-model="newBooksForm.translator" 
                        placeholder="请输入译者" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="封面">
                    <el-upload
                    action="''"
                    list-type="picture-card"
                    :auto-upload="false"
                    :on-change="change"
                    limit=1 v-if="this.newBooksForm.cover != Null ">
                    <img width="100%" v-if="dialogImageUrl" :src="dialogImageUrl" alt="">
                    <i v-else class="el-icon-plus" ></i>
                    </el-upload>
                </el-form-item>
                <el-form-item label="定价">
                    <el-input v-model="newBooksForm.price" 
                        placeholder="请输入定价" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="中国分类法">
                    <el-input v-model="newBooksForm.chinaClass" 
                        placeholder="请输入中国分类法" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="页数">
                    <el-input v-model="newBooksForm.page" 
                        placeholder="请输入页数" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="分类">
                    <el-input v-model="newBooksForm.category" 
                        placeholder="请输入分类" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="出版时间">
                    <el-input v-model="newBooksForm.pubDate" 
                        placeholder="请输入出版时间" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="出版社">
                    <el-input v-model="newBooksForm.pubLisher" 
                        placeholder="请输入出版社" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="出版地">
                    <el-input v-model="newBooksForm.pubLisherAdd" 
                        placeholder="请输入出版地" autocomplete="off"></el-input>
                </el-form-item> -->
                <el-form-item label="装帧">
                    <el-input v-model="newBooksForm.binding" 
                        placeholder="请输入装帧" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="语言">
                    <el-input v-model="newBooksForm.language" 
                        placeholder="请输入语言" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="内容简介">
                    <el-input v-model="newBooksForm.prospectus" 
                        placeholder="请输入内容简介" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="收录位置">
                    <el-input v-model="newBooksForm.location" 
                        placeholder="请输入收录位置" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="总数">
                    <el-input v-model="newBooksForm.quantity" 
                        placeholder="请输入总数" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="剩余数">
                    <el-input v-model="newBooksForm.surplus" 
                        placeholder="请输入剩余数" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="权重">
                    <el-input v-model="newBooksForm.weight" 
                        placeholder="请输入权重" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
				<el-button @click="showAddInfoFlag = false">取 消</el-button>
				<el-button type="primary" @click="addNewBookInfo()">确 定</el-button>
			</div>
        </el-dialog> 
    </div>
    
               
        
    
</template>

<script>

    import {getBooks, fineNewBook, addBook} from "../../api/index"
    
    export default {
        name: '',
        data() {
            return {
                //后端传入书本单
                booksForm:{
                    bookName: '',
                    subhead: '',
                    originalName: '',
                    author: '',
                    translator:'',
                    ISBN: '',
                    cover: '',
                    price: '',
                    chinaClass: '',
                    page: '',
                    category: '',
                    pubDate: '',
                    pubLisher :'',
                    pubLisherAdd: '',
                    binding: '',
                    language: '',
                    prospectus: '',
                    location: '',
                    quantity: '',
                    surplus: '',
                    weight: '',
                },
                //自建表单
                newBooksForm:{
                    bookName: '',
                    subhead: '',
                    originalName: '',
                    author: '',
                    translator:'',
                    ISBN: '',
                    cover: '',
                    price: '',
                    chinaClass: '',
                    page: '',
                    category: '',
                    pubDate: '',
                    pubLisher :'',
                    pubLisherAdd: '',
                    binding: '',
                    language: '',
                    prospectus: '',
                    location: '',
                    quantity: '',
                    surplus: '',
                    weight: '',
                },
                fineISBNForm:{
                    isbn:'',
                },
                showAddInfoFlag:false,

                dataList: "",
                dialogImageUrl: '',
            }
        },


        methods: {
            //初始化界面书本信息
            initBooksForm(){
                getBooks().then(res =>{
                    this.booksForm.bookName = res.data.bookName;
                    this.booksForm.subhead = res.data.subhead;
                    this.booksForm.originalName = res.data.originalName;
                    this.booksForm.author = res.data.author;
                    this.booksForm.translator = res.data.translator;
                    this.booksForm.ISBN = res.data.ISBN;
                    this.booksForm.cover = res.data.cover;
                    this.booksForm.price = res.data.price;
                    this.booksForm.chinaClass = res.data.chinaClass;
                    this.booksForm.page = res.data.page;
                    this.booksForm.category = res.data.category;
                    this.booksForm.pubDate = res.data.pubDate;
                    this.booksForm.pubLisher = res.data.pubLisher;
                    this.booksForm.pubLisherAdd = res.data.pubLisherAdd;
                    this.booksForm.binding = res.data.binding;
                    this.booksForm.language = res.data.language;
                    this.booksForm.prospectus = res.data.prospectus;
                    this.booksForm.location = res.data.location;
                    this.booksForm.quantity = res.data.quantity;
                    this.booksForm.surplus = res.data.surplus;
                    this.booksForm.weight = res.data.weight;
                })
            },

            //初始化界面书本信息
            initNewBook(){
                this.newBooksForm = {
                    bookName: '',
                    subhead: '',
                    originalName: '',
                    author: '',
                    translator:'',
                    ISBN: '',
                    cover: '',
                    price: '',
                    chinaClass: '',
                    page: '',
                    category: '',
                    pubDate: '',
                    pubLisher :'',
                    pubLisherAdd: '',
                    binding: '',
                    language: '',
                    prospectus: '',
                    location: '',
                    quantity: '',
                    surplus: '',
                    weight: '',
                }
            },
    
            open(){
                showAddInfoFlag = true;
                this.initNewBook;
            },

            postNewISBN(){
                if(!this.newBooksForm.ISBN == ''){
                    fineNewBook(this.newBooksForm.ISBN).then(res =>{
                        // console.log(this.newBooksForm);
                        this.newBooksForm = res.data[0];
                        console.log(this.newBooksForm.cover);
                        this.dialogImageUrl = this.newBooksForm.cover;
                        console.log(this.dialogImageUrl)
                    });
                };
            },

            addNewBookInfo(){
                console.log("dianjichengg")
                addBook(this.newBooksForm).then(res =>{
                    this.$message({
						message: res.msg,
						type: 'success'
					});
                    
                    this.showAddFlag = false;
                })
            },
            
        },

        watch:{

        }
    }
    
</script>

<style scoped>
button{
    /* background-color: #66CC99; */
    float: right;
}

.bookHeader{
    width: 15rem;
    float: right;
    height: 40px;
    padding-left: 0.5rem;
}

.el-divider{
    border-top: 5px;
}
</style>