import random
import hashlib
from datetime import datetime

# this isnt particularly efficent but time.time returns something really dumb
start = int(datetime.utcnow().timestamp())
attempts = 0
done = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
validHashing = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'md5']
finished = False

password = input('hash: ')
print(f"Supported types: {validHashing}")
method = input('method: ')

sha1 = hashlib.sha1 
sha224 = hashlib.sha224
sha256 = hashlib.sha256 
sha384 = hashlib.sha384
sha512 = hashlib.sha512
md5 = hashlib.md5

if method not in validHashing:
    print('Not valid')
    exit()

disableAlreadyTestedLog = True
disableNotThePasswordLog = True

while finished == False:
    attempts = attempts + 1
    test = ''

    # this code is stupidly inefficent but i wrote it really quickly because i was bored
    test = test + random.choice(letters)
    test = test + random.choice(letters)
    test = test + random.choice(letters)
    test = test + random.choice(letters)
    test = test + random.choice(letters)

    finalised = hashlib.sha256(bytes(test, encoding='utf-8')).hexdigest()

    # id use match case but its only available in the beta right now so i wont for compatibility
    # enjoy the spaghetti code
    if method == 'sha1':
        finalised = sha1(bytes(test, encoding='utf-8')).hexdigest()
    elif method == 'sha224':
        finalised = sha224(bytes(test, encoding='utf-8')).hexdigest()
    elif method == 'sha256':
        finalised = sha256(bytes(test, encoding='utf-8')).hexdigest()
    elif method == 'sha384':
        finalised = sha384(bytes(test, encoding='utf-8')).hexdigest()
    elif method == 'sha512':
        finalised = sha512(bytes(test, encoding='utf-8')).hexdigest()
    elif method == 'md5':
        finalised = md5(bytes(test, encoding='utf-8')).hexdigest()

    if test in done:
        if disableAlreadyTestedLog == False:
            print(f"{test} already tested")

        continue
    
    if finalised == password:
        finished = True
        print(f"\nPassword: {test}")
        print(f"Method: {method}")
        print(f"Attempts: {attempts}")
        print(f"Time taken (seconds): {(int(datetime.utcnow().timestamp()) - start)}")
    else:
        if disableNotThePasswordLog == False:
            print(f"{test} ({finalised}) is not the password")
        
        done.append(test)
