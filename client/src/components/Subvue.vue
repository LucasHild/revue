<template lang="html">
  <div class="subvue">
    <div class="container"></div>
    <SubvueInfo class="subvue-info" :permalink="permalink"></SubvueInfo>
  </div>

</template>

<script>
import SubvueInfo from '@/components/SubvueInfo'

export default {
  name: 'subvue',

  components: { SubvueInfo },

  data() {
    return {
      permalink: this.$route.params.name
    }
  },

  watch: {
    $route() {
      this.permalink = this.$route.params.name
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
