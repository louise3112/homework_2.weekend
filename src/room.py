class Room():
    def __init__(self, input_name, input_capacity):
        self.name = input_name
        self.capacity = input_capacity
        self.songs = []
        self.guests = []
        self.revenue = 0.00
        self.entry_fee = 10.00
    
    def increase_revenue(self, amount):
        self.revenue += amount
    
    def check_guest_can_pay(self, guest, amount):
        if guest.money >= amount:
            return True
        else:
            return False

    def add_guest(self, guest):
        if self.check_guest_can_pay(guest, self.entry_fee):
            self.increase_revenue(self.entry_fee)
            guest.decrease_money(self.entry_fee)
            self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)
    
    def calculate_remaining_capacity(self):
        return self.capacity - len(self.guests)
    
    def add_song(self, song):
        self.songs.append(song)
    
    def clear_revenue(self):
        self.revenue = 0.00

