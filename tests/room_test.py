import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Pop Room", 8)
        self.room_2 = Room("Punk Room", 2)

        self.song_1 = Song("Faith", "George Michael")
        self.song_2 = Song("Royals", "Lorde")
        self.song_3 = Song("Firework", "Katy Perry")

        self.guest_1 = Guest("Jane", 25.00, "Faith")
        self.guest_2 = Guest("Brian", 20.00, "Perfect")
        self.guest_3 = Guest("Sarah", 10.00, "Firework")
        self.list_of_guests = [self.guest_1, self.guest_2, self.guest_3]
    
    def test_room_has_name(self):
        self.assertEqual("Pop Room", self.room_1.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(8, self.room_1.capacity)
    
    def test_room_starts_with_no_songs(self):
        self.assertEqual([], self.room_1.songs)
    
    def test_room_starts_with_no_guests(self):
        self.assertEqual([], self.room_1.guests)

    def test_room_has_revenue(self):
        self.assertEqual(0.00, self.room_1.revenue)
    
    def test_increase_revenue(self):
        self.room_1.increase_revenue(5.00)
        self.assertEqual(5.00, self.room_1.revenue)
    
    def test_check_guest_can_pay__True(self):
        can_pay = self.room_1.check_guest_can_pay(self.guest_1, 5.00)
        self.assertEqual(True, can_pay)
        
    def test_check_guest_can_pay__False(self):
        can_pay = self.room_1.check_guest_can_pay(self.guest_1, 35.00)
        self.assertEqual(False, can_pay)
    
    def test_add_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual([self.guest_1], self.room_1.guests)
        self.assertEqual(10.00, self.room_1.revenue)
        self.assertEqual(15.00, self.guest_1.money)
    
    def test_remove_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual([], self.room_1.guests)

    def test_calculate_remaining_capacity(self):
        self.room_1.add_guest(self.guest_1)
        remaining_capacity = self.room_1.calculate_remaining_capacity()
        self.assertEqual(7, remaining_capacity)
    
    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual([self.song_1], self.room_1.songs)
    
    def test_song_is_available__True(self):
        self.room_1.add_song(self.song_1)
        song_available = self.room_1.song_is_available("Faith")
        self.assertEqual("George Michael", song_available)
    
    def test_song_is_available__False(self):
        self.room_1.add_song(self.song_1)
        song_available = self.room_1.song_is_available("Fireworks")
        self.assertEqual(None, song_available)
    
    def test_play_song__favourite(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_song(self.song_1)
        playing = self.room_1.play_song("Faith")
        self.assertEqual("Playing Faith by George Michael! Whoo!", playing)
    
    def test_play_song__not_favourite(self):
        self.room_1.add_guest(self.guest_2)
        self.room_1.add_song(self.song_1)
        playing = self.room_1.play_song("Faith")
        self.assertEqual("Playing Faith by George Michael!", playing)

    def test_play_song__song_not_found(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_song(self.song_1)
        playing = self.room_1.play_song("Fireworks")
        self.assertEqual("Fireworks is not available", playing)
        
    def test_clear_revenue(self):
        self.room_1.clear_revenue()
        self.assertEqual(0.00, self.room_1.revenue)