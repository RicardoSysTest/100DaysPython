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

    #Add background image
    imgBg = Image.open('img/background_image_file.png')
    img_background = ctk.CTkImage(dark_image=imgBg, size=(750, 450))
    backgroundImage = ctk.CTkLabel(root, text='', image=img_background)
    backgroundImage.place(x=0,y=0)

    root.mainloop()

```