# v_0.5

from tkinter import *
import customtkinter
import ttkbootstrap as ttk
from ctypes import windll

# Apply modern UI styling
title_label_text = "Face & Object Recognition App"
window_size = "600x400"
font_style = ("Urbanist-Thin", 14)
general_path = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/"

# Colors
window_bg = "#3D63A9"  # Window background 
button_bg = "#B7D0FF"  # Button background
button_fg = "#202020"  # Button text
button_hover_bg = "#99BDFF"  # Darker hover effect
button2_bg = "#DCCCFF"  # Button background
button2_hover_bg = "#D0BCFF"  # Button hover effect
button_border = "#FFFFFF"  # Light purple border
title_bar_bg = "#E5FF00"  # Title bar background color
title_bar_fg = "#000000"  # Title bar font color
main_text_fg = "#FFF4BD"  # Title bar font color
title_bar_close_button_hover = 'red'  # Red close button background color
title_bar_button_hover = '#3e4042' # Hover effect for title bar buttons

# Dark Theme - Colors
# window_bg = "#000000"  # Window background 
# button_bg = "#000000"  # Button background
# button_fg = "#C8C8F2"  # Light purple text
# button_hover_bg = "#2a2633"  # Darker hover effect
# button2_bg = "#000000"  # Button background
# button2_hover_bg = "#2a2633"  # Button hover effect
# button_border = "#C8C8F2"  # Light purple border
# title_bar_bg = "#1A1A1A"  # Title bar background color
# title_bar_fg = "#C8C8F2"  # Title bar font color
# main_text_fg = "#D0BCFF"  # Title bar font color
# title_bar_close_button_hover = 'red'  # Red close button background color
# title_bar_button_hover = '#3e4042' # Hover effect for title bar buttons

def retrive_theme_colors():
    return title_label_text, window_size, window_bg, button_bg, button_fg, button_border, button_hover_bg, title_bar_bg, title_bar_fg, main_text_fg, title_bar_close_button_hover, title_bar_button_hover, general_path

def retrive_extra_theme_colors():
    return button2_bg, button2_hover_bg

def custom_layout_create_button(root, text, command, font_style, button_bg, button_fg, button_hover_bg, button_border, pady):
    btn = customtkinter.CTkButton(
        master=root,
        text=text,
        command=command,
        font=font_style,
        fg_color=button_bg,
        text_color=button_fg,
        hover_color=button_hover_bg,
        border_color=button_border,
        border_width=1,
        corner_radius=10,
        width=200,
        height=50
    )
    btn.pack(pady=pady)  # Add vertical spacing
    return btn