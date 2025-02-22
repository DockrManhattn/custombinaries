import sys
from Crypto.Hash import MD4

def nt_hash(password):
    # Encode the password in UTF-16LE
    utf16le_password = password.encode('utf-16le')
    # Compute the MD4 hash
    md4_hash = MD4.new(utf16le_password).hexdigest()
    return md4_hash

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 nthash.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    hash_result = nt_hash(password)
    print(f"NT Hash of '{password}' is: {hash_result}")
