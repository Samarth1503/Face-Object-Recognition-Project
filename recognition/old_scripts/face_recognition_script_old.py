# v_Working_0.8

# import os
# import sys
# import cv2
# import face_recognition
# import numpy as np
# import threading
# import tkinter as tk
# from tkinter import Label
# from PIL import Image, ImageTk
# import pickle

# # Constants
# PROCESS_EVERY_N_FRAMES = 1  # Process every frame
# FACES_DIR = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/data/faces"
# ENCODINGS_FILE = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/data/knownDatasetEncodings/encodings.pkl"

# # Get camera index from command-line arguments
# camera_index = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# # Function to load known face encodings and names
# def load_known_faces():
#     """Loads known face encodings and names from a file."""
#     if not os.path.exists(ENCODINGS_FILE):
#         print("[INFO] No saved encodings found. Returning empty lists.")
#         return [], []
    
#     with open(ENCODINGS_FILE, "rb") as file:
#         data = pickle.load(file)
    
#     print(f"[INFO] Loaded {len(data['encodings'])} known faces from file.")
#     return data["encodings"], data["names"]


# # Global variables
# running = True
# known_encodings, known_names = load_known_faces()
# frame_count = 0
# cap = None  # Single webcam instance
# recognized_face = {}  # Stores recognized faces and their coordinates
# recognized_face_colour = (188, 188, 242)  # Default color for face rectangle


# # Face Recognition GUI
# class FaceRecognitionApp:
#     def __init__(self):
#         global cap

#         self.root = tk.Tk()
#         self.root.title("Face Recognition")
#         self.root.protocol("WM_DELETE_WINDOW", self.on_close)
#         self.root.geometry("800x600")

#         self.canvas = tk.Label(self.root)
#         self.canvas.pack()

#         cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
#         if not cap.isOpened():
#             print("[ERROR] Cannot open webcam.")
#             self.root.destroy()
#             return

#         cap.set(cv2.CAP_PROP_FPS, 30)
#         cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#         self.update_feed()

#     def update_feed(self):
#         global cap, frame_count

#         if not cap.isOpened() or not running:
#             return

#         ret, frame = cap.read()
#         if not ret:
#             return

#         frame_count += 1
#         if frame_count % PROCESS_EVERY_N_FRAMES == 0:
#             frame = self.recognize_faces(frame)

#         self.update_frame(frame)
#         self.root.after(10, self.update_feed)

#     def recognize_faces(self, frame):
#         global recognized_face, recognized_face_colour

#         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#         rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#         face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         for encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
#             matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.4)
#             name = "Unknown"

#             if True in matches:
#                 match_index = np.argmin(face_recognition.face_distance(known_encodings, encoding))
#                 name = known_names[match_index]

#             # Scale coordinates back to original size
#             top, right, bottom, left = [v * 4 for v in (top, right, bottom, left)]
            
#             # Store recognized face data
#             recognized_face[name] = {"coordinates": (left, top, right, bottom)}

#             cv2.rectangle(frame, (left, top), (right, bottom), recognized_face_colour, 2)
#             cv2.putText(frame, f"{name}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, recognized_face_colour, 2)

#         return frame

#     def update_frame(self, frame):
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame_rgb)
#         img = img.resize((800, 600))
#         img_tk = ImageTk.PhotoImage(image=img)

#         self.canvas.img_tk = img_tk
#         self.canvas.configure(image=img_tk)

#     def on_close(self):
#         global running, cap
#         running = False
#         if cap:
#             cap.release()
#         self.root.quit()

#     def run(self):
#         self.root.mainloop()

# # Start the application
# if __name__ == "__main__":
#     app = FaceRecognitionApp()
#     app.run()

#     running = False
#     print("[INFO] Application closed.")














# import cv2
# import os
# import sys
# import threading
# import tkinter as tk
# from tkinter import Label, Entry
# from PIL import Image, ImageTk
# import pickle
# import face_recognition
# import customtkinter
# import numpy as np
# import ttkbootstrap as ttk
# from gui.gui_layout import *


# # Constants
# FACES_DIR = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/data/faces"
# ENCODINGS_FILE = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/data/knownDatasetEncodings/encodings.pkl"
# IMAGE_PATH = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/skull_2.png"

# # GUI Styling Variables
# title_label_text = "Face & Object Recognition App"
# window_size = "1000x800"
# window_bg = "#000000"
# font_style = ("Urbanist-Thin", 14)
# button_bg = "#000000"  # Button background
# button_fg = "#C8C8F2"  # Light purple text
# button_border = "#C8C8F2"  # Light purple border
# button_hover_bg = "#2a2633"  # Darker hover effect
# title_bar_bg = "#1A1A1A"  # Title bar background color
# title_bar_fg = "#C8C8F2"  # Title bar font color
# title_bar_font_color = "#D0BCFF"  # Title bar font color
# video_label_text = "Face Recognition App"
# video_label_font = ("Urbanist-Thin", 20)

# # Get camera index from command-line arguments
# camera_index = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# # Shared camera instance
# cap = cv2.VideoCapture(camera_index)
# if not cap.isOpened():
#     print("[ERROR] Cannot access webcam with index", camera_index)
#     print("[INFO] Trying to access the default camera.")
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("[ERROR] Cannot access the default webcam.")
#         sys.exit()

# print("[INFO] Using shared camera for face recognition.")

# # Load known faces
# def load_known_faces():
#     if not os.path.exists(ENCODINGS_FILE):
#         print("[INFO] No saved encodings found. Returning empty lists.")
#         return [], []
#     with open(ENCODINGS_FILE, "rb") as file:
#         data = pickle.load(file)
#     print(f"[INFO] Loaded {len(data['encodings'])} known faces from file.")
#     return data["encodings"], data["names"]

# # Global Variables
# running = True
# known_encodings, known_names = load_known_faces()
# frame_count = 0
# PROCESS_EVERY_N_FRAMES = 5  # Process every frame
# recognized_face = {}  # Stores recognized faces
# recognized_face_lock = threading.Lock()  # Thread-safe lock
# recognized_face_colour = (255, 172, 166)  # Rectangle color
# image_path = "C:/Users/58008_Rock/Desktop/College/VU/FY Sem 2/Python/FaceObjectRecognitionApp/fontsUsed/skull_2.png"

# # Face Recognition Class
# class FaceRecognitionApp:
#     def __init__(self):
#         global cap
        
#         # Initialize Tkinter GUI with ttkbootstrap
#         self.root = ttk.Window(themename="darkly")
#         self.root.resizable(True, True)  # Allow window resizing in both directions

#         # Apply the GUI layout
#         title_bar, title_label = apply_gui_layout(
#             self.root, title_label_text, window_size, window_bg, font_style,
#             button_bg, button_fg, button_border, button_hover_bg, title_bar_bg, title_bar_fg, title_bar_font_color
#         )

#         # Add title text above buttons
#         main_text = customtkinter.CTkLabel(self.root, text=video_label_text, font=video_label_font, text_color=button_fg)
#         main_text.pack(pady=(25, 25))

#         self.canvas = tk.Label(self.root)
#         self.canvas.pack()

#         cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
#         if not cap.isOpened():
#             print("[ERROR] Cannot open webcam.")
#             self.root.destroy()
#             return

#         cap.set(cv2.CAP_PROP_FPS, 30)
#         cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
#         # Image at the bottom right
#         image = Image.open(IMAGE_PATH)
#         image = image.resize((20, 20), Image.Resampling.LANCZOS)
#         image_tk = customtkinter.CTkImage(light_image=image, dark_image=image, size=(20, 20))

#         image_label = customtkinter.CTkLabel(self.root, image=image_tk, text="")
#         image_label.image = image_tk  # Keep a reference to avoid garbage collection
#         image_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Position at bottom right with some padding

#         # Center the window on the screen
#         self.root.update_idletasks()
#         width = self.root.winfo_width()
#         height = self.root.winfo_height()
#         x = (self.root.winfo_screenwidth() // 2) - (width // 2)
#         y = (self.root.winfo_screenheight() // 2) - (height // 2)
#         self.root.geometry(f'{width}x{height}+{x}+{y}')

#         threading.Thread(target=self.process_faces, daemon=True).start()
#         self.update_feed()
    
#     def process_faces(self):
#         """Threaded function to process Feed1 (Face Recognition)."""
#         global cap, frame_count, recognized_face
#         while running:
#             ret, frame = cap.read()
#             if not ret:
#                 continue

#             frame_count += 1
#             if frame_count % PROCESS_EVERY_N_FRAMES == 0:
#                 small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#                 rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#                 face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
#                 face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#                 with recognized_face_lock:
#                     recognized_face.clear()  # Clear previous face data

#                     for encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
#                         matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.4)
#                         name = "Unknown"

#                         if True in matches:
#                             match_index = np.argmin(face_recognition.face_distance(known_encodings, encoding))
#                             name = known_names[match_index]

#                         top, right, bottom, left = [v * 4 for v in (top, right, bottom, left)]
#                         recognized_face[name] = (left, top, right, bottom)
    
#     def update_feed(self):
#         """Continuously updates Feed2 (GUI Display) with smooth rendering."""
#         global cap

#         if not cap.isOpened() or not running:
#             return

#         ret, frame = cap.read()
#         if not ret:
#             return

#         # Draw face rectangles from Feed1 (Processed Feed) onto Feed2 (GUI Display)
#         with recognized_face_lock:
#             for name, (left, top, right, bottom) in recognized_face.items():
#                 cv2.rectangle(frame, (left, top), (right, bottom), recognized_face_colour, 2)
#                 cv2.putText(frame, f"{name}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, recognized_face_colour, 2)
        
#         self.update_frame(frame)
#         self.root.after(10, self.update_feed)

#     def update_frame(self, frame):
#         """Converts OpenCV frame to Tkinter-compatible format."""
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame_rgb)
#         img = img.resize((800, 600))
#         img_tk = ImageTk.PhotoImage(image=img)
        
#         self.canvas.img_tk = img_tk
#         self.canvas.configure(image=img_tk)
    
#     def on_close(self):
#         """Handles application closing properly."""
#         global running, cap
#         running = False
#         if cap:
#             cap.release()
#         self.root.quit()
    
#     def run(self):
#         """Starts the Tkinter GUI."""
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = FaceRecognitionApp()
#     app.run()
#     running = False
#     print("[INFO] Application closed.")