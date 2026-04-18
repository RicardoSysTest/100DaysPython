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

def new_window(description):

    def _new_window():

        taks_detail = ctk.CTkToplevel(root)
        taks_detail.title(description)
        taks_detail.geometry("400x200")

    return _new_window


def removed(id):

    def _removed():

        c.execute("DELETE FROM todo WHERE id = ?", (id, ))
        conn.commit()
        renderTodoList()

    return _removed

def status_task(id):
    
    def _status_task():
    
        task = c.execute("SELECT * from todo WHERE id = ?",(id, )).fetchone()
        c.execute("UPDATE todo SET complete = ? WHERE id =?",(not task[3], id))
        conn.commit()
        renderTodoList()
    
    return _status_task

def addTodo():
    
    # Get Value from the entry
    newTask = task_entry.get()

    # Ensure that entry is not emty
    if newTask: 

        #Insert new task in the DB, Pass newsTaks String and because is new taks the status will false Not Complete.
        c.execute("""
            INSERT INTO todo (description, complete) VALUES(?,?) 
        """, (newTask,False))

        # Send instruction to DB
        conn.commit()

        #Clear entry field (from char o to the end)
        task_entry.delete(0, 'end')

        #Update List with the new values set in the DB
        renderTodoList()

    else:
        pass


def renderTodoList(): 

    #Request all the Data store in the DB
    rows  = c.execute("SELECT * FROM todo").fetchall()

    #Before render all the contend in the Frame we remove do avoid dupliation of the list element
    for widget in misTareas.winfo_children():
        
        widget.destroy()

    #Imprimir todos los archivoes inportado en la base de datos
    for i in range(0, len(rows)):
        
        # Print for every inputin the DB 
        id = rows[i][0]
        #create_date = rows[i][1]
        description = rows[i][2]
        complete = rows[i][3]

        # Create a Frame for every task and set widget inside Scroll Frame
        frameTask = ctk.CTkFrame(misTareas, fg_color="transparent", height=300)
        # Widget full cove eje x
        frameTask.pack(fill="x")

        # Change Text color in case that taks is complete or not
        if complete:
            color = '#555555'
            done = True
        else:
            color = '#ffffff'
            done = False
        
        #Add widget for every task
        taskWidget = ctk.CTkCheckBox(frameTask, text=description, text_color=color, font=ctk.CTkFont(size=13, overstrike=done), checkbox_width=15, checkbox_height=15, corner_radius=15, border_width=2, command=status_task(id))
        taskWidget.pack(side='left')
        taskWidget.select() if complete else taskWidget.deselect()

        btn_detail = ctk.CTkButton(frameTask, text='Open', width=60, fg_color="#228C22", corner_radius=20, command=new_window(description))
        btn_detail.pack(side="right", padx=10, pady=5)

        btn_detail = ctk.CTkButton(frameTask, text='Delete', width=60, fg_color="#9B1003", corner_radius=20, command=removed(id))
        btn_detail.pack(side="right", padx=10, pady=5)



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
