import ajax from 'uni-ajax'
import qs from 'qs'

// ajax.defaults.headers['Content-Type'] = 'application/x-www-form-urlencoded';

const instance = ajax.create({
  // 初始配置
  baseURL: 'http://localhost:8000/api',
  timeout: 15000 ,
  header:{
	  ['Content-Type']: 'application/x-www-form-urlencoded',
  }
})

// 添加请求拦截器
instance.interceptors.request.use(
  config => {
    // 在发送请求前做些什么
	if(config.method === "post"){
			
			config.data = qs.stringify(config.data,  { indices: false });
		}
	
    return config
  },
  error => {
    // 对请求错误做些什么
    return Promise.reject(error)
  }
)

// 添加响应拦截器
instance.interceptors.response.use(
  response => {
    // 对响应数据做些什么
	if (response.data.code == 0) {
	
				return response.data;
	
			}else if (response.data.code == 1){
	
				return response.data;
			} else {
	
				uni.showToast({
					title: response.data.msg,
					icon:'error',
				});
				return Promise.reject(response.data);
			}
  },
  error => {
    // 对响应错误做些什么
	uni.showToast({
		title: '系统异常，请求中断',
		icon:'error',
	});
    return Promise.reject(error)
  }
)

// 导出 create 创建后的实例
export default instance