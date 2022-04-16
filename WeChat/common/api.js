import http from "./ajax.js"

export function getBooks() {
	return http.get('/books/info/')
}

export function getUserInfo(token) {
	return http.get('/user/info/', {
		token: token
	})
}

export function exit(token) {
	return http.get('/user/exit/', {
		token: token
	})
}

export function register(param) {

	return http.post('/user/register/', param);
}

export function login(param) {

	return http.post('/user/login/', param);
}
