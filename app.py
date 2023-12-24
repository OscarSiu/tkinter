# A python tkinter gui window for Drone Ground Sampling Distance calculation 
# Author: Oscar Siu 

import tkinter as tk
#import os

# Create the main window and frame
window = tk.Tk()
window.title('Yinspectica v0.1')
window.geometry('600x400')
#window.configure(background='white')

def only_numbers(char):
 return char.replace(".", "0", 1).isdigit()

def cal():
    default_dis = 3
    gsd = float(height_entry.get())
    dis = float(weight_entry.get())
  
    new_gsd = gsd * dis /default_dis

    result = 'New GSD: {:.2f}'.format(new_gsd) + ' (mm/pixel)'
    result_label.configure(text=result,font = 'Arial', fg = 'red')

# Add elements into frame
label = tk.Label(window, text='GSD Calculator', font =('Arial',18), anchor = 'w')
label.pack(side=tk.TOP, pady=30)

# "Sample GSD" group
height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)

height_label = tk.Label(height_frame, width = 22, text='Sample GSD (mm/pixel): ', font =('Arial',12), anchor = 'w')
height_label.pack(side=tk.LEFT)

validation = height_frame.register(only_numbers)
height_entry = tk.Entry(height_frame, validate= 'key', validatecommand=(validation, '%S'))
height_entry.pack(side=tk.RIGHT)

# "Working distance" group
weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)

weight_label = tk.Label(weight_frame, text='Working distance (m): ',font = ('Arial', 12), anchor = 'w')
weight_label.pack(side=tk.LEFT, padx = 20, pady = 30)

validation = weight_frame.register(only_numbers)
weight_entry = tk.Entry(weight_frame, validate='key', validatecommand=(validation, '%S'))
weight_entry.pack(side=tk.RIGHT)


# Button
calculate_btn = tk.Button(window, text='Calculate', font = ('Arial', 12), command=cal)
calculate_btn.pack(pady = 5)


# Show result
result_label = tk.Label(window, font = 14)
result_label.pack(ipady= 20)


# event handler
def echo_hello():
    exit()


# Bottom group
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)
# call event handler to exit the window when the button is pressed
bottom_button = tk.Button(bottom_frame, text='Back', fg='black', command=echo_hello)
bottom_button.pack(side=tk.BOTTOM)

# Run code
window.mainloop()