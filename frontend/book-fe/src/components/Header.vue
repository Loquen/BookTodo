<template>
  <div class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link class="navbar-item" to="/">
        <font-awesome-icon icon="book" />
      </router-link>
      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/books" v-if="isAuthenticated" class="navbar-item">
          Create Book
        </router-link>
        <router-link v-if="!isAuthenticated" to="/login" class="navbar-item">
          Login / Register
        </router-link>
        <a @click="logout" v-if="isAuthenticated" class="navbar-item">
          Logout
        </a>
      </div>
      <div class="navbar-end"></div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => this.$router.push("/login"));
    }
  }
};
</script>

<style lang="scss">
.nav-div {
  cursor: pointer;
}
</style>
