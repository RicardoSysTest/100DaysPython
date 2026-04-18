
# TODO LIST IN Python
This application let you know how to create a Todo that 
store the data in SQLite DB. 

## SetUp
1. Create a virtual enviroment
2. Activate virtual enviroment `pipenv shell`
3. Install GUI interface `pip install customtkinter`
4. Install image gestor `pip install pillow`
5. And to run the project `py main.py`

## Create Main Frame

```python

    import customtkinter as ctk
    import sqlite3

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')

    root = ctk.CTk()
    root.geometry('750x450')
    root.title('ToDo-List')

    root.mainloop()

```