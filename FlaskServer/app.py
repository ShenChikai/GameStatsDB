from flask import Flask, render_template, request, jsonify, redirect, url_for
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

@app.route("/")
def home():
    return render_template("home.html", name='Denny')

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
    cursor.execute( "CALL GenreShare()")
    for item in cursor:
        labels["GenreShare"].append(item[0])
        data["GenreShare"].append(item[2])
    # Get PlatformShare
    cursor.execute( "CALL PlatformShare()")
    for item in cursor:
        labels["PlatformShare"].append(item[0])
        data["PlatformShare"].append(item[2])
    # Get OSShare
    cursor.execute( "CALL OSShare()")
    for item in cursor:
        labels["OSShare"].append(item[0])
        data["OSShare"].append(item[2])
    # Get CompanyMCShare
    cursor.execute( "CALL CompanyMCShare()")
    for item in cursor:
        labels["CompanyMCShare"].append(item[0])
        data["CompanyMCShare"].append(item[2])
    return render_template("marketShare.html", labels = labels, data = data)



@app.route("/about")
def about():
    return render_template("about.html")

# Main
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

# Test Main
# if __name__ == '__main__':
#     app.run(debug=True, port=8000)