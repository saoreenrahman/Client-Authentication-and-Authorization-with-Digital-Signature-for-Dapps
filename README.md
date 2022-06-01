# Client-Authentication-and-Authorization-with-Digital-Signature-for-Dapps
Python code for generating random nonce and then using that random nonce to generate ECC signature in client side and verify ECC signature in server side.

Required Software: Python (version>3)

Python Libraries: datetime,ECC, SHA256, random, time

Instructions:

1. run random_nonce.py to generate randomness beacon.

2. run key_generation to generate keys for each side

3. run signature_generation.py in client side to generate client's signature with client's private key.

4. run signature_verification.py in server side to verify client's signature with client's public key.

N.B. random nonce is considered as message digest. Signature verification considers latest random nonce to match message digest. Certificate generation is an additional code that generates self-signed certificates on user-defined data.

Important Notes: above codes can be similar to the codes available in in verious websites. This application was designed and constructed based on certain requirements.
