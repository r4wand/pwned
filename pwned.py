import hashlib
import requests

with open("passwords.txt", "r") as file:
    passwords = file.read().split('\n')

for password in passwords:
    SHA_PW = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head = SHA_PW[:5]
    url = 'https://api.pwnedpasswords.com/range/' + head
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('Error fetching "{}": {}'.format(
            url, res.status_code))

    HA = res.text.split('\n')
    for x in HA:
        if head + x[:35] == SHA_PW:
            print(password + "\n Cracked: " + x[36:])
