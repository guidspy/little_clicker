from tkinter import*
#import time
#import threading
#import sys
#from pynput.keyboard import Listener, KeyCode
#from pynput.mouse import Controller, Button as bb
#import pynput.mouse as mouse


clicks = "1"



def click():
    clicks = "0.1"
    print(clicks)

def clickc():
    clicks = "0.01"
    print(clicks)


#sleepc = float(clicks.get("clicks"))



#def clicker():
#    while True:
#        if clicking:
#            mouse.click(bb.left,1)
#        time.sleep(sleepc)


#def toggle_event(key):
 #   if key == TOGGLE_KEY:
 #       global clicking
 #       clicking = not clicking
    
 #  elif key == KILL_KEY:
 #       clicking = False
 #       sys.exit()
    


window = Tk()
window.config(bg='black')
window.title("Little Clicker")
window.geometry('500x500')



b = Button(window, text = "10", command=click,)
b.config(font=('ink free',50, 'bold'))
b.place( x=190, y=50 )

c = Button(window, text = "100", command=clickc,)
c.config(font=('ink free',50, 'bold'))
c.place( x=170, y=200 )



#TOGGLE_KEY = KeyCode(char="c")
#KILL_KEY = KeyCode(char="k")

#clicking = False
#mouse=Controller()


#click_thread = threading.Thread(target=clicker)
#click_thread.start()

#with Listener(on_press=toggle_event) as listener:
#    listener.join()


window.mainloop()
