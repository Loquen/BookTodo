import Vue from "vue";
import Vuex from "vuex";

import { fetchBooks, postNewBook, authenticate, register } from "@/api";
import { isValidJwt, EventBus } from "@/utils";

Vue.use(Vuex);

const state = {
  // Single source of data
  books: [],
  user: {},
  jwt: ""
};

const actions = {
  // async operations
  login(context, userData) {
    context.commit("setUserData", { userData });
    return authenticate(userData)
      .then(res => context.commit("setJwtToken", { jwt: res.data }))
      .catch(err => {
        console.log("Error Authenticating: ", err);
        EventBus.$emit("failedAuthentication", err);
      });
  },
  register(context, userData) {
    context.commit("setUserData", { userData });
    return register(userData)
      .then(context.dispatch("login", userData))
      .catch(err => {
        console.log("Error Registering: ", err);
        EventBus.$emit("failedRegistering: ", err);
      });
  },
  logout(context) {
    context.commit("logout");
  },
  loadBooks(context) {
    return fetchBooks().then(res =>
      context.commit("setBooks", { books: res.data })
    );
  },
  submitNewBook(context, book) {
    return postNewBook(book, context.state.jwt.token);
  }
};

const mutations = {
  // isolated data changes
  setBooks(state, payload) {
    state.books = payload.books;
  },
  setUserData(state, payload) {
    console.log("setUserData payload = ", payload);
    state.userData = payload.userData;
  },
  setJwtToken(state, payload) {
    console.log("setJwtToken payload = ", payload);
    localStorage.token = payload.jwt.token;
    state.jwt = payload.jwt;
  },
  logout(state) {
    // remove user from local storage to log user out
    localStorage.removeItem("token");
    state.jwt = "";
    state.user = {};
  }
};

const getters = {
  // reusable data accessors
  isAuthenticated(state) {
    return isValidJwt(state.jwt.token);
  }
};

const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});

export default store;
