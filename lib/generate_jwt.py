import jwt
import datetime
import uuid
from dotenv import load_dotenv
import os

client_id = os.getenv("CLIENT_ID")
secret_id = os.getenv("SECRET_ID")
secret_value = os.getenv("SECRET_VALUE")


def encode_user_data_to_jwt(data_user : str) -> str:
    return jwt.encode(
	{
		'iss': client_id,
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
		"jti": data_user[0],
		"aud": "tableau",
		"sub": data_user[-1],
		"scp": ["tableau:views:embed"]
	},
	 	secret_value,
		algorithm = "HS256",
		headers = {
		'kid': secret_id,
		'iss': client_id,
		'alg': 'HS256'
        }
  )

