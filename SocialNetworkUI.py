from SocialNetworkClasses import SocialNetwork

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Sign In")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

# def sign_in():
#     print("")
#     user_confirm = input("Username: ")
#     input("1. Confirm: ")
#     SocialNetworkClasses.create_account(user_confirm)

def manageAccountMenu(active_user):
    print("")
    print("Hello %s!" % active_user.name)
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Log Out")
    active_user_input = input("Please Choose a number: ")
    if active_user_input == "2":
        friend_username = input("Enter friend\'s username: ")
        SocialNetwork().add_friend(active_user, friend_username)
    return active_user_input


def editAccountDetails():
    print("")
    print("1. Change Name")
    print("2. Change Age")
    print("3. Change Username")
    return input("Please Choose a number: ")




# def create_account():
#     print("")
#     users_name = input("Name: ")
#     user_age = input("Age: ")
#     username = input("Enter a username:")
#     input("1. Confirm ")
#     SocialNetworkClasses.create_account(users_name, user_age, username)