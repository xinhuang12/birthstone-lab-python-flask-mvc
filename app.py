# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=["GET", "POST"])
def results():
    print(request.form['gemstone'])
    user_choice=request.form['gemstone']
    gemstone={
        "January":"your birthstone is: Garnet",
        "Febuary":"your birthstone is: Anethyst",
        "March":"your birthstone is: Aquamarine",
        "April":"your birthstone is: Diamond",
        "May":"your birthstone is: Emerald",
        "June":"your birthstone is: Pearl",
        "July":"your birthstone is: Ruby",
        "August":"your birthstone is: Peridot",
        "September":"your birthstone is: Sapphire",
        "October":"your birthstone is: Opal",
        "November":"your birthstone is: Citrine",
        "December":"your birthstone is: Topaz"}
    try:
        message=gemstone[user_choice]

    except:
        message=("error, please try another month")
        
    return render_template("results.html", message=message)