<template lang="html">
  <div class="post">
    <div class="body container">
      <h1>{{ title }}</h1>
      <h3>by <router-link :to="{ name: 'User', params: {'username': user.username} }">{{ user.username }}</router-link> on {{ created.date }} at {{ created.time }}</h3>
      <p v-html="content"></p>
      <i class="post-id">ID {{ id }}</i>
    </div>
    <div class="container">
      <h2>Comments</h2>
      <Comment v-for="comment in comments" :key="comment.id" :user="comment.user" :created="comment.created" :content="comment.content"></Comment>
    </div>
  </div>
</template>

<script>
import Comment from '@/components/Comment'

export default {
  name: 'post',
  components: { Comment },
  data() {
    return {
      id: this.$route.params.id,
      title: 'Hello World',
      user: { 'username': 'Lanseuo' },
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
  }
}
</script>

<style scoped lang="css">
  .body {
    background: #eeeeee;
  }

  h1 {
    margin: 0;
  }

  h3 {
    margin: 0;
    font-weight: 400;
  }

  .post-id {
    text-align: right;
    display: block;
  }
</style>
