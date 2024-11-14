from tkinter import *


info_window = Tk()
info_window.title('How many clicks???')
app_width = 500
app_height = 350


# Centralizing the window
screen_width = info_window.winfo_screenwidth()
screen_heigth = info_window.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_heigth / 2) - (app_height / 2)

info_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


# Main window background color
info_window.config(bg="black",)



# Putting columns
info_window.columnconfigure(0,weight=1)
info_window.columnconfigure(1,weight=1)


# Header
CPS_label = Label(info_window, text="Cliks per Second", bg="black", fg="lawn green", font=("FixedSys", 25))
CPS_label.grid(columnspan=2, row=1)

# Info
Z_label = Label(info_window, text="Z",bg="black", fg="lawn green", font=("FixedSys", 25))
Z_label.grid(column=0, row=2)
Z_10 = Label(info_window, text="10",bg="black", fg="lawn green", font=("FixedSys", 25))
Z_10.grid(column=1, row=2)

X_label = Label(info_window, text="X",bg="black", fg="lawn green", font=("FixedSys", 25))
X_label.grid(column=0, row=3)
X_10 = Label(info_window, text="100",bg="black", fg="lawn green", font=("FixedSys", 25))
X_10.grid(column=1, row=3)

C_label = Label(info_window, text="C",bg="black", fg="lawn green", font=("FixedSys", 25))
C_label.grid(column=0, row=4)
C_10 = Label(info_window, text="1000",bg="black", fg="lawn green", font=("FixedSys", 25))
C_10.grid(column=1, row=4)

# Header
CPS_label = Label(info_window, text="Control Info at the top left corner", bg="black", fg="lawn green", font=("FixedSys", 16))
CPS_label.grid(columnspan=2, row=5)



# Button command
def understood():
    info_window.destroy()

# Button frame
frame = Frame(info_window, highlightbackground="lawn green",
              highlightcolor="lawn green",
              highlightthickness=3,
              bd=0)
frame.grid(columnspan=2, row=6)

#Button
confirm_button = Button(frame,
                        text="Understood?",
                        bg="black", 
                        fg="lawn green",
                        font=("FixedSys", 25),
                        activebackground="black",
                        activeforeground="lawn green",
                        highlightbackground="lawn green",
                        command=understood)
confirm_button.grid(columnspan=2, row=5)

# Remove the window border to make it less obtrusive
info_window.overrideredirect(True)

# Keep the window always on top
info_window.attributes("-topmost", True)

info_window.mainloop()