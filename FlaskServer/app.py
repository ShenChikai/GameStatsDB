from flask import Flask
from views import views

# Flask Obj Creation
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

# Main
if __name__ == '__main__':
    app.run(debug=True, port=8000)