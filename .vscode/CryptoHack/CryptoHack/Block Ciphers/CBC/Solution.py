import json
import requests

url='http://aes.cryptohack.org/ecbcbcwtf/'

def enc_flag():
    r = requests.get(url+'encrypt_flag/')
    return json.loads(r.text)["ciphertext"]

def dec_ecb():
    c=enc_flag().decode('hex')
    iv=c[:16] 
    c1_c2=c[16:].encode('hex')
    r = requests.get(url+'decrypt/{}/'.format(c1_c2))
    ecb_c1_c2=json.loads(r.text)["plaintext"].decode('hex')
    flag=''
    ecb_c1=ecb_c1_c2[:16]
    ecb_c2=ecb_c1_c2[16:]
    cbc_c1=c[16:32]
    for i,j in zip(ecb_c1,iv):
        flag+=chr(ord(i)^ord(j)) 
    for i,j in zip(ecb_c2,cbc_c1):
        flag+=chr(ord(i)^ord(j)) 
    print (flag)

dec_ecb()