<template>
  <div id="markdownEditor">
    <mavon-editor  v-model="value" class="mavon-editor" :ishljs = "true" v-on:save="deleteOldNote()"></mavon-editor>
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
    deleteOldNote:function(){
      if(this.noteDate){
        let params = new URLSearchParams();
        params.append("note", this.note);
        this.axios.post("http://127.0.0.1:4000/deleteNote", params).then(res => {
          if(res.data=="200"){
            this.saveNote()
          }else{
            alert("更新失败...")
          }
        })
      }else{
        this.saveNote()
      }
    },
    saveNote:function(){
      let params = new URLSearchParams();
        params.append("noteDate", this.currentDate);
        params.append("note", this.value);
        if (this.value) {
          this.axios.post("http://127.0.0.1:4000/setNotebook", params).then(res => {
            if (res.data == "200") {
              alert("笔记已经被记录下来啦~")
            } else {
              alert("出现了故障┑(￣Д ￣)┍请稍后再试～");
            }
          })
        } else {
        alert("记录不能为空哦");
      }
      this.$emit("showHome")
    },
    editNote(){
      this.value=this.note
    }
  },
  mounted(){
    this.getCurrentDate()
    this.editNote()
  },
  props:['noteDate','note']
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
