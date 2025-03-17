import models.login_model as login_model # login backend
import models.main_model as main_model # main backend
import views.login_view as login_view  # login frontend
import views.main_view as main_view  # main frontend
import os # used to create and destroy the json files
import pandas as pd # writes user_data to csv



# creates the json files when the program loads
# (if they don't already exist)
with open("src/data/poke_data.json", "a"):
    print("poke_data.json created")
with open("src/data/type_data.json", "a"):
    print("type_data.json created")

# controls the login system
# gets the user data of the person logged in
valid_login = False
error_msg = ""
register_msg = ""

while valid_login == False:
    # gets the input from the login view
    login_input = login_view.display_login(error_msg, register_msg)

    # closes program if the user closes the window
    if login_input == "close":
        # deletes the content of the json files
        os.remove("src/data/poke_data.json")
        os.remove("src/data/type_data.json")

        quit()
    
    # registers a new user if the user clicks the register button
    elif login_input[2] == "register":
        username = login_input[0]
        password = login_input[1]
        # creates a new user
        register_msg = login_model.register(username, password)

        error_msg = ""
    
    # runs the login backend
    elif login_input[2] == "login":
        username = login_input[0]
        password = login_input[1]
        # processes login request
        login_output = login_model.login(username, password)

        user_data = login_output[0] # pandas dataframe
        error_msg = login_output[1] # string
        valid_login = login_output[2] # True or False
        
        register_msg = ""

# controls an active session
active_session = True
search_input = ""

while active_session == True:
    main_output = main_view.display_main(user_data)

    search_input = main_output[0]
    user_data = main_output[1]

    if search_input == False:
        # deletes the content of the json files
        os.remove("src/data/poke_data.json")
        os.remove("src/data/type_data.json")
        
        df = pd.read_csv("src/data/user_data.csv")

        username = user_data['username'].to_list()[0]
        index = df[df['username'] == username].index

        df.loc[index, 'poke1'] = user_data['poke1'].to_list()[0]
        df.loc[index, 'poke2'] = user_data['poke2'].to_list()[0]
        df.loc[index, 'poke3'] = user_data['poke3'].to_list()[0]
        df.loc[index, 'poke4'] = user_data['poke4'].to_list()[0]
        df.loc[index, 'poke5'] = user_data['poke5'].to_list()[0]
        df.loc[index, 'poke6'] = user_data['poke6'].to_list()[0]
        
        df.to_csv("src/data/user_data.csv", index=False)
        
        quit()
    
    main_model.search(search_input)
