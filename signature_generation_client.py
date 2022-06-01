# #confirmed EC key , sign generation, sign validation (final)
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from pathlib import Path


#read nonce from text file
countriesStr_1=Path('random.txt').read_text()


# Message digest: concatinating random number 
f = open("message_digest_client.txt", "wb")
con = countriesStr_1 
v_as_bytes = str.encode(con)
message = v_as_bytes
f.write(message)
f.close()



#signature generation
key = ECC.import_key(open('ecc_priv_key.pem').read())
h = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(h)
print(signature)


#write signature into a text file!!!
f = open("ecc_sig_generation.pem", "wb")
f.write(signature)
f.close()

