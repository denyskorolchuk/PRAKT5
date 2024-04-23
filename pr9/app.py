import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        obj = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                obj[key] = value

        return obj

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    storinok = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        obj = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                obj[key] = value

        return obj

    def __repr__(self):
        return f"User('{self.name}', '{self.storinok}')"


class UserResource(Resource):
    def get(self, user_id):
        # Логіка отримання користувача за ідентифікатором user_id
        current_user = User.query.filter_by(id=user_id).first()
        # return {
        #     "id": current_user.id,
        #     "email": current_user.email,
        #     "username": current_user.username
        # }
        return current_user.serialize()

class BookResource(Resource):
    def get(self, book_id):
        # Логіка отримання користувача за ідентифікатором user_id
        current_user = Book.query.filter_by(id=book_id).first()
        # return {
        #     "id": current_user.id,
        #     "email": current_user.email,
        #     "username": current_user.username
        # }
        return current_user.serialize()

api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(BookResource, '/book/<int:book_id>')


if __name__ == "__main__":
    app.run(debug=True)
