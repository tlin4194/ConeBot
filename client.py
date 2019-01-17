import requests
import readline

print('Clientside script running')
user_input = ''

while (user_input != 'q'):
    r = 'invalid command'
    user_input = raw_input('Command:')
    switch(user_input) {
        case 'h':
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/')
        case 't':
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/test')
    }
    print(r.json() + '\n')
    user_input = ''


print('---------------')
