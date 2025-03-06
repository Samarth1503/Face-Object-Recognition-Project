# import tkinter as tk
# from tkinter import Label
# from PIL import Image, ImageTk
# import customtkinter
# import ttkbootstrap as ttk
# from gui_layout import apply_gui_layout  # Import the function from gui_layout.py

# # Apply modern UI styling
# title_label_text = "Test GUI Layout"
# window_size = "600x400"
# window_bg = "#000000"
# font_style = ("Urbanist-Thin", 14)
# button_bg = "#000000"  # Button background
# button_fg = "#C8C8F2"  # Light purple text
# button_border = "#C8C8F2"  # Light purple border
# button_hover_bg = "#2a2633"  # Darker hover effect
# title_bar_bg = "#1A1A1A"  # Title bar background color
# title_bar_fg = "#C8C8F2"  # Title bar font color
# title_bar_font_color = "#D0BCFF"  # Title bar font color

# # Initialize Tkinter GUI with ttkbootstrap
# root = ttk.Window(themename="darkly")

# # Apply the GUI layout
# title_bar, title_label = apply_gui_layout(
#     root, title_label_text, window_size, window_bg, font_style,
#     button_bg, button_fg, button_border, button_hover_bg,
#     title_bar_bg, title_bar_fg, title_bar_font_color
# )

# # Add title text above buttons
# title_label = Label(root, text="Test GUI Layout", font=("Urbanist-Thin", 20), bg=window_bg, fg=title_bar_font_color)
# title_label.pack(pady=(25, 25))  # Add margin at the top

# # Function to create a simple button
# def create_button(text, command, pady):
#     btn = customtkinter.CTkButton(
#         root,
#         text=text,
#         command=command,
#         font=font_style,
#         fg_color=button_bg,
#         text_color=button_fg,
#         hover_color=button_hover_bg,
#         border_color=button_border,
#         border_width=1,
#         corner_radius=10,  # Rounded corners
#         width=200,
#         height=50
#     )
#     btn.pack(pady=pady)  # Add vertical spacing
#     return btn

# # Function to close the window
# def close_window():
#     root.destroy()

# # Create a simple button to close the window
# close_button = create_button("Close", close_window, pady=(15, 15))

# # Run the GUI
# root.mainloop()







import tkinter as tk

# Ensure it appears in the taskbar (Windows only)
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myapsp")

root = tk.Tk()
root.geometry("600x400")
root.configure(bg="#000000")  # Set custom background
# root.overrideredirect(True)  # Hide default title bar

# # # --- Custom Title Bar ---
# # title_bar = tk.Frame(root, bg="#1A1A1A", relief="raised", bd=1, height=30)
# # title_bar.pack(fill=tk.X)

# # # Title label
# # title_label = tk.Label(title_bar, text="Custom Title Bar", fg="#C8C8F2", bg="#1A1A1A", font=("Urbanist-Thin", 12))
# # title_label.pack(side=tk.LEFT, padx=10)

# # --- Window Controls ---
# def close_window():
#     root.destroy()

# def minimize_window():
#     root.overrideredirect(False)  # Temporarily allow OS control
#     root.iconify()  # Minimize
#     root.after(10, lambda: root.overrideredirect(True))  # Restore custom title bar when reopened

# def toggle_maximize():
#     if root.state() == "zoomed":
#         root.state("normal")
#     else:
#         root.state("zoomed")

# # Close Button
# close_button = tk.Button(root, text="X", bg="#C8C8F2", fg="#000000", command=close_window, bd=0)
# close_button.pack(side=tk.RIGHT, padx=5)

# # Minimize Button
# minimize_button = tk.Button(root, text="─", bg="#C8C8F2", fg="#000000", command=minimize_window, bd=0)
# minimize_button.pack(side=tk.RIGHT, padx=5)

# # Maximize Button
# maximize_button = tk.Button(root, text="□", bg="#C8C8F2", fg="#000000", command=toggle_maximize, bd=0)
# maximize_button.pack(side=tk.RIGHT, padx=5)

# # --- Make Window Draggable ---
# def start_move(event):
#     root.x = event.x
#     root.y = event.y

# def move_window(event):
#     x = root.winfo_x() + (event.x - root.x)
#     y = root.winfo_y() + (event.y - root.y)
#     root.geometry(f"+{x}+{y}")

# title_bar.bind("<Button-1>", start_move)
# title_bar.bind("<B1-Motion>", move_window)

root.mainloop()
