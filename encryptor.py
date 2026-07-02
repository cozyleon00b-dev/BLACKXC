import os
import sys
from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self):
        self.key_file = "master.key"
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)
    
    def _load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            return key
    
    def encrypt_file(self, file_path):
        if not os.path.exists(file_path):
            return
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted = self.cipher.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted)
        print(f"[✓] Encrypted: {file_path}")
    
    def decrypt_file(self, file_path):
        if not os.path.exists(file_path):
            return
        with open(file_path, "rb") as f:
            encrypted = f.read()
        decrypted = self.cipher.decrypt(encrypted)
        with open(file_path, "wb") as f:
            f.write(decrypted)
        print(f"[✓] Decrypted: {file_path}")

if __name__ == "__main__":
    encryptor = Encryptor()
    files = [
        "main.py", "database.py", "admin.py", "tools.py", "dump.py", "utils.py",
        "modules/attack.py", "modules/bypass.py", "modules/checker.py"
    ]
    
    print("[!] BLACKXC ENCRYPTOR")
    print("[1] Encrypt All Files")
    print("[2] Decrypt All Files")
    
    choice = input("[>] Select: ").strip()
    
    if choice == "1":
        for f in files:
            encryptor.encrypt_file(f)
        print("[✓] All files encrypted!")
    elif choice == "2":
        for f in files:
            encryptor.decrypt_file(f)
        print("[✓] All files decrypted!")