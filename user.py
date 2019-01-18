from pynput import keyboard
import requests

def on_press(key):
    try:
        if(key.char == 'w'):
            r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/fwd')
        elif (key.char == 's'):
            r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/bck')
        elif (key.char == 'a'):
            r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/ccw')
        elif (key.char == 'd'):
            r = requests.get('http://conebot.wv.cc.cmu.edu:5000/teleop/cw')
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        r = requests.get('http://conebot.wv.cc.cmu.edu:5000/reset')

        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

