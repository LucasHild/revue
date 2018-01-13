<template lang="html">
  <div class="user container">
    <h1>{{ username }}</h1>
    <div class="len-posts button">{{ lenPosts }} Posts</div>
    <div class="stars button">{{ stars }} Stars</div>

    <PostPreview v-for="post in posts" :img="post.image" :description="post.content" :id="post.id" :key="post.id">{{ post.title }}</PostPreview>
  </div>
</template>

<script>
import PostPreview from '@/components/PostPreview'

export default {
  name: 'user',
  components: { PostPreview },
  data() {
    return {
      username: this.$route.params.username,
      posts: [
        {
          id: 500,
          title: 'Hello World',
          user: { 'username': 'Lanseuo' },
          image: 'http://fillmurray.com/600/200',
          created: { date: '7 January 2018', time: '16:03' },
          content: 'Lorem ipsum dolor sit <strong>amet</strong>, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos e',
          comments: [
            {
              id: 11,
              user: { 'username': 'Lanseuo' },
              created: { date: '7 January 2018', time: '16:03' },
              content: 'Lorem ipsum dolor sit <strong>amet</strong>, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos e',
            },
            {
              id: 12,
              user: { 'username': 'Lanseuo' },
              created: { date: '7 January 2018', time: '16:03' },
              content: 'Lorem ipsum dolor sit <strong>amet</strong>, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos e',
            }
          ]
        }
      ],
      stars: 16
    }
  },

  computed: {
    lenPosts() {
      return this.posts.length
    }
  }
}
</script>

<style lang="css">
.button {
  background: blue;
  display: inline;
  padding: 10px 20px;
}

.stars {
  background-color: rgb(194, 194, 36) !important;
}

.post-preview:first-of-type {
  margin-top: 25px;
}
</style>
