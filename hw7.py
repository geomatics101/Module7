try:
    from sortedcontainers import SortedDict
except:
    raise ModuleNotFoundError ("Module not found")

'''
In command prompt: Type pip install sortedcontainers to install the module sortedcontainers.
The purpose of this script is to allow users to print usernames/names,
add a user to the list, remove a user from the list, look up a user by name or username, and end the script.

By:  Allison Bergman
Date: March 1, 2017
HW. 7
This was made with Python version 3.6
'''



def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Username by Name')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

#display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    
    menu_choice = int(input("Type in a number (1-5): "))

    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x,y in usernames.items():
            try:
                print("Name: {} \tUser Name: {} \n".format(x,y))
            except:
                raise SystemExit("An unforseen error happend")

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        if name.isalpha() is False: raise ValueError("No numbers in name, please.")
        username = input("User Name: ")
        if username.isalpha() is False: raise ValueError("No numbers in username, please.")
        usernames[name] = username

    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        if name.isalpha() is False: raise ValueError("No numbers in username, please.")
        if name in usernames:
            username_to_delete = usernames[name]
            del usernames[name]
            print ("Username: {} was removed.".format(username_to_delete))   
        else:
            print ("Name must be in list")



        '''This menu choice allows the users to search through both usernames and names for the username
            and name associated with the search value, it also brings up an error if the user tries to put
            a number in the search.'''
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name or username: ")
        
        '''Try and except error if the user enters any numbers in the search perameter for the
            username or name it will come up with a value error.'''
        if name.isalpha() is False: raise ValueError("No numbers allowed please.")
        
        for key, value in usernames.items():            
            '''The capitalization allows anyone to type in different cases for the name or username
                as long as they have the correct letter values it will come up in the search.'''
            if (name.capitalize() == key.capitalize()):
                print("Name: " + key,"&","Username: " + value)
                break
            elif (name.capitalize() == value.capitalize()):
                print("Name: " + key,"&","Username: " + value)
                break
        else:
            print ("Please enter a name or username that is on the list.")

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        try:
            print_menu()
        except:
            raise SystemExit("An unforseen error happend")

