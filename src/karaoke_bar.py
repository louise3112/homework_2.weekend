class KaraokeBar():
    
    def __init__(self, input_name, input_rooms):
        self.name = input_name
        self.rooms = input_rooms
    
    def find_room(self, room_name):
        for room in self.rooms:
            if room.name == room_name:
                return room
        return False
    
    def guest_check_in(self, room_name, list_of_guests):
        room = self.find_room(room_name)
        if room != False:
            for guest in list_of_guests:
                room.add_guest(guest)

    def guest_check_out(self, room_name, list_of_guests):
        room = self.find_room(room_name)
        if room != False:
            for guest in list_of_guests:
                room.remove_guest(guest)