import jwt
encoded = jwt.encode({'username':'MuhammadAwan','admin':'true'},'secret',algorithm='HS256')
print (encoded)
