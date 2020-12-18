import jwt
key=open("pubkey.pem").read()
def create_session():
    encoded = jwt.encode({'username': "admin", 'admin': True}, key, algorithm='HS256')
    return {"session": encoded.decode()}
print(create_session())