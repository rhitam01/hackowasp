from pymongo import MongoClient
from urllib.parse import quote
import random
import certifi

client=MongoClient('mongodb+srv://rhitamdutta1:'+quote('Fly@2102')+'@cluster1.zv9orap.mongodb.net/?retryWrites=true&w=majority', tlsCAFile = certifi.where())
db = client.pratigya
consumption=db['consumption']
userdata=db['userdata']

_id=1

for i in range(100):
    _id+=1
    nn=["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Isabelle", "Jack","Rhitam","Pariansh","Adrija","RAghav","Neharika","Suhani","Priyanka","Aman","Jagrit","rohan","Kabir","Mona","Gaurvi","jiya"]
    name=random.choice(nn)
    current_consumption= random.randint(50,150)
    set_consumption= random.randint(100,200)
    fan=random.randint(10,100)
    light=random.randint(10,50)
    ac=random.randint(40,80)
    bill=(current_consumption*10)
    monthly_aim=random.randint(2500,3500)
    stylelife=['extravagant','moderate','minimalist']
    lifestyle=random.choice(stylelife)
    pp=['basic','standard','premium']
    plan=random.choice(pp)
    userdata.insert_one({'_id':_id,'name':name,'lifestyle':lifestyle,'plan':plan})
    consumption.insert_one({'_id':_id,'name':name,'plan':plan,'current_consumption':current_consumption,'set_consumption':set_consumption,'fan':fan,'light':light,'bill':bill,'monthly_aim':monthly_aim})
