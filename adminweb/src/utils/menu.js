
export const adminMenus = {
    path: '/home',
    name: 'home',
    component: require("../views/home.vue").default,
    children: [
        {
            path: '/index',
            name: '系统首页',
            icon: "fa fa-home",
            component: require("../views/pages/index.vue").default
        },
        {
            path: '/books',
            name: '图书管理',
            icon: "fa fa-book",
            component: require("../views/pages/boooks.vue").default
        },
        {
            path: '/users',
            name: '用户管理',
            icon: "fa fa-users",
            component: require("../views/pages/users.vue").default
        },
        {
            path: '/record',
            name: '借还记录',
            icon: "fa fa-history",
            component: require("../views/pages/record.vue").default
        },
        {
            path: '/notices',
            name: '通知信息管理',
            icon: "fa fa-bullhorn",
            component: require("../views/pages/notices.vue").default
        }
    ]
};

export default function initMenu(router, store){
    // let token = null;
    // if(store.state.token){

    //     token = store.state.token;
    // }else{

    //     token = sessionStorage.getItem("token");
    //     store.state.token = sessionStorage.getItem("token");
    // }

    router.addRoute(adminMenus);
    store.commit("setMenus", adminMenus); 
}