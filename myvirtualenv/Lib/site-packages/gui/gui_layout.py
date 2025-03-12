# v_0.5

from tkinter import *
import customtkinter
import ttkbootstrap as ttk
from ctypes import windll

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

def retrive_theme_colors():
    return title_label_text, window_size, window_bg, button_bg, button_fg, button_border, button_hover_bg, title_bar_bg, title_bar_fg, title_bar_font_color, title_bar_close_button_hover, title_bar_button_hover, general_path

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