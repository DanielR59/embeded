import jwt
import datetime
import uuid
import json

with open('keys.json','r') as f:
	keys = json.load(f)



token = jwt.encode(
	{
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
		"jti": str(uuid.uuid4()),
		"aud": "tableau",
		"sub": keys['sub'],
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

print(token)
