# without specifying spy_details when printing them
from ananya_details import spy, Spy, ChatMessage, friends

#import steganography
from steganography.steganography import Steganography

#import datetime
from datetime import datetime

#import termcolor
from termcolor import colored

special_messages = ['SAVE ME', 'SOS' , 'HELP ME']

# list that has some default statuses inside it
STATUS_MESSAGES =['My name is Anu, Ananya Gupta', 'Have a nice day.', 'Keep Calm and relax']


# print the string
print (colored( 'What\'s up?','blue'))
print (colored('Why should I learn python?','magenta'))

print (colored('Because it is very easy language','yellow'))
print (colored('Let\'s get started','green'))

# give user the option to continue with the default user or define a new user
question = "Do you wish to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "

# ask for the name of the spy
existing = raw_input("What is your name?")

# adding the status function
def add_status():

    updated_status_message = None

#  feature to update the status.
    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

#  option to choose from the existing status update
    default = raw_input(colored("Do you wish to select from the existing status (y/n)? ",'red'))

# spy wants to enter a new status update
    if default.upper() == "N":
        new_status_message = raw_input("Which status message you want to update? ")
        if len(new_status_message) > 0:

    # add new values to the end of the list
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    # print each element in  list of statuses using For Loop
    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

# The user wants to select the desired status by giving the number
        message_selection = int(raw_input("\nChoose from the  above messages "))

# check if the number entered by the user is valid
        if len(STATUS_MESSAGES) >= message_selection:
# user selects from existing status updates and then we will set it as the updated status
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you have chosen is invalid! Press either y or n.'

    if updated_status_message:
        print (colored('Your updated status message is: %s','magenta')) % (updated_status_message)
    else:
        print 'Your current account don\'t have a status updated'

# returns updated status message
    return updated_status_message

# asks the user for name, age and rating of their spy friend.
def add_friend():

#  float variable in python
    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input(colored("Please add your friend's name: ",'magenta'))
    new_friend.salutation = raw_input(colored("Are they Mr. or Ms.?: ",'yellow'))

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input(colored("Please  add your friend's Age?",'blue'))
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input(colored("Please add your friend's Spy rating?",'red'))
    new_friend.rating = float(new_friend.rating)

# additional conditions add friend
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Your Friend is Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

#  returning the total number of friends the user has
    return len(friends)

#  print all details that are stored in each element of friends list
def select_a_friend():
    item_number = 0

    for friend in friends:

       # Asking the user to select a friend
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

# Taking input from the user
    friend_choice = raw_input("Choose from your above friends")

# Returning  index
    friend_choice = int(friend_choice) - 1

    return friend_choice


# sending the secret message to the user
def send_message():

#  returns position of the friend to whom you need to send  message
    friend_choice = select_a_friend()

    original_image = raw_input(colored("What is the name of your image?",'yellow'))
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")

    # encode function in stegnography
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

# when image contains no secret message
    if len(text)>0:
        print "Your secret message image is ready!"

    else:
        print "Please enter secret message....You can't go further!!!!"

# reading the  secret message from the user
def read_message(n=None):

# gain  index of the friend whose message is to be read
    sender = select_a_friend()

    output_path = raw_input(colored("What is the name of your image file?",'magenta'))

    # decode function in stegnography

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)


# secret message that is decoded with current timestamp
    print 'Your secret_text have been saved!'

# special words sent by spy then appropriate message displayed by user
    if secret_text in special_messages:
     print (colored("Just relax!\n",'blue'))
     print (colored("We are coming to save you!\n",'cyan'))
     print (colored("We are here to help you!\n",'green'))



 # function to read chat history of a friend
def read_chat_history():

# get the position of the friend whose chat we want to read
    read_for = select_a_friend()

    print '\n6'

# check if the chat was sent by the active user or some other spy
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (colored(chat.time.strftime("%d %B %Y"),'red'),colored("You said:",'blue'),colored(chat.message,'red'))
    else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"),colored(friends[read_for].name,'green'),colored(chat.message,'magenta'))

# Delete a spy from your list of spies if they are speaking too much
def delete_friends():
    sender = select_a_friend()
    for friend in friends:

        print 'Your current friend is:=', friends

        text = raw_input("Enter the text")

        if len(text)>5:

            del friends[sender]
        else:
            print 'none of your friends are deleted'


# starting the chat function
def start_chat(spy):
 # code refactoring
    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:

     # Final message with all the details
     print (colored("Authentication complete. Welcome ",'blue'))+ (colored(spy.name,'magenta')) + (colored(" age: "
           + str(spy.age),'green')) + (colored(" and rating of: " + str(spy.rating),'yellow'))+ " Glad to have you back with us"

     show_menu = True

     # menu consisting of the option to update the status.
    while show_menu:
            menu_choices = (colored("What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Delete friends \n 7. Exit Application \n ",'red'))
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
           # Add status update
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                  send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                elif menu_choice == 6:
                    delete_friends()
                else:
                    show_menu = False
      # exit application
    else:
        print (colored('Sorry you are not eligible to be a spy','magenta'))

if existing == "Y":
     start_chat(spy)
else:
    spy = Spy('','',0,0.0)
 #  condition  to check if our spy has provided us with a valid name or not
    spy.name = raw_input(colored("Welcome to Spy chat window, you must tell me your spy chat name first: ",'red'))

    # block of code
    if len(spy.name) > 0:

        spy.salutation = raw_input(colored("Should I call you Mr. or Ms.?: ",'red'))

        # asking for the age of spy
        spy.age = raw_input(colored("What is your age?",'cyan'))
        spy.age = int(spy.age)

        # asking for the spy rating
        spy.rating = raw_input(colored("What is your spy rating?",'blue'))
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
