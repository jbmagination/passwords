import random
import hashlib

#password = input('enter hash: ')
password = '4417a30dc8c6b53f5e2e2b9051159348036017f9061e8ace1f966a1ab58fbedd'

done = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
validHashing = ['sha256']
finished = False

while finished == False:
    test = ''

    # this code is stupidly inefficent but i wrote it really quickly because i was bored
    test = test + random.choice(letters)
    test = test + random.choice(letters)
    test = test + random.choice(letters)
    test = test + random.choice(letters)
    test = test + random.choice(letters)

    finalised = hashlib.sha256(bytes(test, encoding='utf-8')).hexdigest()
    if finalised == password:
        print(f"the password is {test}")
    else:
        print(f"{test} ({finalised}) is not the password")
        done.apped(test)
