from flask import Flask, render_template, request, jsonify, redirect, url_for
import time
import datetime
import requests
import os
from dotenv import load_dotenv
# from views import views

# Customized Import
from dbConn import connectToDB

# Flask Obj Creation
app = Flask(__name__)

# This project does not need Blueprint
# app.register_blueprint(views, url_prefix="/")

# Database connection thru MariaDB
# Load environment variables from the .env file
dotenv_path = os.path.abspath('.env') #travels up a level to find the .env
load_dotenv(dotenv_path)
dbconfig = {
    'dbhost' : os.environ["HOST"],
    'dbuser' : os.environ["USER"],
    'dbpass' : os.environ["PASS"],
    'dbname' : os.environ["DB"]
}
# Get Cursor
cursor = connectToDB(dbconfig)

############################################################################################
# Home Page (Stock)
@app.route("/", methods=["GET","POST"])
def home():
    # Get a list of companies from Database
    CompanyList = []
    cursor.execute( "CALL GetCompanyWithStock();")
    for item in cursor:
        CompanyList.append(item[0])
    # SQL Return format: Date, Ticker, Open, High, Low, Close, Adj_Close, Volume
    # Handle Request
    if request.method == "POST":
        args = request.form

        OHLC = []
        Volume = []
        cursor.execute("CALL GetStock(?, ?, ?);",
                        (args['CompanyName'],
                        args['startDate'],
                        args['endDate'])
                        )
        for item in cursor:
            unixTime = time.mktime(item[0].timetuple())
            unixTime = int(str(int(unixTime)) + '000')
            OHLC.append([unixTime, round(item[2], 2), round(item[3], 2), round(item[4], 2), round(item[5], 2)])
            Volume.append([unixTime, round(item[7], 2)])
            
        return render_template("home.html", CompanyList=CompanyList, CompanyName=args['CompanyName'], OHLC=OHLC, Volume=Volume)
    else:
        # Start Page
        OHLC = []
        Volume = []
        cursor.execute( "CALL GetStock('Microsoft', '2020-08-01', '2022-08-02');")
        for item in cursor:
            unixTime = time.mktime(item[0].timetuple())
            unixTime = int(str(int(unixTime)) + '000')
            OHLC.append([unixTime, round(item[2], 2), round(item[3], 2), round(item[4], 2), round(item[5], 2)])
            Volume.append([unixTime, round(item[7], 2)])
            
        return render_template("home.html", CompanyList=CompanyList, CompanyName="Microsoft", OHLC=OHLC, Volume=Volume)
    
############################################################################################
# Interactive Table Page
@app.route("/interactiveTable", methods=["GET","POST"])
def interactiveTable():
    # handle get request
    if request.method == "POST":
        args = request.form
        print(args['Genre'])
        return redirect(url_for("test", name=args))
    else:
        # Empty
        return render_template("interactiveTable.html", data = [])

############################################################################################
# Market Share Page
@app.route("/marketSahre")
def marketSahre():
    labels = {
        "GenreShare": [],
        "PlatformShare": [],
        "OSShare": [],
        "CompanyMCShare": []
    }
    data = {
        "GenreShare": [],
        "PlatformShare": [],
        "OSShare": [],
        "CompanyMCShare": []
    }
    # Get GenreShare
    cursor.execute( "CALL GenreShare();")
    for item in cursor:
        labels["GenreShare"].append(item[0])
        data["GenreShare"].append(item[2])
    # Get PlatformShare
    cursor.execute( "CALL PlatformShare();")
    for item in cursor:
        labels["PlatformShare"].append(item[0])
        data["PlatformShare"].append(item[2])
    # Get OSShare
    cursor.execute( "CALL OSShare();")
    for item in cursor:
        labels["OSShare"].append(item[0])
        data["OSShare"].append(item[2])
    # Get CompanyMCShare
    cursor.execute( "CALL CompanyMCShare();")
    for item in cursor:
        labels["CompanyMCShare"].append(item[0])
        data["CompanyMCShare"].append(item[2])
    return render_template("marketShare.html", labels = labels, data = data)


############################################################################################
# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Main
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

# Test Main
# if __name__ == '__main__':
#     app.run(debug=True, port=8000)