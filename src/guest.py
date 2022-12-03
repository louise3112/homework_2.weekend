class Guest():
    
    def __init__(self, input_name, input_money, input_favourite_song):
        self.name = input_name
        self.money = input_money
        self.favourite_song = input_favourite_song
    
    def decrease_money(self, amount):
        self.money -= amount
    
    def cheer(self, song_name):
        if song_name == self.favourite_song:
            return "Whoo!"
    
