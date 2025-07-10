from cryptography.fernet import Fernet

# 🔑 Generate & Save Key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# 🔑 Load Existing Key
def load_key():
    return open("secret.key", "rb").read()

# 🔒 Encrypt File
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# 🔓 Decrypt File
def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)

# 📋 User Interface
def main():
    print("---- Advanced Encryption Tool (AES-like using Fernet) ----")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()
        print("Key generated and saved as secret.key")

    elif choice == "2":
        path = input("Enter filename to encrypt: ")
        key = load_key()
        encrypt_file(path, key)
        print("File encrypted successfully.")

    elif choice == "3":
        path = input("Enter filename to decrypt: ")
        key = load_key()
        decrypt_file(path, key)
        print("File decrypted successfully.")

    else:
        print("Invalid Option!")

if __name__ == "__main__":
    main()
from cryptography.fernet import Fernet

# 🔑 Generate & Save Key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# 🔑 Load Existing Key
def load_key():
    return open("secret.key", "rb").read()

# 🔒 Encrypt File
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# 🔓 Decrypt File
def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)

# 📋 User Interface
def main():
    print("---- Advanced Encryption Tool (AES-like using Fernet) ----")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()
        print("Key generated and saved as secret.key")

    elif choice == "2":
        path = input("Enter filename to encrypt: ")
        key = load_key()
        encrypt_file(path, key)
        print("File encrypted successfully.")

    elif choice == "3":
        path = input("Enter filename to decrypt: ")
        key = load_key()
        decrypt_file(path, key)
        print("File decrypted successfully.")

    else:
        print("Invalid Option!")

if __name__ == "__main__":
    main()

