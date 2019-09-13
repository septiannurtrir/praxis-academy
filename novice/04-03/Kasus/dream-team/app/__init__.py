from flask_login import LoginManager

# after the db variable initialization
login_manager = LoginManager()


def create_app(config_name):
    # existing code remains

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    return app