import requests
import robocorp.log
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class ERP:
    @staticmethod
    def get_customers(COMPANY_ID, LOGIN_TOKEN):
        try:
            with robocorp.log.suppress_variables():
                base_url = decrypt_url("_Yfkxc_180fY6gXA_lSOP16XmdleEJEyZHsCnspS3e2vZTU2Rx34DwbrCyETgwT2zVu1_MXc1d5XfwfU5hLI3MTWS8RDt2_T24eKh2T_oOs=", COMPANY_ID)
                url = f"{base_url}?company_id={COMPANY_ID}&token={LOGIN_TOKEN}"
                response = requests.get(url)
                response.raise_for_status()
                return Customers(response.json())
        except requests.RequestException as e:
            raise RuntimeError("Error") from e

    @staticmethod
    def get_customer(COMPANY_ID, LOGIN_TOKEN, customer_id):
        try:
            with robocorp.log.suppress_variables():
                base_url = decrypt_url("_Yfkxc_180fY6gXA_lSOP16XmdleEJEyZHsCnspS3e2vZTU2Rx34DwbrCyETgwT2zVu1_MXc1d5XfwfU5hLI3MTWS8RDt2_T24eKh2T_oOs=", COMPANY_ID)
                url = f"{base_url}/{customer_id}?company_id={COMPANY_ID}&token={LOGIN_TOKEN}"
                response = requests.get(url)
                response.raise_for_status()
                return Customer(response.json())
        except requests.RequestException as e:
            raise RuntimeError("Error") from e

class Customers:
    def __init__(self, customers):
        self.customers = customers

    def id(self, archived=None):
        return [customer['id'] for customer in self._filter_customers(archived)]

    def name(self, archived=None):
        return [customer['name'] for customer in self._filter_customers(archived)]

    def _filter_customers(self, archived):
        if archived is None:
            return self.customers
        if archived:
            return [customer for customer in self.customers if customer.get('archived', False)]
        else:
            return [customer for customer in self.customers if not customer.get('archived', False)]

    def __repr__(self):
        return str(self.customers)

class Customer:
    def __init__(self, customer_data):
        self.customer_data = customer_data

    def name(self):
        return self.customer_data['name']

    def archived(self):
        return self.customer_data.get('archived', False)

    def __repr__(self):
        return str(self.customer_data)
    
def derive_key(key, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(key)

def decrypt_url(encrypted_url, key):
    key_bytes = key.encode('utf-8')
    encrypted_data = base64.urlsafe_b64decode(encrypted_url.encode('utf-8'))
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    derived_key = derive_key(key_bytes, salt)
    encrypted_url = encrypted_data[32:]
    
    cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    padded_url = decryptor.update(encrypted_url) + decryptor.finalize()
    
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    url = unpadder.update(padded_url) + unpadder.finalize()
    
    return url.decode('utf-8')