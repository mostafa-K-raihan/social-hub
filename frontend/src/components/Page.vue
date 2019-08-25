<template>
  <div class="page">
    <Topbar/>
    <Sidebar/>
    <MainContent :url="url"/>
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
  },
  data() {
    return {
      url : 'text'
    }
  },
  created() {
    let url = new URL(location.href);
    if(url.pathname.indexOf('media') !==-1) {
      this.url = 'media'
    }else if(url.pathname.indexOf('text') !== -1) {
      this.url = 'text'
    }
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
