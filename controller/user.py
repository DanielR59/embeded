from model.handle_db import HandleDB
from werkzeug.security import generate_password_hash
import uuid

class User():
    data_user = {}

    def __init__(self, data_user) -> None:
        self.db = HandleDB()
        self.data_user = data_user

    def create_user(self):
        self._add_id()
        self._password_hash()
        self._create_username()
        self.db.insert_user(self.data_user)

    def _add_id(self):
        # user = self.db.get_all()
        # one_user = user[-1]
        # id_user = one_user[0]
        self.data_user["id"] = str(uuid.uuid4())


    def _password_hash(self):
        self.data_user["passworduser"] = generate_password_hash(self.data_user["passworduser"], 'pbkdf2:sha256:30',30)

    def _create_username(self):
        self.data_user["username"] = str(self.data_user["firstname"] +"."+ self.data_user["lastname"]).lower()


if __name__ == "__main__":
    data = {
        "firstname": "Juanito",
        "lastname": "Banana",
        "passworduser": "123456",
        "email": "hola@hola.com"
    }
    user = User(data)
    user.create_user()