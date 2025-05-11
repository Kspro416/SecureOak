from cryptography.fernet import Fernet

key = b'hloIpFX6poWrEk6o2rzusPHRrYTpYbgU5U-FgrEdDfY='
f = Fernet(key)

with open('imp_1', 'rb') as orignal:
   orignal_files = orignal.read()
orignal1 = bytes(orignal_files)

orignal1 = f.decrypt(orignal1)

with open('data.json','wb') as encrypt:

    orignal1 = f.decrypt(orignal1)
    encrypt.write(orignal1)