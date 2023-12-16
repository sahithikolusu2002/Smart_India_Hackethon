# import tkinter as tk
# import customtkinter
# import imageDetector
# import videoDetector
# from tkinter import Label
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
# import subprocess
# import os

# # Set appearance mode and default color theme
# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("dark-blue")

# # Create the root window
# root = customtkinter.CTk()
# root.title("Potholes Detection")
# root.resizable(False, False)
# root.geometry("400x200")

# HeadingText = Label(
#     root, text="Select Image or Video to Identify Pothole", font=("poppins", 16)
# )


# def run_flask_app():
#     # Launch the Flask app in a separate process
#     subprocess.Popen(
#         ["python", "app.py"], cwd=os.path.dirname(os.path.realpath(__file__))
#     )


# def select_image_file():
#     filetypes = (("Image files", "*.jpg"),)

#     filename = fd.askopenfilename(
#         title="Open a file", initialdir="/", filetypes=filetypes
#     )

#     if len(filename) > 0:
#         showinfo(title="Selected Image File", message=filename)
#         pothole_data_list = imageDetector.detectPotholeonImage(filename)

#         if pothole_data_list:
#             # Save pothole data to a CSV file with a specific name for images
#             csv_filename = "./templates/pothole_data.csv"
#             imageDetector.create_csv_file(csv_filename)
#             imageDetector.save_to_csv(pothole_data_list, csv_filename)

#         # After processing the image, run the Flask app
#         run_flask_app()


# def select_video_file():
#     filetypes = (("Video files", "*.mp4"),)

#     filename = fd.askopenfilename(
#         title="Open a file", initialdir="/", filetypes=filetypes
#     )

#     if len(filename) > 0:
#         showinfo(title="Selected Video File", message=filename)
#         pothole_data_list = videoDetector.detectPotholeonVideo(filename)

#         if pothole_data_list:
#             # Save pothole data to a CSV file with a specific name for videos
#             csv_filename = "./templates/pothole_data.csv"
#             videoDetector.create_csv_file(csv_filename)
#             videoDetector.save_to_csv(pothole_data_list, csv_filename)

#         # After processing the video, run the Flask app
#         run_flask_app()


# def live_camera_button_callback():
#     # Process the live camera feed
#     pothole_data_list = videoDetector.detectPotholeonVideo("live")

#     if pothole_data_list:
#         # Save pothole data to a CSV file with a specific name for live camera feed
#         csv_filename = "./templates/pothole_data.csv"
#         videoDetector.create_csv_file(csv_filename)
#         videoDetector.save_to_csv(pothole_data_list, csv_filename)

#     # After processing the live camera feed, run the Flask app
#     run_flask_app()


# # Image open button
# image_open_button = customtkinter.CTkButton(
#     root, text="Image", command=select_image_file, hover_color="green"
# )

# # Video open button
# video_open_button = customtkinter.CTkButton(
#     root, text="Video", command=select_video_file, hover_color="green"
# )

# # Live Camera button
# liveCamera_button = customtkinter.CTkButton(
#     root,
#     text="Live Camera",
#     command=live_camera_button_callback,  # Use the callback function
#     hover_color="green",
#     border_color="black",
#     border_width=2.5,
#     fg_color="red",
#     font=("poppins", 14),
# )

# HeadingText.place(x=50, y=15)
# image_open_button.place(x=40, y=80)
# video_open_button.place(x=220, y=80)
# liveCamera_button.pack(side="bottom", pady=20)

# # Run the application
# root.mainloop()

import tkinter as tk
import customtkinter
import imageDetector
import videoDetector
from tkinter import Label
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import subprocess
import os

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# Create the root window
root = customtkinter.CTk()
root.title("Potholes Detection")
root.resizable(False, False)
root.geometry("400x200")

HeadingText = Label(
    root, text="Select Image or Video to Identify Pothole", font=("poppins", 16)
)


def run_flask_app():
    # Launch the Flask app in a separate process
    subprocess.Popen(
        ["python", "app.py"], cwd=os.path.dirname(os.path.realpath(__file__))
    )


def select_image_file():
    filetypes = (("Image files", "*.jpg"),)

    filename = fd.askopenfilename(
        title="Open a file", initialdir="/", filetypes=filetypes
    )

    if len(filename) > 0:
        showinfo(title="Selected Image File", message=filename)
        pothole_data_list = imageDetector.detectPotholeonImage(filename)

        if pothole_data_list:
            # Save pothole data to a CSV file with a specific name for images
            csv_filename = "./templates/pothole_data.csv"
            imageDetector.create_csv_file(csv_filename)
            imageDetector.save_to_csv(pothole_data_list, csv_filename)

        # After processing the image, run the Flask app
        run_flask_app()


def select_video_file():
    filetypes = (("Video files", "*.mp4"),)

    filename = fd.askopenfilename(
        title="Open a file", initialdir="/", filetypes=filetypes
    )

    if len(filename) > 0:
        showinfo(title="Selected Video File", message=filename)
        pothole_data_list = videoDetector.detectPotholeonVideo(filename)

        if pothole_data_list:
            # Save pothole data to a CSV file with a specific name for videos
            csv_filename = "./templates/pothole_data.csv"
            videoDetector.create_csv_file(csv_filename)
            videoDetector.save_to_csv(pothole_data_list, csv_filename)

        # After processing the video, run the Flask app
        run_flask_app()


def live_camera_button_callback():
    # Process the live camera feed
    pothole_data_list = videoDetector.detectPotholeonVideo("live")

    # if pothole_data_list:
    #     # Save pothole data to a CSV file with a specific name for live camera feed
    #     csv_filename = "./templates/pothole_data.csv"
    #     videoDetector.create_csv_file(csv_filename)
    #     videoDetector.save_to_csv(pothole_data_list, csv_filename)

    # After processing the live camera feed, run the Flask app
    run_flask_app()


# Image open button
image_open_button = customtkinter.CTkButton(
    root, text="Image", command=select_image_file, hover_color="green"
)

# Video open button
video_open_button = customtkinter.CTkButton(
    root, text="Video", command=select_video_file, hover_color="green"
)

# Live Camera button
liveCamera_button = customtkinter.CTkButton(
    root,
    text="Live Camera",
    command=live_camera_button_callback,  # Use the callback function
    hover_color="green",
    border_color="black",
    border_width=2.5,
    fg_color="red",
    font=("poppins", 14),
)

HeadingText.place(x=50, y=15)
image_open_button.place(x=40, y=80)
video_open_button.place(x=220, y=80)
liveCamera_button.pack(side="bottom", pady=20)

# Run the application
root.mainloop()
