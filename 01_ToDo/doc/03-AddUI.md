```python


# pip install customtkinter
import customtkinter as ctk

#pip install pillow
from PIL import Image

import sqlite3

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()

root.geometry('750x450')
root.title('ToDo-List')
#==================================================================================================
#  Functions
#==================================================================================================

def addTodo():
    print("New task is add")
#==================================================================================================
# User Interface Configuration
#==================================================================================================
#Add background image
imgBg = Image.open('img/background_image_file.png')
img_background = ctk.CTkImage(dark_image=imgBg, size=(750, 450))
backgroundImage = ctk.CTkLabel(root, text='', image=img_background)
backgroundImage.place(x=0,y=0)

# Add Label Task
title_app = ctk.CTkLabel(root, text='To-Do', bg_color="transparent", font=ctk.CTkFont(size=30, weight='bold'))
title_app.pack(pady=40, padx=(20,40))

#Add Frame container for Entry and Task List
todoFrame = ctk.CTkFrame(root)
todoFrame.pack()

# Entru for new task
task_entry = ctk.CTkEntry(todoFrame, width=500, placeholder_text="Enter new task ...")
task_entry.pack()

#Task List Container
misTareas = ctk.CTkScrollableFrame(todoFrame, height=200, bg_color="transparent", border_width=2, orientation="vertical", scrollbar_button_color="#FFCC70")
misTareas.pack(fill="x")

# Adde Button to enter new task
newTaskBtn = ctk.CTkButton(root, text="Add", width=500, command=addTodo)
newTaskBtn.pack(pady=20)

root.mainloop()


```