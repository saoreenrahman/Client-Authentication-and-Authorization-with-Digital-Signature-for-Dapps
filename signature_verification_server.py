#ECDSA Generation
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from pathlib import Path


#read nonce from text file 
countriesStr_1=Path('random.txt').read_text()


# Message digest: concatinating random nonce from a text file
f = open("message_digest_server.txt", "wb")
con = countriesStr_1 
message = str.encode(con)
f.write(message)
f.close()

#read signature from pem file
with open("ecc_sig_generation.pem", "rb") as f1:
    signature = f1.read()
    #print(signature)
    

#read keys for signature veriification
key = ECC.import_key(open('ecc_pub_key.pem').read())
verifier = DSS.new(key, 'fips-186-3')

#hashing message digest
h = SHA256.new(message)


#verification check
def ver(x,y):
    try:
        verifier.verify(x, y)
        print("Signature is correct.")
        return 1
    except ValueError:
        print("Invalid Signature.")
        return 0


ver(h, signature)

