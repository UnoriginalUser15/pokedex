import customtkinter as ctk # used to create the UI
from PIL import Image, ImageTk # used to import images for customtkinter
import urllib.request
import io
import pandas as pd # used to get the values in the 'user_data' dataframe
import json # used to load the 2 data json files
import models.main_model as main_model


# creates the main view
def display_main(user_data):

    def search():
        global search_input

        search_input = search_var.get().lower().replace(" ", "")

        if search_input == "":
            return

        # removes the window
        root.destroy()
    
    # deletes the variables when you close the window
    def close():
        global search_input
        
        try:
            # this means that the program closes instead of continuing the loop
            del search_input
            # removes the window
            root.destroy()
        except:
            # removes the window
            root.destroy()

    # gets the sprite to display in the buttons
    def get_sprite(pokemon, mode):
        match mode:
            case "screen":
                if pokemon != "Empty":
                    # loads the relevant pokemon data into 'poke_data.json'
                    main_model.search(pokemon)

                    with open("src/data/poke_data.json", "r") as file:
                        poke_data = json.load(file)
                        img_url = poke_data['sprites']['front_default']
                    with urllib.request.urlopen(img_url) as u:
                        raw_data = u.read()

                    # creates the image that is to be displayed in the button
                    img = ImageTk.PhotoImage(Image.open(io.BytesIO(raw_data)).resize((200, 200)))
                else:
                    img = ImageTk.PhotoImage(Image.open("src/assets/transparent_placeholder.png"))
            case "button":
                if user_data[pokemon].to_list()[0] != "Empty":
                    # loads the relevant pokemon data into 'poke_data.json'
                    main_model.search(user_data[pokemon].to_list()[0])

                    with open("src/data/poke_data.json", "r") as file:
                        poke_data = json.load(file)
                        img_url = poke_data['sprites']['front_default']
                    with urllib.request.urlopen(img_url) as u:
                        raw_data = u.read()

                    # creates the image that is to be displayed in the button
                    img = ImageTk.PhotoImage(Image.open(io.BytesIO(raw_data)).resize((65, 65)))
                else:
                    img = ImageTk.PhotoImage(Image.open("src/assets/transparent_placeholder.png"))
        
        return img


    def create_screen():
        pass

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
    root.title("Pokédex")
    root.geometry("480x640")
    root.resizable(False, False)

    search_var = ctk.StringVar()

    ##############################################
    # this contains all the ctk widgets that are placed in the grid

    # --top bar widgets--
    top_bar_frm = ctk.CTkFrame(root, bg_color=BLACK, fg_color=BLACK, width=420, height=60)
    # prevents the frame from adjusting its size based on contents
    top_bar_frm.grid_propagate(False)

    search_ent = ctk.CTkEntry(top_bar_frm, placeholder_text="Search for a Pokémon or Type...",
                                textvariable=search_var, fg_color=WHITE, text_color=BLACK,
                                corner_radius=10, width=300, height=40)

    # --side bar widgets--
    side_bar_frm = ctk.CTkFrame(root, bg_color=RED, fg_color=RED, width=60, height=640)
    # prevents the frame from adjusting its size based on contents
    side_bar_frm.grid_propagate(False)

    black_side_bar_frm = ctk.CTkFrame(side_bar_frm, bg_color=BLACK, fg_color=BLACK, width=60, height=520)

    # --profile button/corner widgets--
    corner_piece_img = ctk.CTkImage(light_image=Image.open("./src/assets/Corner Piece.png"),
                                    dark_image=Image.open("./src/assets/Corner Piece.png"),
                                    size=(60, 60))
    corner_piece_lbl_1 = ctk.CTkLabel(top_bar_frm,text="", image=corner_piece_img)
    corner_piece_lbl_2 = ctk.CTkLabel(side_bar_frm,text="", image=corner_piece_img)

    profile_btn = ctk.CTkButton(side_bar_frm, text="",fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                                border_color=BLACK, border_width=6,
                                corner_radius=30, width=50, height=50)

    # --screen widgets--
    screen_background_img = ctk.CTkImage(light_image=Image.open("./src/assets/Screen Background.png"),
                                        dark_image=Image.open("./src/assets/Screen Background.png"),
                                        size=(420, 260))
    screen_background_lbl = ctk.CTkLabel(root, text="", image=screen_background_img)

    screen_frm = ctk.CTkFrame(root,bg_color="transparent" ,fg_color=BLACK, corner_radius=0,
                                width=340, height=220)
    # prevents the frame from adjusting its size based on contents
    screen_frm.grid_propagate(False)
    
    pokemon_img = ctk.CTkLabel(screen_frm, text="", image=get_sprite('sylveon', 'screen'))
    pokemon_lbl = ctk.CTkLabel(screen_frm, text='sylveon', text_color=WHITE, font=("Arial", 24))

    stats_frm = ctk.CTkScrollableFrame(screen_frm, bg_color="transparent", fg_color="grey20",
                                        width=120, height=200, label_text="Stats", label_fg_color=RED)

    # --buttons widgets--
    buttons_frm = ctk.CTkFrame(root, bg_color=RED, fg_color=RED, width=420, height=320)
    # prevents the frame from adjusting its size based on contents
    buttons_frm.grid_propagate(False)

    btn_1 = ctk.CTkButton(buttons_frm,text=user_data['poke1'].to_list()[0],
                        fg_color=BLUE, bg_color=RED, text_color=BLACK,
                        hover_color=BLUESHADE, corner_radius=20, width=100, height=100,
                        image=get_sprite('poke1', 'button'), compound="top")

    btn_2 = ctk.CTkButton(buttons_frm,text=user_data['poke2'].to_list()[0],
                        fg_color=BLUE, bg_color=RED, text_color=BLACK,
                        hover_color=BLUESHADE, corner_radius=20, width=100, height=100,
                        image=get_sprite('poke2', 'button'), compound="top")
    
    btn_3 = ctk.CTkButton(buttons_frm,text=user_data['poke3'].to_list()[0],
                        fg_color=BLUE, bg_color=RED, text_color=BLACK,
                        hover_color=BLUESHADE, corner_radius=20, width=100, height=100,
                        image=get_sprite('poke3', 'button'), compound="top")
    
    btn_4 = ctk.CTkButton(buttons_frm, text=user_data['poke4'].to_list()[0],
                        fg_color=BLUE, bg_color=RED, text_color=BLACK,
                        hover_color=BLUESHADE, corner_radius=20, width=100, height=100,
                        image=get_sprite('poke4', 'button'), compound="top")
    
    btn_5 = ctk.CTkButton(buttons_frm, text=user_data['poke5'].to_list()[0],
                        fg_color=BLUE, bg_color=RED, text_color=BLACK,
                        hover_color=BLUESHADE, corner_radius=20, width=100, height=100,
                        image=get_sprite('poke5', 'button'), compound="top")
    
    btn_6 = ctk.CTkButton(buttons_frm, text=user_data['poke6'].to_list()[0],
                        fg_color=BLUE, bg_color=RED, text_color=BLACK,
                        hover_color=BLUESHADE, corner_radius=20, width=100, height=100,
                        image=get_sprite('poke6', 'button'), compound="top")

    search_btn = ctk.CTkButton(buttons_frm, text="Search", command=search,
                                fg_color=YELLOW, bg_color=RED, text_color=BLACK,
                                hover_color=YELLOWSHADE, corner_radius=20, width=360, height=40)

    ##############################################
    # puts all the tkinter widgets into 'root'
    
    search_ent.grid(column=0, row=0, columnspan=2, padx=30, pady=10)
    corner_piece_lbl_1.grid(column=3, row=0)
    top_bar_frm.grid(column=0, row=0, columnspan=3)

    profile_btn.grid(column=4, row=0, padx=5, pady=5)
    corner_piece_lbl_2.grid(column=4, row=1)
    black_side_bar_frm.grid(column=4, row=2)
    side_bar_frm.grid(column=4, row=0, rowspan=5)

    screen_background_lbl.grid(column=0, row=1, columnspan=4)
    screen_frm.grid(column=0, row=1, columnspan=4, rowspan=2)
    
    pokemon_img.grid(column=0, row=1, padx=10, pady=(10, 0))
    pokemon_lbl.grid(column=0, row=2, pady=(0, 10))

    stats_frm.grid(column=1, row=1, rowspan=50, padx=(0, 10), pady=10)

    btn_1.grid(column=0, row=3, padx=(30, 15), pady=(20, 10))
    btn_2.grid(column=1, row=3, padx=(15, 15), pady=(20, 10))
    btn_3.grid(column=2, row=3, padx=(15, 30), pady=(20, 10))
    btn_4.grid(column=0, row=4, padx=(30, 15), pady=(10, 10))
    btn_5.grid(column=1, row=4, padx=(15, 15), pady=(10, 10))
    btn_6.grid(column=2, row=4, padx=(15, 30), pady=(10, 10))
    search_btn.grid(column=0, row=5, columnspan=3, padx=(30, 30), pady=(10, 20))
    buttons_frm.grid(column=0, row=3, rowspan=3, sticky="nsew")

    # runs the close function when the window is 'destroyed'
    root.protocol("WM_DELETE_WINDOW", close)

    ##############################################

    root.mainloop()

    # if the user closes the window, the program will stop
    try:
        return search_input
    except:
        return False
