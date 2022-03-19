import http from "../utils/http.js";

/** 系统接口 */
export function getBooks(){
	return http.get('/books/')
}