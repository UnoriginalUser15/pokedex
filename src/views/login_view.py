import customtkinter as ctk # used to create the UI


# creates the ui for the login
def display_login(error_msg):
    # function that runs when the submit button is clicked
    def submit():
        # makes the variable accessable outside of the submit func
        # (i know this is bad practice, i just couldn't find another solution)
        global username
        global password

        username = username_var.get()
        password = password_var.get()
        # removes the window
        root.destroy()

    # deletes the variables when you close the window
    def close():
        global username
        global password
        
        try:
            # this means that the program closes instead of continuing the loop
            del username
            del password

            # removes the window
            root.destroy()
        except:
            # removes the window
            root.destroy()

    # list of colours that will be used for the UI
    RED = "#DC0A2D"
    REDSHADE = "#a3051f"
    YELLOW = "#FEC401"
    YELLOWSHADE = "#bd9101"
    BLUE = "#29AAFD"
    BLUESHADE = "#1c7dbc"
    WHITE = "#DEDEDE"
    BLACK = "#242424"

    # initialises the customtkinter frame
    root = ctk.CTk()
    root.title("login")
    root.geometry("256x256")
    root.resizable(False, False)

    # creates the variable for the text entry
    username_var = ctk.StringVar()
    password_var = ctk.StringVar()

    ##############################################
    # this contains all the ctk widgets that are placed in the grid

    username_lbl = ctk.CTkLabel(root, text="username: ")
    username_ent = ctk.CTkEntry(root, textvariable=username_var)

    password_lbl = ctk.CTkLabel(root, text="password: ")
    password_ent = ctk.CTkEntry(root, textvariable=password_var)

    error_lbl = ctk.CTkLabel(root, text=error_msg, text_color=RED)
    submit_btn = ctk.CTkButton(root, text="submit", command=submit)

    ##############################################
    # puts all the tkinter widgets into 'root'

    username_lbl.grid(column=0, row=0)
    username_ent.grid(column=1, row=0)

    password_lbl.grid(column=0, row=1)
    password_ent.grid(column=1, row=1)

    error_lbl.grid(column=1, row=2)
    submit_btn.grid(column=1, row=3)

    # runs the close function when the window is 'destroyed'
    root.protocol("WM_DELETE_WINDOW", close)

    # displays the window
    root.mainloop()
    # if the user closes the window then it returns false
    try:
        return username, password
    except:
        return False
