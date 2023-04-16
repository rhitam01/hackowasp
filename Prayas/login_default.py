from flask import Flask, url_for, render_template, request, redirect, session
from pymongo import MongoClient
from urllib.parse import quote
import certifi

client=MongoClient('mongodb+srv://rhitamdutta1:'+quote('Fly@2102')+'@cluster1.zv9orap.mongodb.net/?retryWrites=true&w=majority', tlsCAFile = certifi.where())
db = client.pratigya
userdata = db['userdata']
consumption=db['consumption']

app=Flask(__name__)
app.secret_key = 'hello'

@app.route("/subcription")
def subs():
    return render_template("subs.html")

@app.route("/buying")
def buying():

    return render_template("buying.html")

@app.route("/dashboard")
def dash():
    name = session.get('name')
    password = session.get('password')
    user = consumption.find_one({'_id': int(password), 'name': name})
    d2=user['current_consumption']
    data=d2-user['set_consumption']
    fan=user['fan']
    light=user['light']
    ac=d2-(fan+light)
    return render_template("dash.html",ussr=name, rhtm=d2, pncham=data, fa=fan,ligh=light, aa=ac)

@app.route("/contact")
def contact():
    return render_template("contactus.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email=request.form['email']
        password1 = request.form['password']
        password = request.form['password']
        if password1==password:
            userdata.insert_one({'_id': int(password), 'name': name})
            consumption.insert_one({'_id':int(password),'name':name,'plan':"",'current_consumption':0,'set_consumption':0,'fan':0,'light':0,'bill':0,'monthly_aim':0})
            
            
            session['name']=name
            session['password']=password
            return redirect(url_for("login"))
        else:
            return redirect("/")
    return render_template("signupp.html")

@app.route("/")
def homepage():
    return render_template("homepagee.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = userdata.find_one({'_id': int(password), 'name': name})
        print(user)
        if user:
            session['name']=name
            session['password']=password
            return redirect(url_for("dash"))
        else:
            return redirect("/login")
    return render_template("logiinn.html")

if __name__=="__main__":
    app.run(debug=True)