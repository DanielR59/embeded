from model.handle_db import HandleDB
from werkzeug.security import check_password_hash

def check_user(username, password):
    db = HandleDB()
    user = db.get_user(username)
    if not user:
        return None
    user = user[0]
    password_hash = user[4]
    if check_password_hash(password_hash, password):
        return user