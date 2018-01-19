<template lang="html">
  <div class="comment">
    <h4>by <a href="">{{ user.username }}</a> on {{ created.date }} at {{ created.time }}</a></h4>
    <p v-html="content"></p>
  </div>
</template>

<script>
export default {
  name: 'comment',
  props: [
    'user',
    'created',
    'content'
  ],
  data() {
    return {}
  }
}
</script>

<style scoped lang="css">
  .comment {
    background: #f2f2f2;
    padding: 20px 10px;
    margin-bottom: 20px;
  }

  h4 {
    margin: 5px 0;
  }

  p {
    margin: 5px 0;
  }
</style>
