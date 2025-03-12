import customtkinter as ctk # used to get the string value from inputs in 'login_view.py'
import pandas as pd # used to load the csv file


# function for logging in 
def login_backend(username, password):

    valid_login = False
    user_info = None
    error_msg = ""

    # loads the csv file into a pandas datafram
    df = pd.read_csv('src/user_data.csv')
    df = df.set_index('userID')
    # gets list of existing usernames
    user_list = df['username'].to_list()

    # checks if the username exists
    if username in user_list:
        
        # gets the information about the suer logging in
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
