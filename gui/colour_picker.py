import customtkinter
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

color_selected = ""

root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('300x150')
root.configure(bg='#d2e9ff')
def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    print (colors[1])
    root.configure(bg=colors[1])

main_text1 = customtkinter.CTkLabel(root, text="Face Recognition App", font=("Urbanist-Thin", 20), text_color="#d9b3ff")
main_text1.pack(pady=(25, 25))
ttk.Button(root, text='Select a Color', command=change_color).pack(expand=True)

root.mainloop()

'''
blue bg
#3d63a9

#21538f

light blue
#d2e9ff

pink
#d9b3ff




bg
3d63a9

title text
FFF4BD

btn
E0C1FF

btn hover
D6AEFF

btn text
000000






# Apply modern UI styling
title_label_text = "Face & Object Recognition App"
window_size = "600x400"
window_bg = "#000000"
font_style = ("Urbanist-Thin", 14)
button_bg = "#000000"  # Button background
button_fg = "#C8C8F2"  # Light purple text
button_border = "#C8C8F2"  # Light purple border
button_hover_bg = "#2a2633"  # Darker hover effect
title_bar_bg = "#1A1A1A"  # Title bar background color
title_bar_fg = "#C8C8F2"  # Title bar font color
title_bar_font_color = "#D0BCFF"  # Title bar font color
title_bar_close_button_hover = 'red'  # Red close button background color
title_bar_button_hover = '#3e4042' # Hover effect for title bar buttons
general_path = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/"

'''