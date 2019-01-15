from pynput import keyboard

def on_press(key):
    try:
        if(key.char == 'w'): 
            print("forward")
        elif (key.char == 's'): 
            print("backward")
        elif (key.char == 'a'):
            print("rotate CCW")
        elif (key.char == 'd'):
            print("rotate CW")
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

