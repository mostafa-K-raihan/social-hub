<template>
  <div class="page">
    <Topbar/>
    <Sidebar/>
    <MainContent/>
    <Footer/>
  </div>
</template>

<script>

import Topbar  from "./Topbar";
import Sidebar from "./Sidebar";
import MainContent from "./MainContent";
import Footer from "./Footer";
export default {
  name: 'Page',
  components: {
    Footer,
    Topbar,
    Sidebar,
    MainContent
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .page {
    display: grid;
    grid-template-columns: 10% 1fr;
    grid-template-rows: 10% 1fr 10%;
    grid-gap: .5rem;
    border: 1px solid black;
    padding : .5rem;
    height: 100vh;
  }

</style>
