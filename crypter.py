# Encrypt/Decrypt file, key and iv saved in file

from cryptography.fernet import Fernet
import argparse


def write_key(keyFile):
    """
    Generates a key and saves it into a file
    """
    key = Fernet.generate_key()
    with open(keyFile, "wb") as key_file:
        key_file.write(key)
        
def load_key(keyFile):
    """
    Loads the key file
    """
    return open(keyFile, "rb").read()
    
def encrypt(plainFile, key, cipherFile):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    f = Fernet(key)
    with open(plainFile, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(cipherFile, "wb") as file:
        file.write(encrypted_data)

def decrypt(cipherFile, key, plainFile):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(cipherFile, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(plainFile, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Encryptor/Decryptor Script with Key generator.")
    parser.add_argument("keyFile", help="File to store the key")
    parser.add_argument("inputFile", help="File to encrypt/decrypt")
    parser.add_argument("outputFile", help="Output file")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()
    keyFile = args.keyFile
    inputFile = args.inputFile
    outputFile = args.outputFile

    if args.encrypt:
        print("***Starting encryption process***")
        print("***Generating Key file***")
        write_key(keyFile)
        print("***Key file saved***")
        print("***Loading Key file***")
        key = load_key(keyFile)
        print("***Key file loaded***")
    elif args.decrypt:
        print("***Starting decryption process***")
        print("***Loading Key file***")
        key = load_key(keyFile)
        print("***Key file loaded***")

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        encrypt(inputFile, key, outputFile)
        print("***Encryption complete***")
    elif decrypt_:
        decrypt(inputFile, key, outputFile)
        print("***Decryption complete***")
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")


