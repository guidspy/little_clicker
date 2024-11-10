import time
import threading
import sys
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Controller, Button as bb
import pynput.mouse as mouse



clicks = 0.01

TOGGLE_KEY = KeyCode(char="c")
KILL_KEY = KeyCode(char="k")

clicking = False
mouse=Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(bb.left,1)
        time.sleep(clicks)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
    
    elif key == KILL_KEY:
        clicking = False
        sys.exit()


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
