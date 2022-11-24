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

#--------FUNCTIONS & PARAMETERS--------

print("STARTING AES_MODE_CBC_192 SCRIPT")
key = get_random_bytes(24) #CHANGE KEY SIZE HERE
plaintext = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam accumsan lacus velit, non scelerisque turpis maximus quis. Etiam et gravida nisl. Suspendisse potenti. Integer est felis, venenatis tincidunt posuere quis, fringilla eu urna. Donec commodo tincidunt enim, ut luctus dolor venenatis tempor. Vestibulum placerat neque consectetur fermentum ultrices. Pellentesque pretium tristique cursus. Morbi a sapien leo. Suspendisse semper nunc quis urna suscipit, ac porttitor justo auctor. Morbi leo risus, varius nec nisi quis, faucibus facilisis mauris. Sed vehicula, metus quis elementum aliquet, elit odio tristique velit, vel bibendum metus ex quis felis. Pellentesque habitant morbi tristique senectus et netus et'

def encrypt(plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    #print(ct_bytes)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    encrypted_result = json.dumps({'iv':iv, 'ciphertext':ct})
    #print("The Encrypted result:"+encrypted_result) 
    return encrypted_result

def decrypt(ciphertext):
    try:
        b64 = json.loads(ciphertext)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        #print("The message was: ", pt)
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
