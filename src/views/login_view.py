import customtkinter as ctk # used to create the UI


# creates the ui for the login
def display_login(error_msg, register_msg):
    
    # function that runs when the submit button is clicked
    def submit():
        # makes the variable accessable outside of the submit func
        # (i know this is bad practice, i just couldn't find another solution)
        global username
        global password
        global log_or_reg

        username = username_var.get().replace(" ","")
        password = password_var.get().replace(" ","")
        # variable to control whether the back end trys to login a new user or register
        log_or_reg = "login"
        # removes the window
        root.destroy()

    # function that runs when the register button is clicked
    def register():
        # makes the variable accessable outside of the submit func
        # (i know this is bad practice, i just couldn't find another solution)
        global username
        global password
        global log_or_reg

        username = username_var.get().replace(" ", "")
        password = password_var.get().replace(" ", "")
        # variable to control whether the back end trys to login a new user or register
        log_or_reg = "register"
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

        return False

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
    root = ctk.CTk(fg_color=BLACK)
    root.title("Pokédex: Login")
    root.geometry("256x352")
    root.resizable(False, False)

    # creates the variable for the text entry
    username_var = ctk.StringVar()
    password_var = ctk.StringVar()

    ##############################################
    # this contains all the ctk widgets that are placed in the grid

    username_lbl = ctk.CTkLabel(root, text="Username")
    username_ent = ctk.CTkEntry(root, textvariable=username_var,
                                fg_color=WHITE, border_color=RED,
                                text_color=BLACK,
                                width=208)

    password_lbl = ctk.CTkLabel(root, text="Password")
    password_ent = ctk.CTkEntry(root, textvariable=password_var,
                                fg_color=WHITE, border_color=RED,
                                text_color=BLACK,
                                width=208, show="*")

    error_lbl = ctk.CTkLabel(root, text=error_msg, text_color=RED)
    register_lbl = ctk.CTkLabel(root, text=register_msg, text_color=YELLOW)

    submit_btn = ctk.CTkButton(root, text="Submit", command=submit,
                                fg_color=BLUE, hover_color=BLUESHADE,
                                text_color=BLACK, corner_radius=16,
                                width=96, height=32)
    register_btn = ctk.CTkButton(root, text="Register", command=register,
                                fg_color=YELLOW, hover_color=YELLOWSHADE,
                                text_color=BLACK, corner_radius=16,
                                width=96, height=32)

    ##############################################
    # puts all the tkinter widgets into 'root'

    username_lbl.grid(column=0, row=0, pady=(32,0))
    username_ent.grid(column=0, row=1)

    password_lbl.grid(column=0, row=2, pady=(16,0))
    password_ent.grid(column=0, row=3)

    error_lbl.grid(column=0, row=4)
    register_lbl.grid(column=0, row=5)

    # the 'padx=80' makes the content centered, so don't change it
    submit_btn.grid(column=0, row=6, padx=80, pady=(24,0))
    register_btn.grid(column=0, row=7, pady=16)

    # runs the close function when the window is 'destroyed'
    root.protocol("WM_DELETE_WINDOW", close)

    # displays the window
    root.mainloop()
    # if the user closes the window then it returns 'close'
    try:
        return username, password, log_or_reg
    except:
        return "close"
