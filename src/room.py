class Room():
    def __init__(self, input_name, input_capacity):
        self.name = input_name
        self.capacity = input_capacity
        self.songs = []
        self.guests = []
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)

