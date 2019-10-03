from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(100))
    export = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)

    coinInquires_asked = db.relationship('CoinInquire', 
        foreign_keys='CoinInquire.asked_by_id', 
        backref='asker', 
        lazy=True
    )

    respas_requested = db.relationship('CoinInquire',
        foreign_keys='CoinInquire.expert_id',
        backref='expert',
        lazy=True
    )

class CoinInquire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coinInquire = db.Column(db.Text)
    respa = db.Column(db.Text)
    asked_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    expert_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    