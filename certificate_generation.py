import datetime

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from Crypto.PublicKey import ECC
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives import serialization as crypto_serialization
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.exceptions import InvalidSignature

#generating key for root
root_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

#information regarding issuer
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Texas"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Austin"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"My CA"),
])

root_cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    root_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=3650)
).sign(root_key, hashes.SHA256(), default_backend())

# generate a cert for root
cert_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

#read public key
with open('ecc_pub_key.pem', 'r') as f:
    p_k_b = f.read()
    #print(p_k_b)
    p_k_b_as_bytes = str.encode(p_k_b)
  
key = load_pem_public_key(p_k_b_as_bytes, default_backend())


#generating user certificate based on user defined information
new_subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Texas"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Austin"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"New Org Name!"),
])
cert = x509.CertificateBuilder().subject_name(
    new_subject
).issuer_name(
    root_cert.issuer
).public_key(
    #private_key.public_key()
    key
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=30)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"somedomain.com")]),
    critical=False,
).sign(root_key, hashes.SHA256(), default_backend())

#write cert into cert file
with open("cert.crt", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))
    f.close()

#read cert to verify whether it is generated or not!
cert_str1=Path('cert.crt').read_text()
print('certificate is generated')






