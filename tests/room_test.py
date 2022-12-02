import unittest

from src.guest import Guest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Pop Room", 12)
        self.room_2 = Room("Punk Room", 8)

        self.song_1 = Song("Faith", "George Michael")
        self.song_2 = Song("Royals", "Lorde")
        self.song_3 = Song("Firework", "Katy Perry")

        self.guest_1 = Guest("Jane", 20)
        self.guest_2 = Guest("Brian", 21)
        self.guest_3 = Guest("Sarah", 25)
        self.list_of_guests = [self.guest_1, self.guest_2, self.guest_3]
    
    def test_room_has_name(self):
        self.assertEqual("Pop Room", self.room_1.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(12, self.room_1.capacity)
    
    def test_room_starts_with_no_songs(self):
        self.assertEqual([], self.room_1.songs)
    
    def test_room_starts_with_no_guests(self):
        self.assertEqual([], self.room_1.guests)
    
    def test_add_guests(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual([self.guest_1], self.room_1.guests)
    
    def test_remove_guests(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual([], self.room_1.guests)
    
    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual([self.song_1], self.room_1.songs)