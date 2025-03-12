import cv2
import os
import sys
import threading
import tkinter as tk
from tkinter import Label
import pickle
import face_recognition
import customtkinter
import numpy as np
from gui.gui_layout import *
from PIL import Image
from PIL import ImageTk

# Retrieve theme colors from gui_layout.py
(title_label_text, window_size, window_bg, button_bg, button_fg, button_border, button_hover_bg, title_bar_bg, title_bar_fg, main_text_fg, title_bar_close_button_hover, title_bar_button_hover, general_images_path) = retrive_theme_colors()

# Constants
FACES_DIR = os.path.join(general_images_path,"data/faces")
ENCODINGS_FILE = os.path.join(general_images_path,"data/knownDatasetEncodings/encodings.pkl")

# GUI Styling Variables
window_size = (900, 700)
video_label_text = "Face Registration App"
video_label_font = ("Urbanist-Thin", 20)

# Global variables
skull_image_path = os.path.join(general_images_path, "res/skull_2.png")
close_icon_path = os.path.join(general_images_path, "res/x.png")
minimize_icon_path = os.path.join(general_images_path, "res/min.png")
max_icon_path = os.path.join(general_images_path, "res/max.png")
min_icon_path = os.path.join(general_images_path, "res/minus.png")

running = True
frame_count = 0
PROCESS_EVERY_N_FRAMES = 3  # Process every frame
recognized_face = {}  # Stores recognized faces
recognized_face_lock = threading.Lock()  # Thread-safe lock
recognized_face_colour = (255, 172, 166)  # Rectangle color

# Get camera index from command-line arguments
camera_index = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# Shared camera instance
cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    print("[ERROR] Cannot access webcam with index", camera_index)
    print("[INFO] Trying to access the default camera.")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot access the default webcam.")
        sys.exit()

print("[INFO] Using shared camera for face recognition.")


# GUI Functionalities

def set_appwindow(mainWindow): 
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)   
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())

def deminimize(event):
    # root.focus() 
    root.attributes("-alpha", 2)
    if root.minimized == True:
        root.minimized = False        

def minimize_me():
    root.after(10, lambda: fade_out(root))

def maximize_me():
    if root.maximized == False:
        root.normal_size = root.geometry()
        expand_button.config(text=" 🗗 ", image=my_minimise_icon)
        root.after(10, lambda: fade_out(root))
        root.after(200, lambda: root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()-40}+0+0"))
        root.after(300, lambda: fade_in(root))
        root.maximized = not root.maximized 
    else:
        expand_button.config(text=" 🗖 ", image=my_max_icon)
        root.after(10, lambda: fade_out(root))
        root.after(200, lambda: root.geometry(root.normal_size))
        root.after(300, lambda: fade_in(root))
        root.maximized = not root.maximized

def fade_out(widget):
    alpha = widget.attributes("-alpha")
    if alpha > 0:
        alpha -= 0.1
        widget.attributes("-alpha", alpha)
        widget.after(10, lambda: fade_out(widget))

def fade_in(widget):
    alpha = widget.attributes("-alpha")
    if alpha < 1:
        alpha += 0.1
        widget.attributes("-alpha", alpha)
        widget.after(10, lambda: fade_in(widget))

def fade_out_close(widget):
    alpha = widget.attributes("-alpha")
    if alpha > 0:
        alpha -= 0.4
        widget.attributes("-alpha", alpha)
        widget.after(10, lambda: fade_out(widget))
    
    root.destroy()

def changex_on_hovering(event):
    global close_button
    close_button['bg']=title_bar_close_button_hover    
    
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=title_bar_bg
    
def change_size_on_hovering(event):
    global expand_button
    expand_button['bg']=title_bar_button_hover
    
def return_size_on_hovering(event):
    global expand_button
    expand_button['bg']=title_bar_bg
    
def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=title_bar_button_hover
    
def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=title_bar_bg
    
def get_pos(event):
    if root.maximized == False:
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root
        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event):
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

        def release_window(event):
            root.config(cursor="arrow")
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        expand_button.config(text=" 🗖 ")
        root.maximized = not root.maximized


# Program specific functions - Load known faces
def load_known_faces():
    if not os.path.exists(ENCODINGS_FILE):
        print("[INFO] No saved encodings found. Returning empty lists.")
        return [], []
    with open(ENCODINGS_FILE, "rb") as file:
        data = pickle.load(file)
    print(f"[INFO] Loaded {len(data['encodings'])} known faces from file.")
    return data["encodings"], data["names"]

known_encodings, known_names = load_known_faces()

def process_faces():
    """Threaded function to process Feed1 (Face Recognition)."""
    global cap, frame_count, recognized_face
    while running:
        ret, frame = cap.read()
        if not ret:
            continue

        frame_count += 1
        if frame_count % PROCESS_EVERY_N_FRAMES == 0:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            with recognized_face_lock:
                recognized_face.clear()  # Clear previous face data

                for encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
                    matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.4)
                    name = "Unknown"

                    if True in matches:
                        match_index = np.argmin(face_recognition.face_distance(known_encodings, encoding))
                        name = known_names[match_index]

                    top, right, bottom, left = [v * 4 for v in (top, right, bottom, left)]
                    recognized_face[name] = (left, top, right, bottom)

def update_feed():
    """Continuously updates Feed2 (GUI Display) with smooth rendering."""
    global cap

    if not cap.isOpened() or not running:
        return

    ret, frame = cap.read()
    if not ret:
        return

    # Draw face rectangles from Feed1 (Processed Feed) onto Feed2 (GUI Display)
    with recognized_face_lock:
        for name, (left, top, right, bottom) in recognized_face.items():
            cv2.rectangle(frame, (left, top), (right, bottom), recognized_face_colour, 2)
            cv2.putText(frame, f"{name}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, recognized_face_colour, 2)
    
    update_frame(frame)
    root.after(10, update_feed)

def update_frame(frame):
    """Converts OpenCV frame to Tkinter-compatible format."""
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    img = img.resize((800, 600))
    img_tk = ImageTk.PhotoImage(image=img)
    
    canvas.img_tk = img_tk
    canvas.configure(image=img_tk)


# GUI components
root = Tk()
root.title(title_label_text)
root.overrideredirect(True)
root.resizable(True, True)  # Allow window resizing in both directions

win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()
root.geometry(window_size)
root.minimized = False 
root.maximized = False 

root.config(bg=window_bg)
title_bar = Frame(root, bg=title_bar_bg, relief='raised', bd=0,highlightthickness=0)

my_close_icon_src = Image.open(close_icon_path)
my_close_icon = ImageTk.PhotoImage(my_close_icon_src.resize((20, 20)))

my_max_icon_src = Image.open(max_icon_path)
my_max_icon = ImageTk.PhotoImage(my_max_icon_src.resize((20, 20)))

my_min_icon_src = Image.open(min_icon_path)
my_min_icon = ImageTk.PhotoImage(my_min_icon_src.resize((20, 20)))

my_minimise_icon_src = Image.open(minimize_icon_path)
my_minimise_icon = ImageTk.PhotoImage(my_minimise_icon_src.resize((20, 20)))

Label(title_bar, bg=title_bar_bg).pack(side=LEFT, padx=5)

close_button = Button(title_bar, text=' × ', command=lambda: fade_out_close(root),bg=title_bar_bg,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',
                    highlightthickness=0, image=my_close_icon, activebackground=title_bar_bg)
expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=title_bar_bg,padx=2,pady=0,bd=0,fg='white',font=("calibri", 13),
                    highlightthickness=0, image=my_max_icon, activebackground=title_bar_bg)
minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=title_bar_bg,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),
                    highlightthickness=0, image=my_min_icon, activebackground=title_bar_bg)
title_bar_title = customtkinter.CTkLabel(title_bar, text=title_label_text, font=("Urbanist-Thin", 14), text_color=title_bar_fg)

# Add All the gui items
title_bar.pack(fill=X)
close_button.pack(side=RIGHT, ipadx=14, ipady=10)
expand_button.pack(side=RIGHT, ipadx=14, ipady=10)
minimize_button.pack(side=RIGHT, ipadx=14, ipady=10)
title_bar_title.pack(side=TOP, pady=10, anchor="w")

# Add title text above buttons
main_text = customtkinter.CTkLabel(root, text=video_label_text, font=video_label_font, text_color=main_text_fg)
main_text.pack(pady=(25, 25))

canvas = tk.Label(root)
canvas.pack()

cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("[ERROR] Cannot open webcam.")
    root.destroy()
    sys.exit()

cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Image at the bottom right
image = Image.open(skull_image_path)
image = image.resize((20, 20), Image.Resampling.LANCZOS)
image_tk = customtkinter.CTkImage(light_image=image, dark_image=image, size=(20, 20))

image_label = customtkinter.CTkLabel(root, image=image_tk, text="", text_color=main_text_fg)
image_label.image = image_tk  # Keep a reference to avoid garbage collection
image_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Position at bottom right with some padding

# Center the window on the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')


# Start the face processing thread
threading.Thread(target=process_faces, daemon=True).start()

# Start the GUI update loop
update_feed()

title_bar.bind('<Button-1>', get_pos)
title_bar_title.bind('<Button-1>', get_pos) 
close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)
expand_button.bind('<Enter>', change_size_on_hovering)
expand_button.bind('<Leave>', return_size_on_hovering)
minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)

root.bind("<FocusIn>", deminimize)
root.after(10, lambda: set_appwindow(root))
root.bind("<Control-q>", lambda event: root.destroy())

# Run the Tkinter main loop
root.mainloop()

running = False
print("[INFO] Application closed.")