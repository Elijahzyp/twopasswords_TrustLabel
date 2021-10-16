from os import getenv
from typing import Union
from cryptography.fernet import Fernet
from dotenv import load_dotenv


class EncryptionEngine:
    """
    This class is responsible for all the Encryption / Decryption
    operations needed in the code such as:
    - key file generation
    - key file loading
    - encryption str object to bytes
    - decryption bytes type to string
    """

    def __init__(self, data: Union[str, bytes]):
        self.data = data  # can be either string or bytes type

    load_dotenv()
    KEY_PATH = getenv("KEY_FILE")

    # generate unique key file
    # one should store it in **SECURE PLACE**
    @staticmethod
    def generate_key() -> None:
        key = Fernet.generate_key()
        with open(EncryptionEngine.KEY_PATH, "wb") as keyfile:
            keyfile.write(key)

    # load the previously generated key file
    # and return it as Fernet object
    @staticmethod
    def load_key() -> Fernet:
        key = open(EncryptionEngine.KEY_PATH, "rb").read()
        f = Fernet(key)
        return f

    # encode string to bytes and then
    # encrypt data with a key
    def encrypt(self) -> bytes:
        fernet_obj = self.load_key()
        encoded_data = self.data.encode()
        encrypted_data = fernet_obj.encrypt(encoded_data)
        return encrypted_data

    # decrypt data with a key and then
    # decode from bytes
    def decrypt(self) -> str:
        fernet_obj = self.load_key()
        decrypted_data = fernet_obj.decrypt(self.data)
        decoded_data = decrypted_data.decode()
        return decoded_data

    def __repr__(self) -> str:
        return f'EncryptionEngine("{self.data}")'


if __name__ == "__main__":
    # some EE class practice below...

    EncryptionEngine.generate_key()  # generate key file if needed

    # create new EE object that should be encrypted
    password = "encode*this-O!K@J$M^6259"
    print(f"PASSWORD THAT WILL BE ENCRYPTED: {password}")
    my_password = EncryptionEngine(password)

    print("-" * 30)

    print("repr_test_here:")
    print(my_password)  # repr test

    print("-" * 30)

    encrypted_password = my_password.encrypt()  # do encryption
    print(encrypted_password)  # print bytes previously generated by encryption

    print("-" * 30)

    # create new EE object that should be decrypted
    my_bytes = EncryptionEngine(encrypted_password)

    password_was = my_bytes.decrypt()  # do decryption

    print(f"PASSWORD THAT WAS DECRYPTED: {password}")  # print password