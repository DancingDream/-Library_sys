import http from "../utils/http.js"

//管理员类
//登出接口
export function exit(token) {

	return http.get('/admin/exit/', { params: token });
}

//获取用户登陆信息
export function getLoginUser(token) {
	return http.get('/admin/info/', { params: { token: token } });
}

//更新用户数据
export function updLoginUserInfo(params) {

	return http.post('/admin/info/', params);
}

// 传递登录信息
export function login(param) {

	return http.post('/admin/login/', param);
}

//注册信息
export function register(param) {

	return http.post('/admin/register/', param);
}

//更新密码
export function updLoginUserPwd(token, newPwd) {

	return http.post('/admin/pwd/', { token: token, newPwd: newPwd });
}

//获取首页信息
export function getData() {

	return http.get('/admin/data/');
}


//书本类
// 获取书本信息
export function getBooks() {

	return http.get('/books/info/');
}

//添加书籍
export function addBook(param) {

	return http.post('/books/add/', param);
}

//查找新书
export function fineNewBook(param) {

	return http.post('/books/new/', { isbn: param });
}

//修改书本信息
export function amendBook(param) {

	return http.post('/books/amend/', param);
}


//公告类
//获取公告
export function getNotice() {

	return http.get('/notice/getInfo/');
}

//发送新公告
export function addNotice(param) {

	return http.post('/notice/add/', param);
}

//修改公告
export function amenNotice(param) {

	return http.post('/notice/amen/', param);
}


//用户类
//获取用户信息
export function getUsers() {

	return http.get('/user/infos/');
}

//更新用户状态
export function updateUserState(param) {

	return http.post('/user/upState/', param);
}

// 记录类
export function getRecord() {

	return http.get('/record/infos/');
}

