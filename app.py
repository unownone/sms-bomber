from main import bomber
from flask import Flask,render_template,redirect,url_for,request
from config import Config
from flask_pymongo import PyMongo
from threading import Thread


app = Flask(__name__)

app.config.from_object(Config)

mongo = PyMongo(app)

blocked = mongo.db.restricted

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        data=request.args.to_dict()
        if 'res' not in data:
            data['res']=None
        if data['res']==None:
            visib='hidden'
            res=''
        else:
            visib=''
            res=data['res']
        return render_template('index.html',visib=visib,res=res)
    elif request.method=='POST':
        data = request.form.to_dict()
        if 'stop_bomb' in data:
            if 'number' not in data:
                return url_for('/',res='NUMBER NOT PROVIDED')
            else:
                blocked.insert_one({'number':data['number']})
                return url_for('/',res='NUMBER WILL NOT BE BOMBED FROM NOW ON')
        else:
            if 'number' not in data:
                return url_for('/',res='NUMBER NOT PROVIDED')
            if 'freq' not in data:
                return url_for('/',res='PLEASE SELECT THE NUMBER OF MESSAGES TO SEND')
            if 'interval' not in data:
                data['interval']=5
            else:
                block = blocked.find_one({"number":data["number"]})
            if block is None:
                Thread(target=bomber(data['number'],data['freq'],data['interval']),args=(data['number'],int(data['freq']),int(data['interval'],)))
                return url_for('/',res='BOMBING STARTED SUCCESSFULLY')
            else:
                return url_for('/',res='NUMBER CANNOT BE BOMBED')   
            

if __name__=='__main__':
    app.run(debug=False)