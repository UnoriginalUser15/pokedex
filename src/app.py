import models.login_model as login_model # login backend
import views.login_view as login_view
import views.main_view as main_view


# controls the login system
# gets the user data of the person logged in
valid_login = False
error_msg = ""
register_msg = ""

while valid_login == False:
    # gets the input from the login view
    login_input = login_view.display_login(error_msg, register_msg)

    # closes program if the user closes the window
    if login_input == False:
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


main_view.display_main()