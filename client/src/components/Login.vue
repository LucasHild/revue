<template lang="html">
  <div class="login">
    <form @submit.prevent="login">
      <h1>Login</h1>
      <p class="error">{{ error }}</p>
      <input v-model="username" type="text" placeholder="Username">
      <input v-model="password" type="password" placeholder="Password">
      <input class="button" type="submit" value="Login">
    </form>
  </div>
</template>

<script>
import AuthenticationService from '@/services/AuthenticationService'

export default {
  name: 'login',

  data() {
    return {
      username: '',
      password: '',
      error: null
    }
  },

  methods: {
    login() {
      AuthenticationService.login({
        username: this.username,
        password: this.password,
      })
      .then(response => {
        console.log(response.data);
        this.$store.dispatch('setToken', response.data.token)
        this.$store.dispatch('setUser', response.data.user)
      })
      .catch(e => {
        this.error = e.response.data.error
      })
    }
  }
}
</script>

<style scoped lang="css">
.login {
  background: rgb(23, 92, 93);
  background-image: url(/static/newsletter-login.jpg);
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;

  width: 100%;
  height: calc(100vh - 49px);
  position: relative;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

form {
  background-color: white;
  max-width: 500px;
  width: 90%;
  margin-bottom: 49px;
  padding: 20px;
}

h1 {
  text-align: center;
}

input {
  display: block;
  width: 100%;
  margin: 0;
  border: none;
  background: rgb(223, 224, 221);
  padding: 15px;
  text-align: center;
  margin: 20px 0;

  -webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */
  -moz-box-sizing: border-box;    /* Firefox, other Gecko */
  box-sizing: border-box;         /* Opera/IE 8+ */
}
</style>
