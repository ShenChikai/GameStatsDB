from flask import Flask, render_template, request, jsonify, redirect, url_for
# from views import views

# Flask Obj Creation
app = Flask(__name__)

# This project does not need Blueprint
# app.register_blueprint(views, url_prefix="/")

@app.route("/")
def home():
    return render_template("home.html", name='Denny')

@app.route("/<name>")
def test(name):
    return render_template("home.html", name=name)

@app.route("/table1", methods=["GET","POST"])
def table1():
    # handle get request
    if request.method == "POST":
        args = request.form
        print(args['Genre'])
        return redirect(url_for("test", name=args))
    else:
        return render_template("table1.html")

@app.route("/table2")
def table2():
    return render_template("table2.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Main
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

# Test Main
# if __name__ == '__main__':
#     app.run(debug=True, port=8000)