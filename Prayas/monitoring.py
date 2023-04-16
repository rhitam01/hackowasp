from weather import data
from flask import Flask, url_for, render_template, request, redirect, session
from pymongo import MongoClient
from urllib.parse import quote
import certifi

client=MongoClient('mongodb+srv://rhitamdutta1:'+quote('Fly@2102')+'@cluster1.zv9orap.mongodb.net/?retryWrites=true&w=majority', tlsCAFile = certifi.where())
db = client.pratigya
userdata = db['userdata']
consumption=db['consumption']

name = session.get('name')
password = session.get('password')
var=userdata.find_one({'_id':int(password),'name':name})
var1=consumption.find_one({'_id':int(password),'name':name})



temp = data['main']['temp']
humidity= data['main']['humidity']
