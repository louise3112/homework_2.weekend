class Room():
    def __init__(self, input_name, input_capacity, input_bar):
        self.name = input_name
        self.capacity = input_capacity
        self.songs = []
        self.guests = []
        self.revenue = 0.00
        self.entry_fee = 10.00
        self.bar = input_bar
    
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
    
    def find_bar_item(self, item_name):
        for item in self.bar:
            if item["name"] == item_name:
                return item
    
    def reduce_stock(self, item):
        item["stock"] -= 1

    def stock_available(self, item):
        if item["stock"] > 0:
            return True
        else:
            return False

    def sell_from_bar(self, guest_in_room, item_name):
        item = self.find_bar_item(item_name)
        if self.stock_available(item) == True and self.check_guest_can_pay(guest_in_room, item["price"]) == True:
            self.increase_revenue(item["price"])
            guest_in_room.decrease_money(item["price"])
            self.reduce_stock(item)
