<template lang="html">
  <div class="subvue-info">
    <h2>{{ name }}</h2>
    <p>{{ description }}</p>

    <p><strong>Moderators</strong></p>
    <ul>
      <li v-for="moderator in moderators" :key="moderator.username">
        <router-link :to="{ name: 'User', params: {username: moderator.username} }">{{ moderator.username }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import SubvueService from '@/services/SubvueService'

export default {
  name: 'subvue-info',

  props: ['permalink'],

  data() {
    return {
      name: '',
      description: '',
      moderators: []
    }
  },

  mounted() {
    SubvueService.item(this.permalink)
      .then(response => {
        this.name = response.data.name
        this.description = response.data.description
        this.moderators = response.data.moderators
      })
      .catch(e => {
        console.log(e);
      })
  }
}
</script>

<style lang="css">
.subvue-info {
  padding: 10px;
}

.moderator {
  color: rgb(48, 99, 219);
  cursor: pointer;
}
</style>
