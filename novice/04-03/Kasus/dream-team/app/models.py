from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Employee(UserMixin, db.Model):

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = dbColumn(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    check_password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departmens.id'))
    role_id = db.Column(db.Integer, dbForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not readable attribute.')

    @password.setter
    def password(self, password):

    def verify_password(self, password):

        return check_password_hash(self.check_password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)

    @login_manager.user_loader
    def load_user(user_id):
        return Employee.query.get(int(user_id))


    class Department(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(dbString(60), unique=True)
        ddescription = db.Column(db.String(200))
        employees = db.relationship('Employee', backref='department', lazy='dynamic')

        def __repr__(self):
            return '<Department: {}'.format(self.name)

        
        class Role(db.Model):

            __tablename__ = 'roles'

            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(60), unique=True)
            description = db.Column(db.String(200))
            employees = db.relationship('Employee', backref='role', lazy='dynamic')


            def __repr__(self):
                return '<Role: {}>'.format(self.name)