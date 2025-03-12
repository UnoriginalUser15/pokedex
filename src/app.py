import models.login_model as login_model # login backend
import views.login_view as login_view
import views.main_view as main_view


# controls the login system
# gets the user data of the person logged in
valid_login = False
error_msg = ""

while valid_login == False:
    # gets the input from the login view
    login_input = login_view.display_login(error_msg)

    # closes program if the user closes the window
    if login_input == False:
        quit()
    # puts the username and password into variables
    else:
        username = login_input[0]
        password = login_input[1]

    # passes the login data into the backend
    login_output = login_model.login_backend(username, password)

    user_data = login_output[0]
    error_msg = login_output[1]
    valid_login = login_output[2]


# main_view.display_main()