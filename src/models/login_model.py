import customtkinter as ctk # used to get the string value from inputs in 'login_view.py'
import pandas as pd # used to load the csv file


# function for logging in 
def login(username, password):

    valid_login = False
    user_info = None
    error_msg = ""

    # loads the csv file into a pandas datafram
    df = pd.read_csv('src/data/user_data.csv')
    df = df.set_index('userID')
    # gets list of existing usernames
    user_list = df['username'].to_list()

    # checks if the username exists
    if username in user_list:
        
        # gets the information about the user logging in
        user_id = df[df['username'] == username].index
        user_info = df.loc[user_id]

        valid_password = user_info.loc[user_id, 'password'].values
        # turns valid password from an array to a string
        valid_password = ''.join(valid_password)

        # login becomes valid if the password is also correct
        if password != valid_password:
            error_msg = "Error: Invalid password"
        else:
            valid_login = True
    # displays error message if the username is invalid
    else:
        error_msg = "Error: Invalid username"

    # returns all the import data to 'app.py'
    return user_info, error_msg, valid_login

# registers new accounts
def register(username, password):
    register_msg = ""

    # loads the csv file into a pandas datafram
    df = pd.read_csv('src/data/user_data.csv')
    df = df.set_index('userID')
    # gets list of existing usernames
    user_list = df['username'].to_list()

    if username == "":
        register_msg = "Username cannot be blank"
        return register_msg
    
    elif password == "":
        register_msg = "Password cannot be blank"
        return register_msg
    
    elif username not in user_list:
        try:
            user_id = (df.iloc[-1].name) + 1

            new_user = {
                "userID": user_id,
                "username": username,
                "password": password,
                "poke1": "Empty",
                "poke2": "Empty",
                "poke3": "Empty",
                "poke4": "Empty",
                "poke5": "Empty",
                "poke6": "Empty"
            }

            new_user_df = pd.DataFrame([new_user])
            # appends the new user to the .csv file
            new_user_df.to_csv('src/data/user_data.csv', mode='a',index=False , header= False)

            register_msg = "New account has been created!"
        except:
            register_msg = "Unknown error occured when registering"
        
        return register_msg
    
    else:
        register_msg = "Username already exists"
        return register_msg