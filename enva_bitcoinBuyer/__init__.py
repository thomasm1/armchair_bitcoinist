from flask import Flask, flash, jsonify, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coins.db'
db = SQLAlchemy(app)
members = []
coins = [{'currency': 'Bitcoin'},{'currency': 'Ethereum'},{'currency': 'Litecoin'}]


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repre__(self):
        return '<Task %r>' % self.id

 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Tracker(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Oops.. there is an issue adding your coin'
    else:
        tasks = Tracker.query.order_by(Tracker.date_created).all()
        return render_template("home.jinja2", tasks=tasks)


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template("dashboard.jinja2")

@app.route('/currencies', methods=['GET'])
def returnAll():
    return jsonify({'coins': coins})

@app.route('/currencies/<string:currency>', methods=['GET'])
def returnOne(currency):
    findcoins = [coin for coin in coins if coin['currency'] == coin]
    return jsonify({'coin': findcoins[0]})


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

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Tracker.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Oops, there has been a problem deleting that ...'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Tracker.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
    
        try: 
            db.session.commit()
            return redirect('/')
        except:
            return 'Oops, there has been a problem posting that ...'

    else: 
        return render_template('update.html', task=task)


@app.route('/messages')
def messages():
    return render_template("messages.jinja2")

 
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
    else:
        members.append(f"{name} with gender {gender}")
        return redirect("/registrants")
 
if __name__ == '__main__':
   # app.secret_key = 'xxxxxxx'  # ../xx/www/.nogit
    app.run(debug=True)
