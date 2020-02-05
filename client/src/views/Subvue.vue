<template lang="html">
  <div class="subvue">
    <div class="container">
      <h1>Recent Posts</h1>
      <PostPreview :hideSubvue="true" v-for="post in posts" :key="post.id" :post="post">
        {{ post.title }}
      </PostPreview>

      <CreateButton></CreateButton>
    </div>
    
    <SubvueInfo class="subvue-info" v-if="subvue" :subvue="subvue"></SubvueInfo>
    <!-- Only show it if data was fetched -->
    <div v-else=""></div>
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
            posts: [],
            subvue: null
        }
    },

    mounted() {
        this.fetchData()
    },

    methods: {
        fetchData() {
            SubvuesService.item(this.permalink)
                .then(response => {
                    this.subvue = response.data
                })
            SubvuesService.posts(this.permalink)
                .then(response => {
                    this.posts = response.data
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
