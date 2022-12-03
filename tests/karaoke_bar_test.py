import unittest

from src.guest import Guest
from src.karaoke_bar import KaraokeBar
from src.room import Room

class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Pop Room", 8)
        self.room_2 = Room("Punk Room", 2)
        self.ccc_rooms = [self.room_1, self.room_2]

        self.karaoke_bar_1 = KaraokeBar("CodeClan Caraoke", self.ccc_rooms, 100.00)

        self.guest_1 = Guest("Jane", 25.00, "Faith")
        self.guest_2 = Guest("Brian", 20.00, "Perfect")
        self.guest_3 = Guest("Sarah", 10.00, "Firework")
        self.guest_4 = Guest("Frank", 5.00, "Chandalier")
        self.group_1 = [self.guest_1, self.guest_2, self.guest_3]
        self.group_2 = [self.guest_1, self.guest_2, self.guest_4]
    
    def test_karaoke_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.karaoke_bar_1.name)
    
    def test_karaoke_bar_has_rooms(self):
        self.assertEqual([self.room_1, self.room_2], self.karaoke_bar_1.rooms)
    
    def test_karaoke_bar_has_till(self):
        self.assertEqual(100.00, self.karaoke_bar_1.till)
    
    def test_find_room(self):
        room = self.karaoke_bar_1.find_room("Pop Room")
        self.assertEqual(self.room_1, room)    

    def test_find_room__room_does_not_exist(self):
        room = self.karaoke_bar_1.find_room("Indie Room")
        self.assertEqual(False, room)
    
    def test_guest_check_in(self):
        self.karaoke_bar_1.guest_check_in("Pop Room", self.group_1)
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3], self.room_1.guests)
        self.assertEqual(30.00, self.room_1.revenue)
        self.assertEqual(15.00, self.guest_1.money)
        self.assertEqual(10.00, self.guest_2.money)
        self.assertEqual(0.00, self.guest_3.money)
    
    def test_guest_check_in__too_full(self):
        self.karaoke_bar_1.guest_check_in("Punk Room", self.group_1)
        self.assertEqual([], self.room_1.guests)
        self.assertEqual(0.00, self.room_1.revenue)
        
    def test_guest_check_in__cant_all_afford_entry(self):
        self.karaoke_bar_1.guest_check_in("Pop Room", self.group_2)
        self.assertEqual([self.guest_1, self.guest_2], self.room_1.guests)
        self.assertEqual(20.00, self.room_1.revenue)
        self.assertEqual(15.00, self.guest_1.money)
        self.assertEqual(10.00, self.guest_2.money)
        self.assertEqual(5.00, self.guest_4.money)

    def test_guest_check_out(self):
        self.karaoke_bar_1.guest_check_in("Pop Room", self.group_1)
        self.karaoke_bar_1.guest_check_out("Pop Room", self.group_1)
        self.assertEqual([], self.room_1.guests)

    def test_collect_money_from_rooms(self):
        self.karaoke_bar_1.guest_check_in("Pop Room", self.group_1)
        self.karaoke_bar_1.collect_money_from_rooms()
        self.assertEqual(130.00, self.karaoke_bar_1.till)
        self.assertEqual(0.00, self.room_1.revenue)
