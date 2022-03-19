import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path:'/register',
    name:'register',
    component:require("../views/register.vue").default,
  },
  {
    path:'/home',
    name:'home',
    component:require("../views/home.vue").default,
    // children:[
    //   {
    //     path:'/index',
    //     name:index,
    //     icon: "fa fa-home",
    //     component:require("../views/pages/index.vue").default
    //   }
    // ]
  }
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
