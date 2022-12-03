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
    
    def song_is_available(self, song_name):
        for song in self.songs:
            if song.name == song_name:
                return song.artist

    
    def play_song(self, song_name):
        for guest in self.guests:
            if self.song_is_available(song_name) != None and guest.cheer(song_name) != None:
                return f"Playing {song_name} by {self.song_is_available(song_name)}! {guest.cheer(song_name)}"
            elif self.song_is_available(song_name) != None:
                return f"Playing {song_name} by {self.song_is_available(song_name)}!"
            else:
                return f"{song_name} is not available"
    
    def clear_revenue(self):
        self.revenue = 0.00

