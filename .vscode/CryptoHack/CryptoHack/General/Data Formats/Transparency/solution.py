"""

python3

"""

import requests, json, pprint
target = "cryptohack.org"
data = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))
data = json.loads(data.text)

# for d in data:
# 	print(d['common_name'])

print(requests.get("https://thetransparencyflagishere.cryptohack.org").text)

'crypto{thx_redpwn_for_inspiration}'