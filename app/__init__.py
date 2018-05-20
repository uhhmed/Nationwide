from flask import Flask, session, g, render_template


app = Flask(__name__)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.views import general
from app.views import users

app.register_blueprint(general.mod)
app.register_blueprint(users.mod)

# from app import utils
from app.database import User, mongo