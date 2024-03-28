# felt i needed to add comments bc my code isnt ever super readable yk
import time
import json
import random
import requests
from colorama import Fore, Style

# got sidetracked making my name github link look cool
def rt(text):
    rc = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    ct = ''
    for char in text:
        rch = random.choice(rc)
        ct += rch + char + Style.RESET_ALL

    return ct
print(f'Created by {rt("github.com/lhwe")} <3')
# get random usernames
with open('names.txt', 'r') as f: # make newline for each name (currently has 10,000 in it to start)
    names = f.read().splitlines()

# timer for logs
logStarter = Fore.CYAN+f'{time.strftime("[%H:%M:%S]", time.localtime())}{Fore.RESET} - '

# starting_num = 0
# if starting_num < 1:
#     starting_num +=1

theUrlForBrowsers = 'https://www.gimkit.com/join?gc='
room_info_api = 'https://www.gimkit.com/api/matchmaker/find-info-from-code'
code = input(logStarter+'Gimkit Code > ')

# Check if the code is a number
if not code.isdigit():
    print(logStarter+'Please enter a valid code!')
    exit()
else:
    pass

# just massJoiner options
massJoinAsk = input(logStarter+'Mass Joiner? y/n > ')
if massJoinAsk == 'y' or 'Y':
    print(Fore.YELLOW+'[NOTICE] This is an experimental feature, please open issues if any bugs happen, i will try to fix them asap!')
    randomizeBots = input('Do you want to;\n[1] custom names (like bot_1, bot_2, etc.)\n[2] Use the names from names.json file.\n> ')
    massJoin = True

# get room info
room_info_response = requests.post(room_info_api, json={"code": code})
room_info = room_info_response.json()
print(logStarter,room_info)


# removed name random name bypasser. Reason: buggy and slower than using random gen names
if room_info["useRandomNamePicker"] == False:
    if randomizeBots == '1':
        name = input('Bot name > ').join(f'{i+1}')
    else:
        name = random.choice(names)
else:
    name = random.choice(names)

# prepare the JSON
join_json = {
    "clientType": "Gimkit ⁢⁣⁡‍‌‌‌⁣‍⁢⁡⁢‍⁢⁡‌⁢⁡‍⁡⁢⁢⁢⁤⁤⁤‌⁡‌⁤⁤‍‌‌‍⁢⁣⁣⁡‍⁢⁡⁣⁣‌⁢⁢⁢‌⁣‍⁢⁡‍‌⁢⁡⁢‍⁢⁡⁢⁢‍⁢⁢‌‍⁡⁢‍⁢‌‍⁡‌⁡⁢⁢⁢‌⁡‍⁤⁡⁢⁡‍⁢⁢‌⁢⁢⁢⁢⁤⁣⁤⁡⁢⁣⁢⁡⁢‌⁡⁢‌⁣‍⁤‍‌⁢‍‌⁡‌⁡‌‌⁢⁡⁣‌⁡⁢‌⁤⁢‌⁢‍⁢⁣⁢‍⁢⁢⁣‌⁣⁡‍⁡‍⁤⁢⁡‍⁡‌⁢‌⁢⁢⁣⁢‍⁢⁡⁢⁤‌⁤⁢⁡⁢⁡‌⁡‌⁢‍⁡‍‌⁢⁣‌‍⁤‍⁤⁢⁣⁤⁡‌⁣⁡‌⁡‍⁢⁢⁡⁢⁡‍‌‍⁢⁡⁢⁢⁢‌⁤‍⁢‌‍⁢⁡⁢⁢‌⁢‌⁡⁢⁢⁢‍‌⁡⁢⁢‌⁣‌‍‌⁣⁤⁡⁢⁡‍‌‍⁢⁡‌‍‌‌⁢⁣‌⁤⁢‌⁣⁣‌⁡‌⁤‍⁢⁤‌⁡‌⁡‌⁢‌‍⁢‌‍‌‍‌‌⁢‌‌‍Web Client V3.1",
    "roomId": room_info['roomId'],
    "name": name
}

# send the request
join_response = requests.post('https://www.gimkit.com/api/matchmaker/join', json=join_json)

# join url
clickableLink = theUrlForBrowsers + code

# mass joiner
if massJoin != True:
    pass
else:
    if randomizeBots == '1':
        print(logStarter+'Custom names loaded from names.json.')
    elif randomizeBots == '2':
        print(logStarter+'Randomized names loaded.')
        # random names get genned here
        for i in range(len(names)):
            print(f"bot_{i+1}: {names[f'name{i}']}")
    else:
        print('Not a valid option, please try again!')
        exit()
    howMany = input(logStarter+'How many > ')
    join_response
    starting_num += 1


print(logStarter,f"Joined {clickableLink} as {name} ({join_response.status_code})")

print(logStarter+f'Joined {clickableLink} with {howMany} users')