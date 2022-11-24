import time
import json
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode

#--------FUNCTIONS & PARAMETERS--------
plaintext = b'We are no longer the knights who say ni!'
while True:
        try:
            key = DES3.adjust_key_parity(get_random_bytes(24))
            break
        except ValueError:
            pass

def encrypt(plaintext):
    cipher = DES3.new(key, DES3.MODE_CFB)
    ct_bytes = cipher.encrypt(plaintext)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    encrypted_result = json.dumps({'iv':iv, 'ciphertext':ct})
    #print(encrypted_result)
    return encrypted_result

def decrypt(ciphertext):
    try:
        b64 = json.loads(ciphertext)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = DES3.new(key, DES3.MODE_CFB, iv)
        pt = cipher.decrypt(ct)
        #print("The message was: ", pt)
    except (ValueError, KeyError):
        print("Incorrect decryption")

#Individual Testing Section
#-----------------encryption-------------------
start = time.time()
ciphertext = encrypt(plaintext)
end = time.time()
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#----------DECRYPTION---------
from base64 import b64decode, b64encode

start = time.time()

decrypt(ciphertext)

end = time.time()
print("The time of decryption was :",
	(end-start) * 10**3, "ms")