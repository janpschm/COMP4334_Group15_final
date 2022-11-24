import time
import json
from base64 import b64encode
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


#--------FUNCTIONS & PARAMETERS--------
print("STARTING DES_MODE_OFB SCRIPT")
key = get_random_bytes(8) #just works with 8 Byte Key Size
plaintext = b'tested plaintext'

def encrypt(plaintext):
    cipher = DES.new(key, DES.MODE_OFB)
    ct_bytes = cipher.encrypt(plaintext) #padding? Block Size?
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    encrypted_result = json.dumps({'iv':iv, 'ciphertext':ct})
    return encrypted_result

def decrypt(ciphertext):
    try:
        b64 = json.loads(ciphertext)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = DES.new(key, DES.MODE_OFB, iv)
        pt = cipher.decrypt(ct)
        #print("The message was: ", pt)
    except (ValueError, KeyError):
        print("Incorrect decryption")

#test function to measure the time without Json packaging 
def encrypt_decrypt(ciphertext):
    cipher = DES.new(key, DES.MODE_OFB)
    ct_bytes = cipher.encrypt(plaintext) 
    try:
        iv = cipher.iv
        cipher = DES.new(key, DES.MODE_OFB, iv)
        pt = cipher.decrypt(ct_bytes)
        #print("The message was: ", pt)
    except (ValueError, KeyError):
        print("Incorrect decryption")


#Individual Testing Section
#--------ENCRYPTION--------
start = time.time()

ciphertext = encrypt(plaintext)
print(ciphertext)

end = time.time()
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#----------DECRYPTION---------
from base64 import b64decode

# record start time
start = time.time()

decrypt(ciphertext)

# record end time
end = time.time()

print("The time of decryption was :",
	(end-start) * 10**3, "ms")
