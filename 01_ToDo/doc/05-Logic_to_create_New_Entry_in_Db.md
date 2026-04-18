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
#  DB Configuration
#==================================================================================================
#Create DB (In case that todo.db is not define new wil be created)
conn = sqlite3.connect('todo.db')

#Create cursor to create table, add todo consult
c = conn.cursor()

#Create table and if table is not define create
c.execute("""
    CREATE TABLE if not exists todo(
          id INTEGER PRIMARY KEY AUTOINCREMENT, 
          create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          description TEXT NOT NULL, 
          complete BOOLEAN NOT NULL
    );
""")

#Execute Conusltation
conn.commit()

#==================================================================================================
#  Functions
#==================================================================================================

def addTodo():
    
    # Get Value from the entry
    newTask = task_entry.get()

    # Ensure that entry is not emty
    if newTask: 
        print("Add taks ", newTask)

        #Insert new task in the DB, Pass newsTaks String and because is new taks the status will false Not Complete.
        c.execute("""
            INSERT INTO todo (description, complete) VALUES(?,?) 
        """, (newTask,False))

        # Send instruction to DB
        conn.commit()

        #Clear entry field (from char o to the end)
        task_entry.delete(0, 'end')

    else:
        pass


def renderTodoList(): 

    #Request all the Data store in the DB
    rows  = c.execute("SELECT * FROM todo").fetchall()

    #¿Que es lo que nos devuelve rows?
    print(rows)

    # Destroy info 
    #for widget in misTareas.winfo_children():
        #widget.destroy()

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

#Render all the Task Created
renderTodoList()

root.mainloop()




```