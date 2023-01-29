import psycopg2
import uuid
DB_NAME = "tableau-embeded"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "localhost"
DB_PORT = "6666"

class HandleDB():
    def __init__(self) -> None:
        self._conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
        self._cursor = self._conn.cursor()

    def get_all(self) -> list:
        self._cursor.execute("SELECT * FROM metadata.users")
        return self._cursor.fetchall()

    def get_user(self, email : str) -> list:
        self._cursor.execute(f"SELECT * FROM metadata.users WHERE email = '{email}'")
        return self._cursor.fetchall()

    def insert_user(self, data_user : dict) -> None:
        self._cursor.execute(f"INSERT INTO metadata.users (id,firstname,lastname,username,passworduser,email) VALUES ('{uuid.uuid4()}', '{data_user['firstname']}', '{data_user['lastname']}', '{data_user['username']}', '{data_user['passworduser']}', '{data_user['email']}')")
        self._conn.commit()

    def __del__(self) -> None:
        self._conn.close()


if __name__ == "__main__":

    db = HandleDB()
    data = {
        "id": "1",
        "firstname": "Jose",
        "lastname": "Rosas",
        "passworduser": "123456",
        "email": "hola@vikingoinformatico.com"
    }

    data['username'] = str(data['firstname'] + (data['lastname'])).lower()

    db.insert_user(data)
    print(db.get_all())