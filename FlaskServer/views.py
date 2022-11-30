from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    # handle get request
    # args = request.args
    # name = args.get('name')

    return render_template("index.html", name='Denny')


@views.route("/jinja")
def jinja():
    return render_template("testJinja.html")

@views.route("/table")
def table():
    return render_template("table.html")

# Redirect with 'redirect' and 'url_for'
# @views.route("/return_home")
# def return_home():
#     return redirect(url_for("views.home"))

# Return JSON
# @views.route("/json")
# def get_json():
#     return jsonify({
#         'name': 'time',
#         'age': '28'
#     })

# Dynamic URL
# @views.route("/profile/<username>") 