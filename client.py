import requests
import readchar


print('Clientside script running')
user_input = ' '

while (user_input != 'q'):
    r = 'invalid command'
    user_input = ''
    user_input = readchar.readchar()

    if (user_input == 'h'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/')
        r = "hello"
    if (user_input == 't'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/test')
        r = "test"
    if (user_input == 'a'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/ccw')
        r = "a"
    if (user_input == 's'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/bck')
        r = "s"
    if (user_input == 'd'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/cw')
        r = "d"
    if (user_input == 'w'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/fwd')
        r = "w"
    if (user_input == 'o'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/armup')
        r = "o"
    if (user_input == 'l'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/armdown')
        r = "l"
    if (user_input == 'q'):
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/test')
        r = "Quitting"
    print(r + '\n')


print('---------------')
