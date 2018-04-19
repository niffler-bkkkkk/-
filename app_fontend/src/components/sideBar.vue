<template>
  <div class="sideBar">
    <div class="listItem home" :class="[isActive==1?listItemActive:'']" v-on:click="listActive(1,'showHome')">
      <img class="Icon" src="../assets/shop.svg">
    <div class="functionList" :class="[isActive==1?functionListActive:'']">
      <img class="arrow-right" src="../assets/next.svg">
      <a class="text" href="#">主页</a>
      <img class="arrow-left" :class="[isActive==1?arrowLeftActive:'']" src="../assets/prev.svg">
    </div>
    </div>
    <div class="listItem noteBook" :class="[isActive==2?listItemActive:'']" v-on:click="listActive(2,'showNoteBook')">
      <img class="Icon" src="../assets/notebook.svg">
      <div class="functionList" :class="[isActive==2?functionListActive:'']">      
        <img class="arrow-right" src="../assets/next.svg">
        <a class="text" href="#">记事本</a>
        <img class="arrow-left" :class="[isActive==2?arrowLeftActive:'']" src="../assets/prev.svg">
      </div>
    </div>
    <div class="listItem anniversary" :class="[isActive==3?listItemActive:'']" v-on:click="listActive(3,'showAnniversary')">
      <img class="Icon" src="../assets/heart.svg">
      <div class="functionList" :class="[isActive==3?functionListActive:'']">      
        <img class="arrow-right" src="../assets/next.svg">
        <a class="text" href="#">纪念日</a>
        <img class="arrow-left" :class="[isActive==3?arrowLeftActive:'']" src="../assets/prev.svg">
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "sidebar",
  data() {
    return {
      listItemActive:"listItemActive",
      functionListActive:"functionListActive",
      arrowLeftActive:"arrowLeftActive",
      isActive:1
    }
  },
  methods: {
    listActive(index,show){
      this.isActive=index
      this.$emit(show)
    }
  }
};
</script>
<style scoped>
.sideBar {
  height:690px;
  min-width: 180px;
  width: 12%;
  display: inline-block;
  margin-top:4px;
  margin-left:40px;
  background: rgba(255, 255, 255, 0.85);
  box-shadow: 0 0px 2px rgba(0, 0, 0, 0.157);
}
.Icon {
  height: 32px;
  width: 32px;
}
.listItem {
  height: 50px;
  padding: 10px;
  display: flex;
  align-items: center;
  cursor: pointer;
}
.listItem:hover{
  background: rgba(132, 165, 146,0.45);
}
.functionList{
  display: flex;
  align-items: center;
  margin-left: 6px;
}
.arrow-right,
.arrow-left {
  height: 18px;
  width: 18px;
  margin: 4px;
}
.arrow-left{
  margin-left:26px;
  opacity: 0;
}
.listItem:hover .arrow-left{
  margin-left:4px;
  opacity: 1;
  transition: 0.2s ease-out .0s;
}
.listItem:hover .functionList{
  margin-left:20px;
  transition: 0.2s ease-out .0s;
}
.listItemActive{
  background: rgba(132, 165, 146,0.45);
}
.arrowLeftActive{
  margin-left:4px;
  opacity: 1;
}
.functionListActive{
  margin-left:20px;
}
</style>
