import unittest

from src.guest import Guest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Jane", 20)
    
    def test_guest_has_name(self):
        self.assertEqual("Jane", self.guest_1.name)
    
    def test_guest_has_age(self):
        self.assertEqual(20, self.guest_1.age)

