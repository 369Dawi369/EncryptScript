import os
from cryptography.fernet import Fernet

files = []
ignoreFiles = ["EncScript.py", "KEY.key", "decrypt.py", "counter.txt"]

for file in os.listdir():
    if file in ignoreFiles:
        continue
    elif os.path.isfile(file):
        files.append(file)

with open("KEY.key", 'rb') as f:
    secretKEY = f.read()

for file in files:
    with open(file, 'rb') as g:
        contents = g.read()
    contentsDecrypted = Fernet(secretKEY).decrypt(contents)
    with open(file, 'wb') as h:
        h.write(contentsDecrypted)

with open("counter.txt", 'r+') as f:
    f.seek(0)
    f.write("0")
    f.truncate()

