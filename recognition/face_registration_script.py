# v_working_0.8.1 (Using GUI_LAYOUT.PY)

import cv2
import os
import sys
import tkinter as tk
from tkinter import Label, Entry
from PIL import Image, ImageTk
import pickle
import face_recognition
import customtkinter
import ttkbootstrap as ttk
from gui.gui_layout import *
from PIL import Image

# Constants
FACES_DIR = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/data/faces"
ENCODINGS_FILE = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/data/knownDatasetEncodings/encodings.pkl"
IMAGE_PATH = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/skull_2.png"

# GUI Styling Variables
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
title_bar_button_hover = '#3e4042'
name_label_text = "Enter your name:"
name_label_font = ("Urbanist-Thin", 14)
start_button_text = "Start Registration"
instruction_label_font = ("Urbanist-Thin", 14)
prompt_label_font = ("Urbanist-Thin", 12)
prompt_label_fg = "aliceblue"
video_label_text = "Face Registration App"
video_label_font = ("Urbanist-Thin", 20)

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


# Functionalities

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


# Program specific functions - Face Registration
def process_new_faces():
    """Processes new faces from the dataset and saves encodings to a file."""
    print("[INFO] Processing new faces...")
    encodings, names = [], []

    for folder_name in os.listdir(FACES_DIR):
        folder_path = os.path.join(FACES_DIR, folder_name)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith((".jpg", ".png", ".jpeg")):
                    img_path = os.path.join(folder_path, filename)
                    try:
                        image = face_recognition.load_image_file(img_path)
                        encoding = face_recognition.face_encodings(image)
                        if not encoding:
                            print(f"[WARNING] No face found in {img_path}, skipping...")
                            continue  # Skip images without detected faces
                        encodings.append(encoding[0])
                        names.append(folder_name)
                    except Exception as e:
                        print(f"[ERROR] Could not process image {img_path}: {e}")

    # Save encodings to file
    os.makedirs(os.path.dirname(ENCODINGS_FILE), exist_ok=True)
    with open(ENCODINGS_FILE, "wb") as file:
        pickle.dump({"encodings": encodings, "names": names}, file)

    print(f"[INFO] Saved {len(encodings)} face encodings.")
    return encodings, names

def start_registration():
    """Starts face registration and initializes webcam feed."""
    global name, save_path, cap, count
    name = name_entry.get()
    if not name:
        instruction_label.configure(text="Please enter your name.")
        return

    save_path = os.path.join(FACES_DIR, name)
    os.makedirs(save_path, exist_ok=True)

    # Hide entry and start button
    name_entry.pack_forget()
    name_label.pack_forget()
    start_button.pack_forget()

    # Resize and center the window
    root.geometry("1000x800")
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    update_frame()

def update_frame():
    """Continuously updates the video feed in the UI."""
    ret, frame = cap.read()
    if ret:
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.config(image=imgtk)
        instruction_label.configure(text=instructions[count])
        prompt_label.configure(text="Press Enter to capture picture")

    if cap.isOpened():
        root.after(10, update_frame)

def capture_image(event=None):
    """Captures the current frame and saves it as an image."""
    global count
    if cap and cap.isOpened():
        ret, frame = cap.read()
        if ret:
            file_path = os.path.join(save_path, f"{name}_{count + 1}.jpg")
            cv2.imwrite(file_path, frame)
            count += 1

            if count >= 6:
                process_new_face_encodings()  # Call the function to update encodings
                show_completion_buttons()
            else:
                instruction_label.configure(text=instructions[count])

def process_new_face_encodings():
    """Updates the known encodings after registering a new face."""
    instruction_label.configure(text="Updating face database... Please wait.")
    root.update()  # Force UI update before processing
    process_new_faces()  # Call function to process faces
    instruction_label.configure(text="Face database updated successfully!")

def show_completion_buttons():
    """Displays buttons for returning to the app or registering another face."""
    instruction_label.configure(text="Face Registration Completed!")
    prompt_label.configure(text="")  # Remove "Press Enter" prompt

    return_button = custom_layout_create_button("Return To App", return_to_app, pady=10)
    new_face_button = custom_layout_create_button("Register New Face", reset_registration, pady=10)

def return_to_app():
    """Closes the registration window without launching a new instance."""
    cap.release()  # Release camera when closing
    cv2.destroyAllWindows()
    root.destroy()  # Just close the window, don't relaunch the app

def reset_registration():
    """Resets the registration UI for a new user."""
    global count
    count = 0
    instruction_label.configure(text="")
    prompt_label.configure(text="")
    video_label.config(image="")
    name_entry.pack(pady=5)
    name_label.pack(pady=10)
    start_button.pack(pady=10)


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

my_close_icon_src = Image.open("C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/x.png")
my_close_icon = ImageTk.PhotoImage(my_close_icon_src.resize((20, 20)))

my_max_icon_src = Image.open("C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/max.png")
my_max_icon = ImageTk.PhotoImage(my_max_icon_src.resize((20, 20)))

my_min_icon_src = Image.open("C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/minus.png")
my_min_icon = ImageTk.PhotoImage(my_min_icon_src.resize((20, 20)))

my_minimise_icon_src = Image.open("C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/min.png")
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
close_button.pack(side=RIGHT,   ipadx=14, ipady=10)
expand_button.pack(side=RIGHT,  ipadx=14, ipady=10)
minimize_button.pack(side=RIGHT,ipadx=14, ipady=10)
title_bar_title.pack(side=TOP, pady=10, anchor="center")

# Add title text above buttons
main_text = customtkinter.CTkLabel(root, text=video_label_text, font=video_label_font, text_color=button_fg)
main_text.pack(pady=(25, 25))

name_label = customtkinter.CTkLabel(root, text=name_label_text, font=name_label_font, text_color=button_fg)
name_label.pack(pady=10)

name_entry = Entry(root, font=name_label_font)
name_entry.pack(pady=5)

start_button = custom_layout_create_button(root, start_button_text, start_registration, font_style, button_bg, button_fg, button_hover_bg, button_border, pady=(15, 15))

instruction_label = customtkinter.CTkLabel(root, text="", font=instruction_label_font, text_color=button_fg)
instruction_label.pack(pady=10)

prompt_label = customtkinter.CTkLabel(root, text="", font=prompt_label_font, text_color=prompt_label_fg)
prompt_label.pack(pady=5)

video_label = Label(root)
video_label.pack()

# Image at the bottom right
image = Image.open(IMAGE_PATH)
image = image.resize((20, 20), Image.Resampling.LANCZOS)
image_tk = customtkinter.CTkImage(light_image=image, dark_image=image, size=(20, 20))

image_label = customtkinter.CTkLabel(root, image=image_tk, text="")
image_label.image = image_tk  # Keep a reference to avoid garbage collection
image_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Position at bottom right with some padding

instructions = [
    "Look straight at the camera",
    "Turn slightly to your left",
    "Turn slightly to your right",
    "Look up slightly",
    "Look down slightly",
    "Smile!"
]
count = 0
save_path = ""


# Center the window on the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

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

root.mainloop()