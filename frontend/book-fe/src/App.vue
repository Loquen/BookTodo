<template>
  <div id="app">
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
          <router-link class="navbar-item" to="/about">About</router-link>
        </div>
        <div class="navbar-end"></div>
      </div>
    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
@import "~bulma/bulma";
</style>
