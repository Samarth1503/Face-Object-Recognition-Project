# v_0.5

from tkinter import *
import customtkinter
import ttkbootstrap as ttk
from ctypes import windll

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