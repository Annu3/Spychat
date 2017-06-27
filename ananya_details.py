from datetime import datetime

# Spy class features
class Spy:

    # important things we want to know about our spy
    def __init__ (self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

# chat message class is created
class ChatMessage:
    # constructor is defined
    def __init__ (self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

# own spy is created
spy = Spy('Annu', 'Ms.', 24, 4.7)

# spy friends
friend_one = Spy('Riya', 'Ms.', 26, 4)
friend_two = Spy('Madhu', 'Ms.', 24, 4.3)
friend_three = Spy('Nikita', 'Dr.', 48, 3.8)


friends = [friend_one, friend_two, friend_three]
