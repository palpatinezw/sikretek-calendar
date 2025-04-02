from flask import Flask, request
import datetime
import json
from dategen import Sikretekdate

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Sikretek Calendar API - This message means that the API is running!"

@app.route("/sikretek_date")
def getSikretekDate():
    anchordatetime = datetime.date(2021, 6, 25) # 25 June 2021 - ANCHOR DATE - 1st Moon of Light of 0 years After Revelation
    anchorsikretekdate = Sikretekdate(0, 1, 0, anchordatetime)

    try:
        dateParam = request.args.get("date")
        if dateParam == None: targetdate = datetime.date.today()
        else: targetdate = datetime.date.fromisoformat(dateParam)
    except:
        print("[sikretek_date] Invalid 'date' parameter")
        return {"success":False, "error": "Invalid 'date' parameter"}
    
    anchorsikretekdate.gotoDate(targetdate)
    
    return {"success":True, "data":anchorsikretekdate.getStrObj()}

@app.route("/sikretek_range")
def getSikreteRange():
    anchordatetime = datetime.date(2021, 6, 25) # 25 June 2021 - ANCHOR DATE - 1st Moon of Light of 0 years After Revelation
    anchorsikretekdate = Sikretekdate(0, 1, 0, anchordatetime)

    try:
        startParam = request.args.get("start")
        if startParam == None: startdate = datetime.date.today()
        else: startdate = datetime.date.fromisoformat(startParam)
    except:
        print("[sikretek_range] Invalid 'start' parameter")
        return {"success":False, "error": "Invalid 'start' parameter"}
    try:
        endParam = request.args.get("end")
        if endParam == None: enddate = datetime.date.today()
        else: enddate = datetime.date.fromisoformat(endParam)
    except:
        print("[sikretek_range] Invalid 'end' parameter")
        return {"success":False, "error": "Invalid 'end' parameter"}
    
    if startParam > endParam:
        return {"success":False, "error": "Start date must be before end date"}
    
    res = []

    anchorsikretekdate.gotoDate(startdate)
    res.append(anchorsikretekdate.getStrObj())
    while (anchorsikretekdate.gregoriandate != enddate):
        anchorsikretekdate.advanceDate()
        res.append(anchorsikretekdate.getStrObj())
    
    return {"success":True, "data":res}