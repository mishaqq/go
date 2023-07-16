import tkinter 
from tkinter import ttk
from tkinter import messagebox

board_size = 9
handicap = 0
komi = 0
board_style = "·"

def enter_data():
    
    global board_size
    global komi
    global handicap
    global board_style
    board_size = board_size_combobox.get()
    handicap = handicap_combobox.get()
    komi = komi_combobox.get()
    board_style = board_style_combobox.get()



    if int(board_size) == 9 and int(handicap) > 0:
        tkinter.messagebox.showwarning(title="Handicap to big for 9x9!", message="Choose other handicap.")
    else:
        window.destroy()
            
           
   

window = tkinter.Tk()
window.title("Go v1.0")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_settings_frame =tkinter.LabelFrame(frame, text="Game Settings")
user_settings_frame.grid(row= 0, column=0, padx=20, pady=10)



board_size_label = tkinter.Label(user_settings_frame, text="Board Size")
board_size_combobox = ttk.Combobox(user_settings_frame, values=[9, 13 ,19])
board_size_label.grid(row=0, column=0)
board_size_combobox.current(0)
board_size_combobox.grid(row=1, column=0)

handicap_label = tkinter.Label(user_settings_frame, text="Handicap")
handicap_combobox = ttk.Combobox(user_settings_frame, values=[0,1,2,3,4,5])
handicap_label.grid(row=0, column=1)
handicap_combobox.current(0)
handicap_combobox.grid(row=1, column=1)

komi_label = tkinter.Label(user_settings_frame, text="Komi")
komi_combobox = ttk.Combobox(user_settings_frame, values=[0,3.5, 4.5, 5.5, 6.5])
komi_label.grid(row=0, column=2)
komi_combobox.current(0)
komi_combobox.grid(row=1, column=2)



board_style_label = tkinter.Label(user_settings_frame, text="Board Style")
board_style_combobox = ttk.Combobox(user_settings_frame, values=[ "·","*"])
board_style_combobox.current(0)
board_style_label.grid(row=2, column=1)
board_style_combobox.grid(row=3, column=1)

for widget in user_settings_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



# Button
button = tkinter.Button(frame, text="Start!", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()