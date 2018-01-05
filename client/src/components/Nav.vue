<template lang="html">
  <nav>
    <ul>
      <li><router-link :to="{ name: 'Home', params: {} }">ReVue</router-link></li>
      <li style="float:right"><router-link :to="{ name: 'SignUp', params: {} }">Sign Up</router-link></li>
      <li style="float:right"><router-link :to="{ name: 'Login', params: {} }">Login</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
}
</script>

<style scoped lang="css">
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
  }

  li {
    float: left;
  }

  li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none
  }

  li a:hover {
      background-color: #111;
  }

  nav .active {
    background-color: #4CAF50;
  }
</style>
