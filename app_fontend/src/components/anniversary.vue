<template>
  <div class="canlendar">
    <div class="selectDate">
      <div class="currentMonth">{{ selectedMonth }}</div>
        <div class="selectContainer">
          <select v-model="selectedYear">
            <option v-for="(item,index) in allYear" :key="index" :value="item">{{ item }}</option>
          </select>
          <select v-model="selectedMon">
            <option v-for="(item,index) in allMon" :key="index" :value="item">{{ item }}</option>
          </select>
        </div>
        <div class="anniversaryText">
      <p>{{ countDown }}</p>天后是你们<br><p>{{ anniversary }}<br>{{ anniversaryYears }}</p>周年<br>的纪念日
    </div>
    </div>
    <div class="calendarContainer">
    <div class="weekContainer">
    <div class="weekItem" v-for="(item,index) in week" :key="index">{{ item }}</div>
    </div>
    <div class="dateContainer">
      <div class="line line1"></div>
      <div class="line line2"></div>
      <div class="line line3"></div>
      <div class="line line4"></div>
      <div class="line line5"></div>
      <div class="dateItem" v-for="(item,index) in dateInfo" :key="index" :class="[item.title==''?'':anniColor,item.date=='x'?blankDateItem:'',currentDateIndex==index?currentDateColor:'']" v-on:click="addAnniversary(index)" :title="item.title">{{ item.date }}</div>
    </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "anniversary",
  data() {
    return {
      countDown: 0,
      anniversary: "",
      anniversaryYears: 0,
      selectedMonth: "",
      selectedYear: 0,
      selectedMon: 0,
      currentYear: 0,
      currentMonth: 0,
      currentDate: 0,
      firstDay: 0,
      lastDate: 0,
      week: ["日", "一", "二", "三", "四", "五", "六"],
      month: ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."],
      allYear: [],
      allMon: [],
      dateInfo: [],
      blankItem: 0,
      blankDateItem: "blankDateItem",
      currentDateColor: "currentDateColor",
      currentDateIndex: 233,
      anni: [],
      anniDay: 0,
      anniColor: "anniColor",
      anniMon: "",
      anniDay: ""
    };
  },
  methods: {
    addAnniversary(index) {
      var anniversary = prompt("这一天是啥纪念日呢?");
      var anniYear = this.selectedYear;
      var anniMon = this.selectedMon;
      var anniDay = index - this.firstDay + 1;
      if (anniMon < 10) {
        anniMon = "0" + anniMon;
        this.anniMon = anniMon;
      }
      if (anniDay < 10) {
        anniDay = "0" + anniDay;
        this.anniDay = anniDay;
      }
      if (anniversary) {
        var date = anniYear + "/" + anniMon + "/" + anniDay;
        let params = new URLSearchParams();
        params.append("anniDate", date);
        params.append("anni", anniversary);
        if (anniversary) {
          this.axios.post("http://127.0.0.1:4000/anniversary", params).then(res => {
            if (res.data == "200") {
              alert("这一天记录下来啦～");
              this.getAnni();
            } else {
              alert("出现了故障┑(￣Д ￣)┍请稍后再试～");
            }
          });
        }
      } else if (anniversary === null) {
        return false;
      } else {
        alert("请输入纪念日w");
      }
    },
    getApointedDate(year, month) {
      var date = new Date(year, month, 0);
      this.lastDate = date.getDate();
      date.setDate(1);
      this.firstDay = date.getDay();
    },
    getCurrentDate() {
      var date = new Date();
      var currentYear = date.getFullYear();
      var currentMonth = date.getMonth();
      var currentDate = date.getDate();
      this.currentYear = currentYear;
      this.currentMonth = currentMonth + 1;
      this.currentDate = currentDate;
      this.selectMonth = this.month[currentMonth];
      this.selectedYear = currentYear;
      this.selectedMon = currentMonth + 1;
    },
    setAllYear() {
      for (let i = 2018; i > 1990; i--) {
        this.allYear.push(i);
      }
    },
    setAllMon() {
      for (let i = 1; i < 13; i++) {
        this.allMon.push(i);
      }
    },
    CountDown(annidate, currentdate) {
      var adate, date1, date2, cout;
      adate = annidate.split("/");
      date1 = new Date(adate[1] + "/" + adate[2] + "/" + adate[0]);
      adate = currentdate.split("/");
      date2 = new Date(adate[1] + "/" + adate[2] + "/" + adate[0]);
      var count = parseInt((date1 - date2) / 1000 / 60 / 60 / 24);
      return count;
    },
    getAnni() {
      var currentYear = this.currentYear.toString();
      var currentMonth = this.currentMonth.toString();
      var currentDate = this.currentDate.toString();
      if (this.currentMonth < 10) {
        var currentMonth = "0" + this.currentMonth.toString();
      }
      if (this.currentDate < 10) {
        var currentDate = "0" + this.currentDate.toString();
      }
      var current = currentYear + "/" + currentMonth + "/" + currentDate;
      this.axios.get("http://127.0.0.1:4000/getAnni").then(res => {
        this.anni = res.data;
        this.anni.sort(function(a, b) {
          return Date.parse(a.anniDate) - Date.parse(b.anniDate);
        });
        for (var i = 0; i < this.anni.length; i++) {
          if (current.slice(5) <= this.anni[i].anniDate.slice(5)) {
            break;
          }
        }
        if (i < this.anni.length) {
          var anniversaryYears = this.currentYear - this.anni[i].anniDate.slice(0, 4);
          var count = this.CountDown(this.currentYear + "/" + this.anni[i].anniDate.slice(5), current);
          if (anniversaryYears) {
            this.anniversaryYears = anniversaryYears;
            this.anniversary = this.anni[i].anni;
            this.countDown = count;
          }
        }
        this.setTitle();
        this.setCurrentDateColor();
      });
    },
    setTitle() {
      this.dateInfo = [];
      var anniMon = this.selectedMon;
      if (anniMon < 10) {
        anniMon = "0" + anniMon;
      }
      var blank = Number(this.firstDay);
      for (var e = 0; e < blank; e++) {
        this.$set(this.dateInfo, e, { date: "x", title: "" });
      }
      for (var i = 1; i <= this.lastDate; i++) {
        this.$set(this.dateInfo, e, { date: i, title: "" });
        e++;
      }
      for (var i = 0; i < this.anni.length; i++) {
        if (anniMon == this.anni[i].anniDate.slice(5, 7)) {
          var day = this.anni[i].anniDate.slice(8);
          if (day.slice(0, 1) == "0") {
            day = day.slice(1);
          }
          for (var j = 0; j < this.dateInfo.length; j++) {
            if (day == this.dateInfo[j].date) {
              this.$set(this.dateInfo, j, { date: day, title: this.anni[i].anni });
            }
          }
        }
      }
    },
    setCurrentDateColor() {
      if (this.selectedYear == this.currentYear && this.selectedMon == this.currentMonth) {
        this.currentDateIndex = this.currentDate + this.firstDay - 1;
      }else{
        this.currentDateIndex=233
      }
    }
  },
  mounted() {
    this.getCurrentDate();
    this.setAllYear();
    this.setAllMon();
    this.getAnni();
  },
  watch: {
    selectedYear: function getNewCanlendar(value) {
      this.getApointedDate(value, this.selectedMon);
      this.getAnni();
    },
    selectedMon: function getNewCanlendar(value) {
      this.getApointedDate(this.selectedYear, value);
      this.selectedMonth = this.month[value - 1];
      this.getAnni();
    }
  }
};
</script>
<style scoped>
.anniversaryText {
  font-size: 30px;
  color: #f4a460;
  font-weight: 500;
  margin-top: 60px;
}
.anniversaryText p {
  display: inline;
  font-size: 50px;
  color: #f08080;
}
.canlendar {
  height: 100%;
  display: flex;
  flex-direction: row;
  margin: 0 auto;
  margin-top: 4px;
}
.selectDate {
  background: rgba(255, 255, 255, 0.85);
  box-shadow: 0 0px 2px rgba(0, 0, 0, 0.157);
  height: 690px;
  width: 25vw;
  min-width: 300px;
  margin-right: 20px;
  display: flex;
  align-items: center;
  flex-direction: column;
}
.selectContainer {
  display: flex;
  flex-direction: row;
}
.currentMonth {
  color: rgba(132, 165, 146, 1);
  font-size: 60px;
  font-weight: 500;
}
.calendarContainer {
  width: 700px;
  height: 685px;
  overflow: hidden;
  box-shadow: 0 0px 2px rgba(0, 0, 0, 0.157);
  background: rgba(255, 255, 255, 0.85);
}
.weekItem,
.dateItem {
  font-size: 20px;
  height: 54px;
  width: 54px;
  line-height: 54px;
  text-align: center;
  vertical-align: center;
  display: inline-block;
  margin: 23px;
  cursor: pointer;
}
.weekItem {
  height: 40px;
  line-height: 40px;
}
.dateItem {
  box-shadow: 0 0px 2px rgba(0, 0, 0, 0.157);
  border-radius: 50%;
  background: rgba(132, 165, 146, 0.25);
}
.dateItem:hover {
  background: rgba(132, 165, 146, 0.45);
}
.blankDateItem {
  background: transparent;
  pointer-events: none;
  box-shadow: none;
  font-size: 0;
}
.weekContainer {
  border-bottom: 1px solid rgba(0, 0, 0, 0.25);
}
.dateContainer {
  position: relative;
}
.line {
  width: 100%;
  height: 1px;
  background: rgba(0, 0, 0, 0.25);
  position: absolute;
  top: 100px;
}
.line2 {
  top: 200px;
}
.line3 {
  top: 300px;
}
.line4 {
  top: 400px;
}
.line5 {
  top: 500px;
}
select {
  box-shadow: 0 0px 2px rgba(0, 0, 0, 0.157);
  margin: 20px;
  width: 120px;
  height: 20px;
  outline: 0;
  background: transparent;
  border: 1px solid rgba(0, 0, 0, 0.25);
}
.anniColor {
  background: #f4a460;
  opacity: 0.85;
}
.anniColor:hover {
  background: #f4a460;
  opacity: 1;
}
.currentDateColor {
  background:#f08080;
  opacity: 0.85;
}
.currentDateColor:hover{
  background: #f08080;
  opacity: 1;
}
</style>
