from flask import Flask, flash, jsonify, request, render_template, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
from .commands import create_tables
from .extensions import db, login_manager

def create_app(config_file='settings.py'): # db data separate;  serving from currency_server.py
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main)

    app.cli.add_command(create_tables)

    return app

    # app.config.from_pyfile(config_file)

    # return app 

# class Tracker(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repre__(self):
#         return '<Task %r>' % self.id



## RETURN HERE --- UNACCOUNTED!!! >>>
# if __name__ == '__main__':
#    # app.secret_key = 'xxxxxxx'  # ../xx/www/.nogit
#     app.run(debug=True)
