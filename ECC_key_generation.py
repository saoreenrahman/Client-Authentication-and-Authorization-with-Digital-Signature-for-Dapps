from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from pathlib import Path


# generating EC private key
key = ECC.generate(curve='P-256')


#writing a private key in a file
f = open('ecc_priv_key.pem','wt')
f.write(key.export_key(format='PEM'))
#print(key)
f.close()


#writing a public key in a file
f = open('ecc_pub_key.pem','wt')
public_key = key.public_key()
f.write(public_key.export_key(format='PEM'))
#print(public_key)
f.close()

