import http from "../utils/http.js";

/** 系统接口 */
export function getBooks(){
	return http.get('/books/info/')
}

export function boBookInfo(param){
	return http.post('/record/boBook/', param)
}

export function reBookInfo(params){
	return http.post('/record/reBook/', params)
}