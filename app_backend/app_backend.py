from flask import Flask
from flask import request
from flask_cors  import *
from sqlconnect import sqlconnect

app = Flask(__name__)
CORS(app, supports_credentials=True)
sqlCon=sqlconnect()

@app.route('/anniversary',methods=['POST'])
def anniversary():
    if request.method == 'POST' and request.form.get('anniDate') and request.form.get('anni'):
        data=request.form.to_dict()
        anniDate=data.get("anniDate")
        anni=data.get("anni")
        judge=sqlCon.judgeAnni(anniDate)
        if judge==0:
            result = sqlCon.setAnni(anniDate, anni)
            if result==0:
                return "200"
            else:
                return "emm"
        else:
            res = sqlCon.coverAnni(anniDate, anni)
            if res==0:
                return "200"
            else:
                return "emmm"
    else:
        return "emmm"

@app.route('/getAnni',methods=['GET'])
def getAnni():
    if request.method =='GET':
        result=sqlCon.getAnniData()
        return result

@app.route('/setNotebook',methods=['POST'])
def setNotebook():
    if request.method == 'POST' and request.form.get('noteDate') and request.form.get('note'):
        data=request.form.to_dict()
        noteDate=data.get("noteDate")
        note=data.get("note")
        result=sqlCon.setNote(noteDate,note)
        if result==0:
            return "200"
        else:
            return "emmm"

@app.route('/getNotebook',methods=['GET'])
def getNotebook():
    if request.method=='GET':
        result=sqlCon.getNote()
        return result

@app.route('/deleteNote',methods=['POST'])
def deleteNote():
    if request.method=='POST' and request.form.get('note'):
        data = request.form.to_dict()
        note = data.get("note")
        result=sqlCon.deleteNote(note)
        if result==0:
            return "200"
        else:
            return "emmmm"

if __name__ == '__main__':
    app.run(debug=True,port=4000,use_reloader=False)
