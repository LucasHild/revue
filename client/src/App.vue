<template>
  <div id="app">
    <Nav/>
    <main>
      <router-view/>
    </main>
  </div>
</template>

<script>
import Nav from '@/components/Nav'

export default {
  name: 'app',
  components: {Nav}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
