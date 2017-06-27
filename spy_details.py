from datetime import datetime

class Spy:

    def __init__ (self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__ (self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('riya', 'Ms.', 26, 4)
friend_two = Spy('madhu', 'Ms.', 24, 4.3)
friend_three = Spy('no', 'Dr.', 48, 3.8)


friends = [friend_one, friend_two, friend_three]
