from getpass import getpass
import sys

from flask import current_app
from bull import app, bcrypt
from bull.models import User, db

def main():

    with app.app_contect():
        db.metadata.create_all(db.engine)
        if User.query.all():
            print 'A user already exist! Create another? (y/n):',
            create = raw_input()
            if create == 'n':
                return

        print 'Enter email address: ',
        email = raw_input()
        password = getpass()
        assert password == getpass('Password (again):')

        user = User(
            email=email,
            password=bcrypt.generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print 'User added.'

if __name__ == '__main__':
    sys.exit(main())