from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
# from views import views

# Flask Obj Creation
app = Flask(__name__)

# This project does not need Blueprint
# app.register_blueprint(views, url_prefix="/")

# Database connection thru 

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
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
    response = requests.get(url)
    rawData = response.json()
    data = list(map(lambda x: {
        'Name': x['name'],
        'Price': x['current_price'],
        '24High': x['high_24h'],
        '24Low': x['low_24h'],
        'MC': str(int(x['market_cap']) // 1_000_000) + 'M',
    }, rawData))
    print(data)
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