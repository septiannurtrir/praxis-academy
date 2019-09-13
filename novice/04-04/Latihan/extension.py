from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = dbColumn(db.Boolean, default=False)

    def is_active(self):
        return True

    def get_id(self):
        return self.authenticated

    def is_anonymous(self):
        return False