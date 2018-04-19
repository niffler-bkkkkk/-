import pymysql
import json

class sqlconnect:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='appdb', charset='utf8')
        self.cur = self.conn.cursor()

    def setNote(self,noteDate,note):
        sql = "INSERT INTO notebook (noteDate,note) VALUES (\'%s\', \'%s\')" % (noteDate,note)
        self.cur.execute(sql)
        self.conn.commit()
        return 0

    def getNote(self):
        sql="SELECT * FROM notebook"
        self.cur.execute(sql)
        results=self.cur.fetchall()
        data=[]
        for result in results:
            info={}
            info['noteDate']=result[0]
            info['note']=result[1]
            data.append(info)
        jsonStr=json.dumps(data)
        return jsonStr

    def setAnni(self,anniDate,anni):
        sql = "INSERT INTO anniversary (anniDate,anni) VALUES (\'%s\', \'%s\')" % (anniDate,anni)
        self.cur.execute(sql)
        self.conn.commit()
        return 0

    def getAnniData(self):
        sql="SELECT * FROM anniversary"
        self.cur.execute(sql)
        results=self.cur.fetchall()
        data=[]
        for result in results:
            info={}
            info['anniDate']=result[0]
            info['anni']=result[1]
            data.append(info)
        jsonStr = json.dumps(data)
        return jsonStr

    def judgeAnni(self,date):
        sql="SELECT * FROM anniversary WHERE anniDate=\'" + date + "\'"
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if len(results) == 0:
            return 0
        else:
            return ()

    def coverAnni(self,date,anni):
        sql="UPDATE anniversary SET anni=\'%s\' WHERE anniDate=\'%s\'"%(anni,date)
        self.cur.execute(sql)
        self.conn.commit()
        return 0

    def deleteNote(self,note):
        sql = "DELETE FROM notebook WHERE note=\'%s\'" % (note)
        self.cur.execute(sql)
        self.conn.commit()
        return 0