import jwt,datetime
import os

client_id=os.environ.get('API_USER') #client_id
client_secret=os.environ.get('API_PASSWORD') #client_secret


class GenerateApiToken:

	def __init__(self):
		self.client_id = client_id
		self.client_secret = client_secret
		print (client_secret)

	def generate_token(self,client_id,client_secret):	

		if self.client_id==client_id and self.client_secret==client_secret:

			payload = {
					'id': self.client_id, #client_id
					'secret': self.client_secret, #client_secret
					# expire time of the jwt tokens (datetime.timedelta(days=5) expires in 5 days)
					'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5), 
				}
			# encoding the JWT Token 
			jwt_token = {'Access_token': jwt.encode(payload, "SECRET",algorithm='HS256'),'success':True}
			return jwt_token
		else:
			return {'success':False}

class ValidateApiToken:

	def __init__(self,headers):

		self.client_id = client_id #client_id
		self.client_secret = client_secret #client_secret
		self.headers=headers

	def verify_token(self):

		try:
			# decoding the JWT Token
			decoded_token=jwt.decode(self.headers, 'SECRET', algorithms=['HS256'])
			# To verify data encode in GenerateApiToken == data encode in ValidateApiToken
			print(decoded_token)
			if decoded_token['id']==self.client_id and decoded_token['secret']==self.client_secret:
				return {'success':True ,'Access':'Access Granted'}
			else:
				return {'success':False ,'Access':'Access denied due invalid credentials'}
		except jwt.ExpiredSignatureError:
			return {'success':False ,'Access':'Access Expired or token Expired'}
