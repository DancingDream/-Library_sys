import http from "../utils/http.js"

//管理员类
//登出接口
export function exit(token){
	
	return http.get('/admin/exit/', {params: token});
}

//获取用户登陆信息
export function getLoginUser(token){
	return http.get('/admin/info/', {params: {token: token}});
}

// 传递登录信息
export function login(param){
	
	return http.post('/admin/login/', param);
}

//注册信息
export function register(param){
	
	return http.post('/admin/register/', param);
}


//书本类
// 获取书本信息
export function getBooks(){

	return http.get('/books/info/', param);
}

//添加书籍
export function addBook(param){
	
	return http.post('/books/add/', param);
}

//查找新书
export function fineNewBook(param){
	
	return http.post('/books/new/', {isbn:param});
}

//修改书本信息
export function amendBook(param){
	
	return http.post('/books/amend/', param);
}

