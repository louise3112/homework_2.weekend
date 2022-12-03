import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Jane", 25.00, "Faith")
    
    def test_guest_has_name(self):
        self.assertEqual("Jane", self.guest_1.name)
    
    def test_guest_has_money(self):
        self.assertEqual(25.00, self.guest_1.money)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Faith", self.guest_1.favourite_song)
    
    def test_decrease_money(self):
        self.guest_1.decrease_money(5.00)
        self.assertEqual(20.00, self.guest_1.money)
    
    def test_cheer(self):
        cheer = self.guest_1.cheer("Faith")
        self.assertEqual("Whoo!", cheer)


