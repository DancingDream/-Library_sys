import http from "../utils/http.js"

// 获取书本信息
export function getBooks(){
	return http.get('/books/')
}

// 传递登录信息
export function login(param){
	
	return http.post('/login/', param);
}

//登出接口
export function exit(token){
	
	return http.get('/exit/', {params: token});
}

//注册信息
export function register(param){
	
	return http.post('/register/', param);
}