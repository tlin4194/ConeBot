import requests
import readline

print('Clientside script running')
user_input = ' '

while (user_input[0] != 'q'):
    r = 'invalid command'
    user_input = ' '
    user_input = raw_input('Command:')[0]
    if (user_input == 'h'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/')
    if (user_input == 't'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/test')
    print(r + '\n')


print('---------------')
