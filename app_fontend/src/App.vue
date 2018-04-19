<template>
  <div id="app">
    <div class="topBar"></div>
    <side-bar v-on:showHome="showPage('showhome')" v-on:showNoteBook="showPage('shownote')" v-on:showAnniversary="showPage('showanni')"/>
    <home v-if="showhome"/>
    <note-book  v-if="shownote"/>
    <anniversary v-if="showanni"/>
  </div>
</template>

<script>
import sideBar from './components/sideBar'
import home from './components/home'
import noteBook from './components/noteBook'
import anniversary from './components/anniversary'

export default {
  name: 'App',
  components:{
    sideBar,
    home,
    noteBook,
    anniversary
  },
  data(){
    return {
      showhome:true,
      shownote:false,
      showanni:false,
      showques:false
    };
  },
  methods:{
    showPage(page){
      this.showhome=false
      this.shownote=false
      this.showanni=false
      this.showques=false
      if(page=='showhome'){
        this.showhome=true
      }else if(page=='shownote'){
        this.shownote=true
      }else if(page=='showanni'){
        this.showanni=true

      }
    }
  },
  mounted(){
  }
}
</script>

<style>
html,body,#app{
  height:100%;
  overflow-x: hidden;
  margin:0;
  padding:0;
  background: rgba(0, 0, 0, 0.01);
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
}
a{
  text-decoration: none;
  color:#000;
}
.topBar{
  height:4px;
  width: 100%;
  background:rgba(132, 165, 146,0.45);
  position: absolute;
  top: 0;
}
</style>
