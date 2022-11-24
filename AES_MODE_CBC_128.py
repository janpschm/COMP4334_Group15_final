#---------IMPORT---------
import time
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
#Imports for decrypt
from base64 import b64decode
from Crypto.Util.Padding import unpad
import Resources.DataInput

#--------FUNCTIONS & PARAMETERS--------

print("STARTING AES_MODE_CBC_128 SCRIPT")
key = get_random_bytes(16) #CHANGE KEY SIZE HERE
plaintext = b"testes plaintext to decrypt"

def encrypt(plaintext):
    #generate cipher and encrypt
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    #package and return
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    encrypted_result = json.dumps({'iv':iv, 'ciphertext':ct})
    #print(encrypted_result)
    return encrypted_result

def decrypt(ciphertext):
    try:
        #unpackage 
        b64 = json.loads(ciphertext)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        #decrypt
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        #print(pt)
    except (ValueError, KeyError):
        print("Incorrect decryption")


#Individual Testing Section
#--------ENCRYPTION--------
# record start time
start = time.time()

ciphertext = encrypt(plaintext)

# record end time
end = time.time()
# print the difference between start and end time in milli. secs
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#----------DECRYPTION---------

# record start time
start = time.time()

decrypt(ciphertext)

# record end time
end = time.time()
# print the difference between start and end time in milli. secs
print("The time of decryption was :",
	(end-start) * 10**3, "ms")
