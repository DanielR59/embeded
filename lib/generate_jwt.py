import jwt
import datetime
import uuid
from .utils import load_keys


keys = load_keys('keys.json')

def encode_user_data_to_jwt(data_user : str) -> str:
    print(data_user)

    return jwt.encode(
	{
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
		"jti": data_user[0],
		"aud": "tableau",
		"sub": data_user[-1],
		"scp": ["tableau:views:embed"]
	},
		keys['token'],
		algorithm = "HS256",
		headers = {
		'kid': keys['kid'],
		'iss': keys['iss'],
		'alg': 'HS256'
        }
  )

