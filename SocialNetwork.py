from  SocialNetworkClasses import SocialNetwork, Person 
from SocialNetworkClasses import *
import SocialNetworkUI


ai_social_network = SocialNetwork()


if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = SocialNetworkUI.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            print("\nYou are now in the sign in menu.")
            signed_in_user = ai_social_network.sign_in()
            if signed_in_user != None:
                inner_menu_choice = SocialNetworkUI.manageAccountMenu(signed_in_user)
            
            
                if inner_menu_choice == "1":
                    SocialNetworkUI.editAccountDetails()
                    print("")
                    
   
                elif inner_menu_choice == "2":
                    print("")
                    SocialNetwork.add_friend()
                    SocialNetworkUI.manageAccountMenu()
                    break
                        
                elif inner_menu_choice == "3":
                    print("3")
                    print("You\'re current friends are: ")
                    print(SocialNetwork.add_friend)
                    
                    
            while True:
                if inner_menu_choice == "5":
                    break
                else:
                    inner_menu_choice = SocialNetworkUI.manageAccountMenu(signed_in_user)

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = SocialNetworkUI.mainMenu()



























# while True: 
#     if choice == "1":
#         print("\nYou are now in the create account menu")
#         ai_social_network.create_account()
#         while True:
#             inner_menu_choice = SocialNetworkUI.mainMenu()
#             if inner_menu_choice == "1":
#                 SocialNetworkUI.manageAccountMenu()
#                 break
                
#             elif inner_menu_choice == "2":
#                 print("\nYou are now in the sign in menu.")
#                 signed_in_user = ai_social_network.sign_in()
#                 if signed_in_user != None:
#                     SocialNetworkUI.manageAccountMenu(signed_in_user)
                    
#             elif inner_menu_choice =="2":
#                 SocialNetworkUI.editAccountDetails()
                
                
                
#             if inner_menu_choice == "5":
#                 break
                    
                    
#                         # while True:
#                         #     FriendList.add_friend()
#                         #     friend = Person(friend_name)
#                         #     if inner_menu_choice == "2":
#                         #         break




#     elif choice == "2":
#         ai_social_network.sign_in()
            

    # elif choice == "2":
    #             print("\nYou are now in the sign in menu")
    #             inner_menu_choice = SocialNetworkUI.sign_in()
    #             while True:
    #                 if user_confirm == any(self.list_of_people):
    #                     inner_menu_choice = SocialNetworkUI.manageAccountMenu()
    #                 else:
    #                     print("Invalid username! Please try again.")
    #                     inner_menu_choice = SocialNetworkUI.sign_in()






    # elif choice == "2":
    #                 print("\nYou are now in the sign in menu")
    #                 inner_menu_choice = SocialNetworkUI.sign_in()
    #                 while True:
    #                     if user_confirm == any(self.list_of_people):
    #                         inner_menu_choice = SocialNetworkUI.manageAccountMenu()
    #                     else:
    #                         print("Invalid username! Please try again.")
    #                         inner_menu_choice = SocialNetworkUI.sign_in()






# elif choice == "2":
#             print("\nYou are now in the sign in menu")
#             inner_menu_choice = SocialNetworkUI.sign_in()
#             #Handle inner menu here
#             while True:
#                 if inner_menu_choice == "5":
#                     break
#                 else:
#                     inner_menu_choice = SocialNetworkUI.manageAccountMenu()








    # elif choice == "2":
    #     print("\nYou are now in the sign in menu")
    #     while True:
    #         inner_menu_choice = SocialNetworkUI.sign_in()
    #         if  inner_menu_choice == "1":
    #             break
                
    #         else:
    #             inner_menu_choice = SocialNetworkUI.sign_in()


    
    # elif choice == "3":
    #     print("Thank you for visiting. Goodbye")
    #     break

    # else:
    #     print("Your input is invalid. Try Again!")
        
    #         #restart menu
    #     choice = SocialNetworkUI.mainMenu()   



