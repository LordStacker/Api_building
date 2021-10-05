from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Post
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db.init_app(app)
Migrate(app, db)


@app.route("/user", methods=["GET"])
def user():
    user = User.query.get(1)
    return jsonify(user.serialize()),200

if __name__ == "__main__":
    app.run(host='localhost', port=8080)