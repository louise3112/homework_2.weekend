import unittest

from src.guest import Guest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.song import Song

class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Pop Room", 8)
        self.room_2 = Room("Punk Room", 2)
        self.ccc_rooms = [self.room_1, self.room_2]

        self.karaoke_bar_1 = KaraokeBar("CodeClan Caraoke", self.ccc_rooms)

        self.guest_1 = Guest("Jane", 20)
        self.guest_2 = Guest("Brian", 21)
        self.guest_3 = Guest("Sarah", 25)
        self.list_of_guests = [self.guest_1, self.guest_2, self.guest_3]
    
    def test_karaoke_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.karaoke_bar_1.name)
    
    def test_karaoke_bar_has_rooms(self):
        self.assertEqual([self.room_1, self.room_2], self.karaoke_bar_1.rooms)
    
    def test_find_room(self):
        room = self.karaoke_bar_1.find_room("Pop Room")
        self.assertEqual(self.room_1, room)    

    def test_find_room__room_does_not_exist(self):
        room = self.karaoke_bar_1.find_room("Indie Room")
        self.assertEqual(False, room)
    
    def test_guest_check_in(self):
        self.karaoke_bar_1.guest_check_in("Pop Room", self.list_of_guests)
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3], self.room_1.guests)

    def test_guest_check_out(self):
        self.karaoke_bar_1.guest_check_in("Pop Room", self.list_of_guests)
        self.karaoke_bar_1.guest_check_out("Pop Room", self.list_of_guests)
        self.assertEqual([], self.room_1.guests)
        
