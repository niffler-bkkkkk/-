<template>
  <div class="homeContainer">
    <div class="markdownContent" v-for="(item,index) in compiledMd" :key="index">
      <div class="delete" :class="[showAllContent==index?showDelete:'']"  v-on:click="deleteNote(index)">&times;</div>
    <div class="markdownText" :class="[showAllContent==index?allMarkdownText:'']" v-html="item"></div>
    <div class="noteDate" :class="[showAllContent==index?showNotedate:'']">{{ datearray[index] }}</div>
    <div class="readBtn" v-on:click="showAll(index)">阅读全文></div>
    </div>
  </div>
</template>
<script>
import marked from "marked";
let hljs = require("highlight.js");
import "highlight.js/styles/default.css";

marked.setOptions({
  renderer: new marked.Renderer(),
  gfm: true,
  tables: true,
  breaks: false,
  pedantic: false,
  sanitize: false,
  smartLists: true,
  smartypants: false,
  highlight: function(code, lang) {
    if (lang && hljs.getLanguage(lang)) {
      return hljs.highlight(lang, code, true).value;
    } else {
      return hljs.highlightAuto(code).value;
    }
  }
});
export default {
  name: "HelloWorld",
  data() {
    return {
      noteData: [],
      note: [],
      datearray: [],
      compiledMd: [],
      showAllContent: 0,
      showDelete: "showDelete",
      allMarkdownText: "allMarkdownText",
      showNotedate: "showNotedate"
    };
  },
  methods: {
    getNote() {
      this.axios.get("http://127.0.0.1:4000/getNotebook").then(res => {
        this.noteData = res.data;
        this.compileMd();
      });
    },
    compileMd() {
      for (var i = 0; i < this.noteData.length; i++) {
        var note = this.noteData[i].note;
        var date = this.noteData[i].noteDate;
        var markednote = marked(note);
        this.$set(this.note, i, note);
        this.$set(this.compiledMd, i, markednote);
        this.$set(this.datearray, i, date);
      }
    },
    showAll(index) {
      this.showAllContent = index;
    },
    deleteNote(index) {
      let params = new URLSearchParams();
      params.append("note", this.note[index]);
      if (confirm("确定要删除该条记录吗？")) {
        this.axios.post("http://127.0.0.1:4000/deleteNote", params).then(res => {
          if (res.data == "200") {
            alert("记录已被删除");
            this.getNote();
          } else {
            alert("出现了故障┑(￣Д ￣)┍请稍后再试～");
          }
        })
      } else {
        return false;
      }
    }
  },
  mounted() {
    this.getNote();
  }
};
</script>
<style scoped>
.homeContainer {
  width: 60%;
  margin: 0 auto;
  margin-top: 4px;
}
.markdownContent {
  color: rgba(0, 0, 0, 0.65);
  padding: 30px;
  margin-bottom: 10px;
  background: #fff;
  box-shadow: 0 0px 2px rgba(0, 0, 0, 0.157);
}
.markdownText {
  min-height: 100px;
  max-height: 160px;
  overflow: hidden;
}
.allMarkdownText {
  height: auto;
  max-height:800px;
  overflow: visible;
}
.readBtn {
  width: 100px;
  background: rgba(0, 0, 0, 0.65);
  margin: 0 auto;
  text-align: center;
  cursor: pointer;
  color: #fff;
}
.readBtn:hover {
  background: rgba(0, 0, 0, 0.85);
}
.delete {
  float: right;
  color: #fff;
  font-size: 24px;
  height: 24px;
  line-height: 24px;
  text-align: center;
  border-radius: 50%;
  width: 24px;
  cursor: pointer;
  background: rgba(0, 0, 0, 0.65);
  display: none;
}
.delete:hover {
  color: #fff;
  background: rgba(0, 0, 0, 0.85);
}
.showDelete {
  display: block;
}
.noteDate {
  font-weight: 500;
  text-align: right;
  display: none;
}
.showNotedate {
  display: block;
}
</style>
