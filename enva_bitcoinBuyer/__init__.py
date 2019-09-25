from flask import flash

from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coins.db'
db = SQLAlchemy(app)
members = []


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repre__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
            return 'testing db!'
        else: 
            return render_template("home.jinja2")
    # return "Console"


@app.route('/home', methods=['GET', 'POST'])
def home():
        if request.method == 'POST':
            return 'testing db!'
        else: 
                # btc = float(request.form['btc'])
                # profit = float(request.form['profit'])

        #         print(btc)
        #         print(profit)

        #         a = float(profit) / 100
        #         print(a)

        #         b = 1.005012531 * float(btc)
        #         print(float(b))

        #         s = float(1 + a) * float(b)
        #         print("%.16f" % s)

        #         flash('BTC. ' + "%.16f" % s, 'success')
            return render_template("home.jinja2")
    # "ArmChair Bitcoinist"


@app.route('/home/console')
def console():  
    return render_template("console.jinja2")


@app.route('/home/messages')
def messages():
    return render_template("messages.jinja2")


@app.route('/home/<input>')
def input(input):
    return "Input: {} <br /><br /><a href='/home'>back</a>".format(input)


@app.route('/home/<input>/<message>')
def home_input_message(input, message):
    return render_template("home_input_message.jinja2",
                           input=input,
                           message=message)
    # return "{0}, {1}".format(name, message)


@app.route('/register')
def register():
    return render_template("register.jinja2")


@app.route('/registrants')
def registrants():
    return render_template("registered.html", members=members)


@app.route('/registerPost')  # , methods=["POST"])
def registerPost():
    members = []
    name = request.args.get("name")
    gender = request.args.get("gender")
    if not name or not gender:
        return render_template("failure.jinja2")
    members.append(f"{name} with gender {gender}")
    return redirect("/registrants")

# URL: http://localhost:5000/query?a=test&b=123
@app.route('/query')
def query():
    a = request.args.get('a')
    b = request.args.get('b')
    return "<h4>Variable a = {0}<br />while Variable b = {1}</h4><a href='/home'>back</a>".format(a, b)
 

if __name__ == '__main__':
    app.secret_key = 'xxxxxxx' # ../xx/www/.nogit
    app.run(debug=True)
