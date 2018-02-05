<template lang="html">
  <div class="subvue">
    <div class="container">
      <h1>Recenst Posts</h1>
      <PostPreview v-for="post in posts" :key="post.id" :post="post">
        {{ post.title }}
      </PostPreview>

      <CreateButton></CreateButton>
    </div>
    <SubvueInfo class="subvue-info" :permalink="permalink"></SubvueInfo>
  </div>

</template>

<script>
import SubvueInfo from '@/components/SubvueInfo'
import CreateButton from '@/components/CreateButton'
import PostPreview from '@/components/PostPreview'
import SubvuesService from '@/services/SubvuesService'

export default {
  name: 'subvue',

  components: { SubvueInfo, CreateButton, PostPreview },

  data() {
    return {
      permalink: this.$route.params.name,
      posts: []
    }
  },

  mounted() {
    this.fetchData()
  },

  methods: {
    fetchData() {
      SubvuesService.posts(this.permalink)
        .then(response => {
          this.posts = response.data
        })
        .catch(e => {
          console.log(e);
        })
    }
  },

  watch: {
    $route() {
      this.permalink = this.$route.params.name
      this.fetchData()
    }
  }
}
</script>

<style scoped lang="css">
.container {
  width: 80%;
  float: left;
}

.subvue-info {
  width: 20%;
  float: right;
}
</style>
