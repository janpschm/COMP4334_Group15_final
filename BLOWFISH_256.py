from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import Blowfish
from struct import pack
import time
import json
from base64 import b64decode
from base64 import b64encode

from Crypto.Util.Padding import unpad
import Resources.DataInput


#--------FUNCTIONS & PARAMETERS--------

print("STARTING BLOWFISH SCRIPT")
key = get_random_bytes(32) #256 bit key
plaintext = b"test"

def encrypt(plaintext):
    bs = Blowfish.block_size
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    plen = bs - len(plaintext) % bs
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    ct_bytes = cipher.encrypt(plaintext + padding)

    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    encrypted_result = json.dumps({'iv':iv, 'ciphertext':ct})
    return encrypted_result


def decrypt(ciphertext):
    try: 
        b64 = json.loads(ciphertext)
        iv = b64decode(b64['iv'])
        ciphertext = b64decode(b64['ciphertext'])

        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        msg = cipher.decrypt(ciphertext)
        last_byte = msg[-1]
        msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
        #print(repr(msg))
        
    except (ValueError, KeyError):
        print("Incorrect decryption")


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