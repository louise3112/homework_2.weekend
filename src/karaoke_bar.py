class KaraokeBar():
    
    def __init__(self, input_name, input_rooms):
        self.name = input_name
        self.rooms = input_rooms

        self.till = 100.00
    
    def find_room(self, room_name):
        for room in self.rooms:
            if room.name == room_name:
                return room
        return False
    
    def guest_check_in(self, room_name, group):
        room = self.find_room(room_name)
        remaining_capacity = room.calculate_remaining_capacity()
        if room != False and len(group) <= remaining_capacity:
            for guest in group:
                room.add_guest(guest)

    def guest_check_out(self, room_name, group):
        room = self.find_room(room_name)
        if room != False:
            for guest in group:
                room.remove_guest(guest)
    
    def collect_money_from_rooms(self):
        for room in self.rooms:
            self.till += room.revenue
            room.clear_revenue()
    