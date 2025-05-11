from Encryption import crypting
from os import remove
import tempfile
import sys
import os
import json
from easygui import passwordbox, enterbox
from cryptography.fernet import Fernet
''' If you want to check the password
 please run the temp_dec.py and a data.json file will be made then check it...'''

key = b'hloIpFX6poWrEk6o2rzusPHRrYTpYbgU5U-FgrEdDfY='
f = Fernet(key)

def main():
    pass

with open('imp_1','rb') as encrypt:
    encrypt1 = encrypt.read()

decrypt = f.decrypt(encrypt1)
try:
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as tmp:
            tmp.write(decrypt)
            tmp_path = tmp.name
except Exception as e:
        print("Failed to create temporary file:", str(e))
        sys.exit(1)

try:
    with open(tmp_path, 'rb') as a:
        data = json.load(a)
    for user_info in data['users']:
        input_user1_user = enterbox("Enter username: ")
        input_pass1_pass = passwordbox("Enter password: ")

        if user_info['user'] == input_user1_user and user_info['pass'] == input_pass1_pass:
            main()#Put your function here... This is an example....
        else:
            print("Unsucess")

finally:
    try:
        os.unlink(tmp_path)
    except:
        pass

#Thank You for downloading the Program