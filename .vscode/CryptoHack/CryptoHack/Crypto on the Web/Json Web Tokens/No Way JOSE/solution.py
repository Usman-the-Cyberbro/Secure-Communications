import jwt
encoded = jwt.encode({'username':'MuhammadAwan','admin':'true'},'',algorithm='none')
print (encoded)