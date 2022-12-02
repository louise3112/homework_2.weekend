import unittest

from src.guest import Guest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.song import Song

class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Pop Room", 12)
        self.room_2 = Room("Punk Room", 8)
        self.ccc_rooms = [self.room_1, self.room_2]

        self.karaoke_bar_1 = KaraokeBar("CodeClan Caraoke", self.ccc_rooms)
    
    def test_karaoke_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.karaoke_bar_1.name)
    
    def test_karaoke_bar_has_rooms(self):
        self.assertEqual([self.room_1, self.room_2], self.karaoke_bar_1.rooms)
