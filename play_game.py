from sys import exit
from user_input.is_user_registered import is_user_registered
from user_input.get_username_and_password import get_username_and_password
from database_functions.users import get_user, UserNotFound

if __name__ == '__main__':
    pass
    # step1 ask user if sign up or login
    is_registered = is_user_registered()

    # get the username and password
    username, password = get_username_and_password()

    if is_registered:
        try:
            user = get_user(username)# check user exists in db AND that password is correct and start game
        except UserNotFound:
            print('User does not exist')
            exit()

        if password != user['password']:
            print('Password is incorrect')
            exit()
    else:
        # if sign up, check user dosen't exist. Check user and password are valid, , call function to start game
        pass

    print('Game started')
