from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keys():

    private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()) 
    
    public_key = private_key.public_key()

    return private_key, public_key

def encrypt_private_key(a_message, private_key):
    encrypted = private_key.encrypt(
        a_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def decrypt_public_key(encoded_encrypted_msg, public_key):
    original_message = public_key.decrypt(
        encoded_encrypted_msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message

def main():
    #Generate Private and Public Keys for the Node B
    private, public = generate_keys()
          
    #Converting Keys to Bytes to store in the file    
    private_key = private.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
            )
    public_key = public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
    
    #Storing the Public and Private keys into the file         
    with open('private_key.txt', 'wb') as f:
        f.write(private_key)
    with open('public_key.txt', 'wb') as f:
        f.write(public_key)
                
    #Reading Private and Public Keys from the files
    with open("private_key.txt", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
    with open("public_key.txt", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        
    #Binary Message to be encrypted using Node B public Key
    print("=======================================")

    f = open("message.txt", "rb")
    message = f.read()
    print("Message fetched!")
    #Encoded Message
    print("=======================================")
    encoded = encrypt_private_key(message, public)
    print("Message encoded!")
    print("=======================================\nDecrypting!")

    #Message Decryption using Node B private Key
    message = decrypt_public_key(encoded, private)
    print("=======================================")
    print("Message Decoded!")
    print("=======================================")

    print(message)
  
if __name__== "__main__":
  main()