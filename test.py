from controller.user import User



data = {
    "firstname": "Jorge",
    "lastname": "De la Madrid",
    "passworduser": "123456",
    "email": "holapelade@hola.com"
}
user = User(data)
user.create_user()