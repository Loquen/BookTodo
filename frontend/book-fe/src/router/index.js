import Vue from "vue";
import Router from "vue-router";
import Home from "../views/Home.vue";
import NewBook from "../views/NewBook.vue";
import Login from "@/components/Login";
import store from "@/store";

Vue.use(Router);

export const router = new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/about",
      name: "About",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "../views/About.vue")
    },
    {
      path: "/books",
      name: "NewBook",
      component: NewBook
      // beforeEnter(to, from, next) {
      //   if (!store.getters.isAuthenticated) {
      //     next("/login");
      //   } else {
      //     next();
      //   }
      // }
    },
    {
      path: "/login",
      name: "Login",
      component: Login
    }
  ]
});

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access restricted page
  const publicPages = ["/login"];
  const authRequired = !publicPages.includes(to.path);

  if (authRequired && !store.getters.isAuthenticated) {
    return next("/login");
  }

  next();
});
