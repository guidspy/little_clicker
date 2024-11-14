import time
import sys
import threading
from pynput.mouse import Controller, Button as B
from pynput.keyboard import Listener, KeyCode
import tkinter as tk
from Info import*





clicking10 = False
clicking100 = False
clicking1000 = False

TOGGLE_KEY = KeyCode(char="z")
TOGGLE_KEY2 = KeyCode(char="x")
TOGGLE_KEY3 = KeyCode(char="c")
KILL_KEY = KeyCode(char="k")

CLICK_EVENT = threading.Event()
mouse = Controller()



# Clicking CPS control
def clicker10():
    while True:
        if clicking10:
            mouse.click(B.left, 1)
        time.sleep(0.1)

def clicker100():
    while True:
        if clicking100:
            mouse.click(B.left, 1)
        time.sleep(0.01)

def clicker1000():
    while True:
        if clicking1000:
            mouse.click(B.left, 1)
        time.sleep(0.001)

# Clicking Control
def toggle_event(key):
    global clicking10
    global clicking100
    global clicking1000
    if key == TOGGLE_KEY:
        clicking10 = not clicking10
        clicking100 = False
        clicking1000 = False
        update_gui()
    
    if key == TOGGLE_KEY2:
        clicking100 = not clicking100
        clicking10 = False
        clicking1000 = False
        
        
        update_gui()
    
    if key == TOGGLE_KEY3:
        clicking1000 = not clicking1000
        clicking10 = False
        clicking100 = False
        
        
        update_gui()

    elif key == KILL_KEY:
        clicking10 = False
        clicking100 = False
        clicking1000 = False
        root.destroy()
        sys.exit()

def update_gui():
    if clicking10:
        status_label.config(text="Press Z to stop or K to KILL", bg="SpringGreen2", fg="black",font=("FixedSys", 15)) 
    
    elif clicking100:
        status_label.config(text="Press X to stop or K to KILL", bg="SpringGreen2", fg="black",font=("FixedSys", 15)) 
    
    elif clicking1000:
        status_label.config(text="Press C to stop or K to KILL", bg="SpringGreen2", fg="black",font=("FixedSys", 15)) 
    
    else:
        status_label.config(text="Press Z or X or C to start", bg="firebrick2",font=("FixedSys", 15)) 



# Starts the clicking
def start_clicker_thread():
    
    click_thread = threading.Thread(target=clicker10, daemon=True)
    click_thread.start()
    
    click_thread = threading.Thread(target=clicker100, daemon=True)
    click_thread.start()
    
    click_thread = threading.Thread(target=clicker1000, daemon=True)
    click_thread.start()


# Waits for the inputs
def start_listener():
    with Listener(on_press=toggle_event) as listener:
        listener.join()

# Create the GUI in the main thread
root = tk.Tk()
root.title("Clicker Status")

# Position the window at the bottom right corner
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 250
window_height = 30
#root.geometry(f"{window_width}x{window_height}+{screen_width - window_width}+{screen_height - window_height}")
root.geometry("250x30+0+0")

# Use slightly darker colors for the background
status_label = tk.Label(root, text="Press Z or X or C to start", bg="firebrick2", fg="white", font=("FixedSys", 15))
status_label.pack(fill="both", expand=True)

# Remove the window border to make it less obtrusive
root.overrideredirect(True)

# Keep the window always on top
root.attributes("-topmost", True)

# Start the clicking and listener in separate threads
start_clicker_thread()
threading.Thread(target=start_listener, daemon=True).start()

# Start the tkinter main loop in the main thread
root.mainloop()