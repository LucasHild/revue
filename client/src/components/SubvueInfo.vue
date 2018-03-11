<template lang="html">
  <div class="subvue-info">
    <router-link class="heading" :to="{ name: 'Subvue', params: {name: subvue.permalink} }"><h2>{{ subvue.name }}</h2></router-link>
    <p>{{ subvue.description }}</p>

    <button @click="subscribe" v-if="!subscribed" class="subscribe-button">Subscribe</button>
    <button @click="unsubscribe" v-if="subscribed" class="subscribe-button">Unsubscibe</button>

    <p><strong>Moderators</strong></p>
    <ul>
      <li v-for="moderator in subvue.moderators" :key="moderator.username">
        <router-link :to="{ name: 'User', params: {username: moderator.username} }">{{ moderator.username }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import SubvuesService from '@/services/SubvuesService'
import UsersService from '@/services/UsersService'

export default {
  name: 'subvue-info',

  props: ['subvue'],

  data() {
    return {
      subscribed: false
    }
  },

  methods: {
    subscribe() {
      if (!this.$store.state.isUserLoggedIn) {
        this.$router.push({ name: 'Login' });
        return false
      }

      SubvuesService.subscribe(this.subvue.permalink)
        .then(response => {
          this.checkSubscribed();
        })
        .catch(e => {
          console.log(e);
        })
    },

    unsubscribe() {
      if (!this.$store.state.isUserLoggedIn) {
        this.$router.push({ name: 'Login' });
        return false
      }

      SubvuesService.unsubscribe(this.subvue.permalink)
        .then(response => {
          this.checkSubscribed();
        })
        .catch(e => {
          console.log(e);
        })
    },

    checkSubscribed() {
      if (!this.$store.state.isUserLoggedIn) {
        return false
      }

      UsersService.username(this.$store.state.user.username)
        .then(response => {
          var filteredSubscribedSubvues = response.data.subscribed.filter(s => {
            return s.permalink == this.subvue.permalink
          });
          this.subscribed = filteredSubscribedSubvues.length > 0
        })
        .catch(e => {
          console.log(e);
        })
    }
  },

  mounted() {
    this.checkSubscribed()
  },

  watch: {
    subvue() {
      this.checkSubscribed()
    }
  }
}
</script>

<style lang="css">
.heading {
  color: black;
}

.heading:hover {
  color: rgb(48, 99, 219);
}

.subvue-info {
  padding: 10px;
}

.subscribe-button {
  background-color: rgb(23, 92, 93);
  color: white;
  border: 0;
  padding: 10px 25px;
  cursor: pointer;
}

.subscribe-button:hover {
  background-color: rgb(19, 112, 113);
}

.moderator {
  color: rgb(48, 99, 219);
  cursor: pointer;
}
</style>
