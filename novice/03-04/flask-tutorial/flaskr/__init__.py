import os

from flask import Flask

def create_app(test_config=None):
    #membuat dan mengatur app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        #load the instance config, jika ada, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load the test config jika passed in
        app.config.from_mapping(test_config)

    #meyakinkan lagi bahwa folder objek benar benar ada
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #contoh halaman web dengan kata hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

    def create_app():
        app = ...

        from . import db
        db.init_app(app)

        return app

def create_app():
    app = ...

    from . import auth
    app.register_blueprint(auth.bp)

    return app