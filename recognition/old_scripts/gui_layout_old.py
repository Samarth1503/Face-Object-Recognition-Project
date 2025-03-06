# import tkinter as tk
# from tkinter import Label
# from PIL import Image, ImageTk
# import customtkinter
# import ttkbootstrap as ttk

# def apply_gui_layout(root, title_label_text, window_size, window_bg, font_style, button_bg, button_fg, button_border, button_hover_bg, title_bar_bg, title_bar_fg, title_bar_font_color):
#     root.title(title_label_text)
#     root.geometry(window_size)
#     root.configure(bg=window_bg)

#     # Remove the default title bar
#     root.overrideredirect(True)

#     # Create a custom title bar
#     title_bar = tk.Frame(root, bg=title_bar_bg, relief='raised', bd=2)
#     title_bar.pack(fill=tk.X)

#     # Add title text to the custom title bar
#     title_label = Label(title_bar, text=title_label_text, font=("Urbanist-Thin", 10), fg=title_bar_fg, bg=title_bar_bg)
#     title_label.pack(side=tk.LEFT, padx=10)

#     # Load images for the buttons
#     close_image_path = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/close.jpg"
#     minimize_image_path = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/maximize.jpg"

#     close_image = Image.open(close_image_path)
#     minimize_image = Image.open(minimize_image_path)

#     close_image = close_image.resize((20, 20), Image.Resampling.LANCZOS)
#     minimize_image = minimize_image.resize((20, 20), Image.Resampling.LANCZOS)

#     close_image_tk = ImageTk.PhotoImage(close_image)
#     minimize_image_tk = ImageTk.PhotoImage(minimize_image)

#     # Keep a reference to the images to prevent garbage collection
#     root.close_image_tk = close_image_tk
#     root.minimize_image_tk = minimize_image_tk

#     # Function to close the window
#     def close_window():
#         root.destroy()

#     # Function to minimize the window
#     def minimize_window():
#         root.overrideredirect(False)
#         if root.attributes('-fullscreen'):
#             root.attributes('-fullscreen', False)
#         else:
#             root.attributes('-fullscreen', True)
#         root.overrideredirect(True)

#     # Add minimize and close buttons to the custom title bar
#     close_button = tk.Button(title_bar, image=close_image_tk, command=close_window, bg=title_bar_bg, fg=title_bar_fg, relief='flat', activebackground=title_bar_bg)
#     close_button.pack(side=tk.RIGHT, padx=5)

#     minimize_button = tk.Button(title_bar, image=minimize_image_tk, command=minimize_window, bg=title_bar_bg, fg=title_bar_fg, relief='flat', activebackground=title_bar_bg)
#     minimize_button.pack(side=tk.RIGHT, padx=5)

#     # Function to move the window
#     def move_window(event):
#         root.geometry(f'+{event.x_root}+{event.y_root}')

#     # Bind the title bar to the move function
#     title_bar.bind('<B1-Motion>', move_window)

#     return title_bar, title_label


# # Function to create modern buttons
# def custom_layout_create_button(root, text, command, font_style, button_bg, button_fg, button_hover_bg, button_border, pady):
#     btn = customtkinter.CTkButton(
#         master=root,
#         text=text,
#         command=command,
#         font=font_style,
#         fg_color=button_bg,
#         text_color=button_fg,
#         hover_color=button_hover_bg,
#         border_color=button_border,
#         border_width=1,
#         corner_radius=10,
#         width=200,
#         height=50
#     )
#     btn.pack(pady=pady)  # Add vertical spacing
#     return btn






# import tkinter as tk
# from tkinter import Label
# from PIL import Image
# import customtkinter
# import ttkbootstrap as ttk


# def apply_gui_layout(root, title_label_text, window_size, window_bg, font_style, button_bg, button_fg, button_border, button_hover_bg, title_bar_bg, title_bar_fg, title_bar_font_color):
#     root.title(title_label_text)
#     root.geometry(window_size)
#     root.configure(bg=window_bg)
    
#     # Ensure the window is visible in the taskbar
#     root.attributes('-topmost', False)  # Allow normal window stacking
#     root.attributes('-toolwindow', False)  # Ensure it appears in the taskbar
#     root.attributes('-fullscreen', False)  # Prevent fullscreen lock
#     root.overrideredirect(False)  # Allow OS to manage the window

#     # Remove the default title bar
#     root.overrideredirect(True)

#     # Create a custom title bar
#     title_bar = customtkinter.CTkFrame(root, bg_color=title_bar_bg, border_width=1)
#     title_bar.pack(fill=tk.X)

#     # Add title text to the custom title bar
#     title_label = customtkinter.CTkLabel(master=title_bar, text=title_label_text, font=("Urbanist-Thin", 12), text_color=title_bar_fg)
#     title_label.pack(side=tk.LEFT, padx=10, pady=0)

#     # Load images for the buttons
#     close_image_path = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/close.jpg"
#     minimize_image_path = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/maximize.jpg"

#     close_image = Image.open(close_image_path)
#     minimize_image = Image.open(minimize_image_path)

#     close_image = close_image.resize((20, 20), Image.Resampling.LANCZOS)
#     minimize_image = minimize_image.resize((20, 20), Image.Resampling.LANCZOS)

#     close_image_tk = customtkinter.CTkImage(light_image=close_image, dark_image=close_image, size=(20, 20))
#     minimize_image_tk = customtkinter.CTkImage(light_image=minimize_image, dark_image=minimize_image, size=(20, 20))

#     # Keep a reference to the images to prevent garbage collection
#     root.close_image_tk = close_image_tk
#     root.minimize_image_tk = minimize_image_tk

#     # Function to close the window
#     def close_window():
#         root.destroy()

#     # Function to minimize the window
#     def minimize_window():
#         root.overrideredirect(False)
#         if root.attributes('-fullscreen'):
#             root.attributes('-fullscreen', False)
#         else:
#             root.attributes('-fullscreen', True)
#         root.overrideredirect(True)

#     # Add minimize and close buttons to the custom title bar
#     close_button = customtkinter.CTkLabel(title_bar, image=close_image_tk, text="")
#     close_button.bind("<Button-1>", lambda e: close_window())
#     close_button.pack(side=tk.RIGHT, padx=0, pady=0)

#     minimize_button = customtkinter.CTkLabel(title_bar, image=minimize_image_tk, text="")
#     minimize_button.bind("<Button-1>", lambda e: minimize_window())
#     minimize_button.pack(side=tk.RIGHT, padx=2, pady=0)

#     # Function to move the window
#     def move_window(event):
#         root.geometry(f'+{event.x_root}+{event.y_root}')

#     # Bind the title bar to the move function
#     title_bar.bind('<B1-Motion>', move_window)

#     return title_bar, title_label


# # Function to create modern buttons
# def custom_layout_create_button(root, text, command, font_style, button_bg, button_fg, button_hover_bg, button_border, pady):
#     btn = customtkinter.CTkButton(
#         master=root,
#         text=text,
#         command=command,
#         font=font_style,
#         fg_color=button_bg,
#         text_color=button_fg,
#         hover_color=button_hover_bg,
#         border_color=button_border,
#         border_width=1,
#         corner_radius=10,
#         width=200,
#         height=50
#     )
#     btn.pack(pady=pady)  # Add vertical spacing
#     return btn



























