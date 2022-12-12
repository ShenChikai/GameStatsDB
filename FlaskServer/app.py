from flask import Flask, render_template, request, jsonify, redirect, url_for
import time
import datetime
import requests
import os
from dotenv import load_dotenv
# from views import views

# Customized Import
from dbConn import connectToDB
from chatGPT2SQL import User2SQL

# Flask Obj Creation
app = Flask(__name__)

# This project does not need Blueprint
# app.register_blueprint(views, url_prefix="/")

# Database connection thru MariaDB
# Load environment variables from the .env file
dotenv_path = os.path.abspath('.env') #travels up a level to find the .env
load_dotenv(dotenv_path)
dbconfig = {
    'dbhost' : os.environ["DBHOST"],
    'dbuser' : os.environ["DBUSER"],
    'dbpass' : os.environ["DBPASS"],
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
        # Init Page
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
        # Get Options
        gameOpt, genreOpt, platformOpt, AwardOpt = getAllOptions(cursor)
        
        # Execute the Table Query
        header, table = tableProc(args['GameName'],
                                    args['Genre'],
                                    args['Platform'],
                                    args['Award'],
                                    args['Sales']
                                )
        
        # Debug Script
        # print('############################################################')
        # print(f'Statment: {cursor.statement}')
        # print(f"args: {args['GameName']}, {args['Genre']}, {args['Platform']}, {args['OS']}, {args['Sales']}")
        print(f'Num row returned: {cursor.rowcount}')
        # print(f'Description: {cursor.description}')

        return render_template("interactiveTable.html", 
                                    GameList=gameOpt, 
                                    GenreList=genreOpt, 
                                    PlatformList=platformOpt, 
                                    AwardList=AwardOpt,
                                    header = header,
                                    table = table
                                )
    else:
        # Init Page
        # Get Options
        gameOpt, genreOpt, platformOpt, AwardOpt = getAllOptions(cursor)
        
        # Init start with '','','PC','Microsoft Windows','True'
        # Execute the Table Query
        header, table = tableProc('', '', '', 'Game of the Year', 'True')

        # Debug Script
        # print('############################################################')
        # print(f'Statment: {cursor.statement}')
        # print(f"args: {args['GameName']}, {args['Genre']}, {args['Platform']}, {args['OS']}, {args['Sales']}")
        print(f'Num row returned: {cursor.rowcount}')
        # print(f'Description: {cursor.description}')

        return render_template("interactiveTable.html", 
                                    GameList=gameOpt, 
                                    GenreList=genreOpt, 
                                    PlatformList=platformOpt, 
                                    AwardList=AwardOpt,
                                    header = header,
                                    table = table
                                )

# Get All Options
def getAllOptions(cursor):
    gameOpt, genreOpt, platformOpt, AwardOpt = [], [], [], []
    cursor.callproc( "GetAllTableOptions" )
    # Games
    for item in cursor:
        gameOpt.append(item[0])
    # Genre
    cursor.nextset()
    for item in cursor:
        genreOpt.append(item[0])
    # Platform
    cursor.nextset()
    for item in cursor:
        platformOpt.append(item[0])
    # Award
    cursor.nextset()
    for item in cursor:
        AwardOpt.append(item[0])
    return gameOpt, genreOpt, platformOpt, AwardOpt

# Retrieve Data for Table Proc Call
def tableProc(GameName, Genre, Platform, Award, SalesOpt):
    cursor.callproc("InteractiveTableSearch", (
                        GameName, Genre, Platform, Award, SalesOpt
                    ))
        
    header = []
    for column in cursor.description:
        header.append(column[0])
    
    table = []
    for item in cursor:
        if item[9] == 1:
            won = 'Yes'
        else:
            if not item[7]:
                won = 'N\A'
            else:
                won = 'No'

        table.append([
            item[0],
            '&#128178;' + str(round(item[1],3)) + 'M',
            item[2].strftime("%Y/%m/%d"),
            item[3] if item[3] else 'N\A',
            item[4] if item[4] else 'N\A',
            '&#128178;' + str(item[5] // 1_000_000)[:-2] + 'M' if item[5] else 'N\A',
            item[6] if item[6] else 'N\A',
            'N\A' if not item[7] else item[7],
            'N\A' if not item[8] else item[8],
            won
        ])
    
    return header, table

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
# Text-to-SQL ChatGPT Page
@app.route("/textSearch", methods=["GET","POST"])
def textSearch():
    # handle get request
    if request.method == "POST":
        args = request.form
        print(args['EnglishText'])
        # Call ChatGPT
        # Try to establish connection with ChatGPT
        errorMsg = ""
        requestPass = False
        tStart = time.time()
        try:
            newChat = User2SQL()
            newChat.get_user_input(args['EnglishText'])
            SQL_Statement = newChat.get_response()
            print(SQL_Statement)
            requestPass = True
        except:
            errorMsg = "Sorry, ChatGPT is currently down. Please come back and try later."
        # Compute Time elapsed
        tEnd = time.time()
        tElapsed = round(tEnd-tStart)
        print(f'Took {tElapsed}s')
        # Query Database
        header, table = [], []
        if requestPass:
            try:
                cursor.execute(SQL_Statement)
                for column in cursor.description:
                    header.append(column[0])
                for item in cursor:
                    table.append(item)
            except:
                errorMsg = "Sorry, ChatGPT could not proper process your query at this time. Please try something else."
        
        return render_template("textSearch.html", header = header, table = table, errorMsg=errorMsg)
    else:
        # init page
        return render_template("textSearch.html", header = [], table = [], errorMsg = "")
############################################################################################
# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Main
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port="5000")

# Test Main
if __name__ == '__main__':
    app.run(debug=True, port=8000)