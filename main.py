import time
import Resources.DataInput

import AES_MODE_CBC_128
import AES_MODE_CBC_192
import AES_MODE_CBC_256

import DES_MODE_OFB_64
import DES_TRIPLE_192
import BLOWFISH_128
import BLOWFISH_256

# HOW TO USE THIS PERFORMANCE TEST:
# Start this Script to get the performance output of all listed Encryption functions. 
# Use the Resources.DataInput to change the fixed used data input 
# Use the i and j parameter to change how often the encryption function is used

#When reading the Output start at the Marked Point
 
#--------PARAMETERS--------

#Plaintext to encrypt/decrypt for all Algorithms
plaintext = Resources.DataInput.plaintext_10_000b #change the data input
i = 100 #change the execution amount
j = 100#variable used, should be same as i 

print("----------FROM HERE ON STARTS THE RELEVANT OUTPUT OF THE MAIN SCRIPT ----------")
#--------AES_MODE_CBC_128----------------------
print("----------AES_MODE_CBC_128----------")
#ENCRYPTION
start = time.time()
while j>0:
	ciphertext = AES_MODE_CBC_128.encrypt(plaintext)
	j -= 1
end = time.time()
j = i 
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#DECRYPTION
start = time.time()
while j>0:
	AES_MODE_CBC_128.decrypt(ciphertext)
	j -= 1
end = time.time()
j = i 
print("The time of decryption was :",
	(end-start) * 10**3, "ms")

#--------AES_MODE_CBC_192-------------------------
print("----------AES_MODE_CBC_192----------")
#ENCRYPTION
start = time.time()
while j>0:
	ciphertext = AES_MODE_CBC_192.encrypt(plaintext)
	j -= 1
end = time.time()
j = i 
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#DECRYPTION
start = time.time()
while j>0:
	AES_MODE_CBC_192.decrypt(ciphertext)
	j -= 1
end = time.time()
j = i 
print("The time of decryption was :",
	(end-start) * 10**3, "ms")

#--------AES_MODE_CBC_256-------------------------
print("----------AES_MODE_CBC_256----------")
#ENCRYPTION
start = time.time()
while j>0:
    ciphertext = AES_MODE_CBC_256.encrypt(plaintext)
    j -= 1
j = i
end = time.time()
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#DECRYPTION
start = time.time()
while j>0:
    AES_MODE_CBC_256.decrypt(ciphertext)
    j -= 1
j = i
end = time.time()
print("The time of decryption was :",
	(end-start) * 10**3, "ms")

#--------DES_MODE_OFB_64-------------------------
print("----------DES_MODE_OFB_64----------")
#ENCRYPTION
start = time.time()
while j>0:
	ciphertext = DES_MODE_OFB_64.encrypt(plaintext)
	j -= 1
end = time.time()
j = i 
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#DECRYPTION
start = time.time()
while j>0:
	DES_MODE_OFB_64.decrypt(ciphertext)
	j -= 1
end = time.time()
j = i 
print("The time of decryption was :",
	(end-start) * 10**3, "ms")

#--------DES_TRIPLE_192-------------------------
print("----------DES_TRIPLE_192----------")
#ENCRYPTION
start = time.time()
while j>0:
	ciphertext = DES_TRIPLE_192.encrypt(plaintext)
	j -= 1
end = time.time()
j = i 
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#DECRYPTION
start = time.time()
while j>0:
	DES_TRIPLE_192.decrypt(ciphertext)
	j -= 1
end = time.time()
j = i 
print("The time of decryption was :",
	(end-start) * 10**3, "ms")


#--------BLOWFISH_128----------------------
print("----------BLOWFISH_128----------")
#ENCRYPTION
start = time.time()
while j>0:
	ciphertext = BLOWFISH_128.encrypt(plaintext)
	j -= 1
end = time.time()
j = i 
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#DECRYPTION
start = time.time()
while j>0:
	BLOWFISH_128.decrypt(ciphertext)
	j -= 1
end = time.time()
j = i 
print("The time of decryption was :",
	(end-start) * 10**3, "ms")

#--------BLOWFISH_256----------------------
print("----------BLOWFISH_256----------")
#ENCRYPTION
start = time.time()
while j>0:
	ciphertext = BLOWFISH_256.encrypt(plaintext)
	j -= 1
end = time.time()
j = i 
print("The time of encryption was :",
	(end-start) * 10**3, "ms")

#DECRYPTION
start = time.time()
while j>0:
	BLOWFISH_256.decrypt(ciphertext)
	j -= 1
end = time.time()
j = i 
print("The time of decryption was :",
	(end-start) * 10**3, "ms")