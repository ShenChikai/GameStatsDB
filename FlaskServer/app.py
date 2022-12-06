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
load_dotenv()
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

@app.route("/table1", methods=["GET","POST"])
def table1():
    # handle get request
    if request.method == "POST":
        args = request.form
        print(args['Genre'])
        return redirect(url_for("test", name=args))
    else:
        # Empty
        return render_template("table1.html", data = [])

@app.route("/table2")
def table2():
    # testing
    data = []
    cursor.execute( "SELECT * FROM Rawscores")
    for item in cursor:
        data.append(item)
    return render_template("table2.html", data = data)



@app.route("/about")
def about():
    return render_template("about.html")

# Main
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port="5000")

# Test Main
if __name__ == '__main__':
    app.run(debug=True, port=8000)