import customtkinter as ctk # used to create the UI
from PIL import Image # used to import images for customtkinter


# creates the main view
def display_main():
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
    root.title("pokedex")
    root.geometry("480x640")
    root.resizable(False, False)

    ##############################################
    # this contains all the ctk widgets that are placed in the grid

    # --top bar widgets--
    top_bar_frm = ctk.CTkFrame(master=root, bg_color=BLACK, fg_color=BLACK, width=420, height=60)
    # prevents the frame from adjusting its size based on contents
    top_bar_frm.grid_propagate(False)

    search_ent = ctk.CTkEntry(master=top_bar_frm, placeholder_text="Search for a Pokémon...",
                        fg_color=WHITE, text_color=BLACK, corner_radius=20, width=300, height=40)

    # --side bar widgets--
    side_bar_frm = ctk.CTkFrame(master=root, bg_color=RED, fg_color=RED, width=60, height=640)
    # prevents the frame from adjusting its size based on contents
    side_bar_frm.grid_propagate(False)

    black_side_bar_frm = ctk.CTkFrame(master=side_bar_frm, bg_color=BLACK, fg_color=BLACK, width=60, height=520)

    # --profile button/corner widgets--
    corner_piece_img = ctk.CTkImage(light_image=Image.open("./src/assets/Corner Piece.png"),
                                    dark_image=Image.open("./src/assets/Corner Piece.png"),
                                    size=(60, 60))
    corner_piece_lbl_1 = ctk.CTkLabel(master=top_bar_frm,text="", image=corner_piece_img)
    corner_piece_lbl_2 = ctk.CTkLabel(master=side_bar_frm,text="", image=corner_piece_img)

    profile_btn = ctk.CTkButton(master=side_bar_frm, text="",fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                                border_color=BLACK, border_width=6,
                                corner_radius=30, width=50, height=50)

    # --screen widgets--
    screen_background_img = ctk.CTkImage(light_image=Image.open("./src/assets/Screen Background.png"),
                                        dark_image=Image.open("./src/assets/Screen Background.png"),
                                        size=(420, 260))
    screen_background_lbl = ctk.CTkLabel(master=root, text="", image=screen_background_img)

    screen_frm = ctk.CTkFrame(master=root,bg_color=BLACK ,fg_color=WHITE)

    # --buttons widgets--
    buttons_frm = ctk.CTkFrame(master=root, bg_color=RED, fg_color=RED, width=420, height=320)
    # prevents the frame from adjusting its size based on contents
    buttons_frm.grid_propagate(False)

    btn_1 = ctk.CTkButton(master=buttons_frm,text="button 1", fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                        corner_radius=20, width=100, height=100)
    btn_2 = ctk.CTkButton(master=buttons_frm,text="button 2", fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                        corner_radius=20, width=100, height=100)
    btn_3 = ctk.CTkButton(master=buttons_frm,text="button 3", fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                        corner_radius=20, width=100, height=100)
    btn_4 = ctk.CTkButton(master=buttons_frm, text="button 4", fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                        corner_radius=20, width=100, height=100)
    btn_5 = ctk.CTkButton(master=buttons_frm, text="button 5", fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                        corner_radius=20, width=100, height=100)
    btn_6 = ctk.CTkButton(master=buttons_frm, text="button 6", fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                        corner_radius=20, width=100, height=100)
    
    btn_7 = ctk.CTkButton(master=buttons_frm, text="button 7", fg_color=BLUE, bg_color=RED, hover_color=BLUESHADE,
                        corner_radius=20, width=360, height=40)


    ##############################################
    # puts all the tkinter widgets into 'root'
    
    search_ent.grid(column=0, row=0, columnspan=3, padx=30, pady=10)
    corner_piece_lbl_1.grid(column=3, row=0)
    top_bar_frm.grid(column=0, row=0, columnspan=3)

    profile_btn.grid(column=4, row=0, padx=5, pady=5)
    corner_piece_lbl_2.grid(column=4, row=1)
    black_side_bar_frm.grid(column=4, row=2)
    side_bar_frm.grid(column=4, row=0, rowspan=5)

    screen_background_lbl.grid(column=0, row=1, columnspan=4)

    btn_1.grid(column=0, row=3, padx=(30, 15), pady=(20, 10))
    btn_2.grid(column=1, row=3, padx=(15, 15), pady=(20, 10))
    btn_3.grid(column=2, row=3, padx=(15, 30), pady=(20, 10))
    btn_4.grid(column=0, row=4, padx=(30, 15), pady=(10, 10))
    btn_5.grid(column=1, row=4, padx=(15, 15), pady=(10, 10))
    btn_6.grid(column=2, row=4, padx=(15, 30), pady=(10, 10))
    btn_7.grid(column=0, row=5, columnspan=3, padx=(30, 30), pady=(10, 20))
    buttons_frm.grid(column=0, row=3, rowspan=3, sticky="nsew")

    root.mainloop()
