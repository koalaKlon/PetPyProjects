import os
from cryptography import fernet
from cryptography.fernet import Fernet


class Encrypter:
    def create_key(self):
        """ This function creates a Key for Encryption and Decryption."""

        key_generator = False

        while not key_generator:

            try:
                with open('key/key.key', 'wb') as f:
                    f.write(Fernet.generate_key())
                    f.close()

                print('Key Generated.')

                key_generator = True

            except:
                os.makedirs('./key')

    def encrypt_file(self, file):
        """This Function Encrypts the file which is given as the parameter"""

        file_name = file.split('\\')[-1]

        with open(file, 'rb') as f:
            data = f.read()
            f.close()

        try:
            with open('key/key.key', 'rb') as f:
                key = f.read()
                f.close()

        except:
            print("Key not Found Please Generate a Key")

        file_written = False

        while not file_written:
            try:
                os.makedirs('./Encrypted Files')
            except FileExistsError:
                with open('Encrypted Files/Encrypted {}'.format(file_name), 'wb') as f:
                    f.write(Fernet(key).encrypt(data))
                    f.close()
                os.remove(file)
                print("File Encrypted")
                file_written = True

    def decrypt_file(self, encrypted_file):
        """This Function Decrypts the file"""

        file_name = encrypted_file.split('\\'[-1])
        file_name = file_name.split(' ')[-1]

        with open(encrypted_file, 'rb') as f:
            data = f.read()
            f.close()

        with open('key/key.key', 'rb') as f:
            key = f.read()
            f.close()

        file_written = False

        while not file_written:

            try:
                os.makedirs('./Decrypted Files')

            except FileExistsError:
                with open('Decrypted Files/{}'.format(file_name), 'wb') as f:
                    f.write(Fernet(key).decrypt(data))
                    f.close()

                print("File Decrypted.")
                file_written = True



