<template>
  <div id="markdownEditor">
    <mavon-editor  v-model="value" class="mavon-editor" :ishljs = "true" v-on:save="saveNote(value)"></mavon-editor>
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      value:'',
      currentDate:''
    }
  },
  methods:{
    getCurrentDate:function(){
      var date = new Date();
      var currentYear = date.getFullYear();
      var currentMonth = date.getMonth()+1;
      var currentDate = date.getDate();
      this.currentDate=currentYear+'-'+currentMonth+'-'+currentDate
    },
    saveNote:function(value){
      let params = new URLSearchParams();
        params.append("noteDate", this.currentDate);
        params.append("note", value);
        if (value) {
          this.axios.post("http://127.0.0.1:4000/setNotebook", params).then(res => {
            if (res.data == "200") {
              alert("笔记记录下来啦～");
            } else {
              alert("出现了故障┑(￣Д ￣)┍请稍后再试～");
            }
          })
        } else {
        alert("记录不能为空哦");
      }
    }
  },
  mounted(){
    this.getCurrentDate()
  }
}
</script>
<style scoped>
  #markdownEditor{
    height:690px;
    display: inline-block;
    margin:0 auto;
    margin-top:4px;
    box-shadow: 0 0px 2px rgba(0, 0, 0, 0.157)!important;
    overflow: hidden;
  }
  .mavon-editor{
    height:100%;
  }
</style>
