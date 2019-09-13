@login_manager.user_loader
def user_loader(user_id):

    return User.query.get(user_id)