from flask import Flask,render_template,url_for,request,redirect
from config import Config
from flask_pymongo import PyMongo
from threading import Thread

visited=0
unique = 0
app = Flask(__name__)

app.config.from_object(Config)

mongo = PyMongo(app)

blocked = mongo.db.restricted
logging = mongo.db.logging

@app.route('/',methods=['GET','POST'])
def home(self):
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
        return render_template('index.html',visib=visib,res=res,visits=self.visited,uniq=self.unique)
    elif request.method=='POST':
        data = request.form.to_dict()
        if 'stop_bomb' in data:
            if 'number' not in data:
                return redirect(url_for('home',res='NUMBER NOT PROVIDED',visits=self.visited,uniq=self.unique))
            else:
                blocked.insert_one({'number':data['number']})
                return redirect(url_for('home',res='NUMBER WILL NOT BE BOMBED FROM NOW ON',visits=self.visited,uniq=self.unique))
        else:
            if data['number']=="":
                return redirect(url_for('home',res='NUMBER NOT PROVIDED',visits=self.visited,uniq=self.unique))
            if data['freq']=="":
                return redirect(url_for('home',res='PLEASE SELECT THE NUMBER OF MESSAGES TO SEND',visits=self.visited,uniq=self.unique))
            if 'interval'=="":
                data['interval']=5
            else:
                block = blocked.find_one({"number":data["number"]})
            if block is None:
                from main import bomber
                thread = Thread(target=bomber,args=(data['number'],int(data['freq']),int(data['interval'])))
                thread.start()
                datea = request.headers['X-Forwarded-For']
                logg = logging.find_one_and_update({"info":"total views"},{{"$inc":{"total_views":1}},{"$push": {"ips":datea}}})
                datea = logging.find_one({"info":"total views"})
                self.visited = datea["total_views"]
                self.unique = len(datea["ips"])
                return redirect(url_for('home',res='BOMBING STARTED SUCCESSFULLY',visits=self.visited,uniq=self.unique))
            else:
                return redirect(url_for('home',res='NUMBER CANNOT BE BOMBED',visits=self.visited,uniq=self.unique))
            

if __name__=='__main__':
    visits = logging.find_one({"info":"total views"})
    visited = visits["total_views"]
    unique = len(visits["ips"])
    app.run(debug=False)