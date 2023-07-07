



# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def create_account(self):
        users_name = input("Name: ")
        user_age = input("Age: ")
        username = input("Enter a username:")
        pers = Person(users_name, user_age, username)
        self.list_of_people.append(pers)
        #implement function that creates account here
        print("Creating ...")
        

    def sign_in(self):
        print("")
        user_confirm = input("Username: ")
        for x in self.list_of_people:
            # print("comparing with: " + str(x.username))
            if user_confirm == x.username:
                print("Valid username.")
                return x
        print("Invalid username! Please try again.")

    def add_friend(self, active_user, friend_name):
        active_user.friendlist.append(friend_name)
        print(str(active_user.friendlist))
            

    
        


class Person:
    def __init__(self, name, age, username):
        self.name = name
        self.age = age
        self.username = username
        self.friendlist = []









    # def add_friend(self, person_object):
    #     #implement adding friend. Hint add to self.friendlis
    #     self.friendlist.append()
    #     pass

    def send_message(self):
        #implement sending message to friend here
        pass