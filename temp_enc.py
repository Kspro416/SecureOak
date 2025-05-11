from cryptography.fernet import Fernet

key = b'hloIpFX6poWrEk6o2rzusPHRrYTpYbgU5U-FgrEdDfY='
f = Fernet(key)

with open('data.json', 'rb') as orignal:
   orignal_files = orignal.read()
orignal1 = bytes(orignal_files)

with open('imp_1','wb') as encrypt:

    orignal1 = f.encrypt(orignal1)
    encrypt.write(orignal1)