<template>
  <div class="home">
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">Check out recent Books</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="card" v-for="book in books" v-bind:key="book.id">
          <div class="card-content">
            <p class="title">{{ book.title }}</p>
            <p class="subtitle">{{ book.created_at.toDateString() }}</p>
            <p v-if="book.read" class="subtitle has-text-success">Complete!</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  data() {
    return {
      books: [
        {
          id: 0,
          title: "Ender's Game",
          author: "Orson Scott Card",
          genre: "Sci Fi",
          read: true,
          created_at: new Date(2017, 12, 1)
        },
        {
          id: 1,
          title: "Leviathan Wakes",
          author: "James S. A. Corey",
          genre: "Sci Fi",
          read: true,
          created_at: new Date(2017, 12, 1)
        },
        {
          id: 2,
          title: "War and Peace",
          author: "Leo Tolstoy",
          genre: "Classics",
          read: false,
          created_at: new Date(2017, 12, 1)
        },
        {
          id: 3,
          title: "Harry Potter and the Socerers Stone",
          author: "JK Rowling",
          genre: "Fantasy",
          read: true,
          created_at: new Date(2017, 12, 1)
        },
        {
          id: 4,
          title: "The 4 Hour Workweek",
          author: "Tim Ferriss",
          genre: "Self Help",
          read: true,
          created_at: new Date(2017, 12, 1)
        }
      ]
    };
  }
};
</script>
