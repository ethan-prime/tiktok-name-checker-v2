import requests
import random
using_multiple_cookies = False
cookie = []

print('AVAILABLE DOES NOT MEAN THE NAME IS SURELY AVAILABLE; IT ONLY MEANS THAT IT COULD NOT DETECT AN ACCOUNT WITH SPECIFIED USERNAME')
print('GET COOKIE(S) BY VISTING https://www.tiktok.com/ , HEAD TO "NETWORK" TAB IN DEVELOPER TOOLS , UNDER "REQUEST HEADERS" , RIGHT CLICK ON THE VALUE NEXT TO "cookie: " AND SELECT "Copy Value" PASTE THIS VALUE INTO PROMPT. YOU MAY INPUT AS MANY COOKIES AS YOU WOULD LIKE , WHEN DONE SIMPLY SUBMIT AN EMPTY INPUT.')

def get_cookies():
    c = input('Please input cookie(s):')
    if len(c) > 0:
        cookie.append(c)
        get_cookies()

get_cookies()

if len(cookie) > 1:
    using_multiple_cookies = True

def cycle_cookies():
    use = cookie.pop(0)
    cookie.append(use)
    return use

names = []
with open('usernames.txt') as f:
    names = f.readlines()

for i in range(len(names)):
    names[i] = names[i].replace('\n', '') 

if len(names) == 0:
    if input('Generate random names [Y/N]: ') == 'Y':
        number = int(input('How many names: '))
        length = int(input('How long each name should be: '))
        use_only_letters = bool(input('Use only letters [Y/N]: '))
        if use_only_letters == 'Y':
            char_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        else:
            char_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for i in range(number):
            new_name = []
            for x in range(length):
                new_name.append(random.choice(char_set))
            names.append(''.join(new_name))

if len(names) == 0:
    names = (input('Input names to be checked: ')).split(' ')

results = []

n = 0
for name in names:
    n += 1
    if using_multiple_cookies:
        use_cookie = cycle_cookies()
        r = requests.get(f'https://www.tiktok.com/@{name}', headers={'cookie': use_cookie, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'})
    else:
        r = requests.get(f'https://www.tiktok.com/@{name}', headers={'cookie': cookie[0], 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'})
    if(r.status_code == 200):
        print(f'[TAKEN] {name} [{n}/{len(names)}]')
    elif(r.status_code == 404):
        print(f'[AVAILABLE] {name} [{n}/{len(names)}]')
        results.append(name)

with open('usernames.txt', 'w') as f:
    for name in results:
        f.write(f'{name}\n')

print('RESULTS PRINTED IN usernames.txt')
print(f'ALL NAMES FOUND: {results}')