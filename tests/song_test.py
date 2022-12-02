import unittest

from src.guest import Guest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Faith", "George Michael")
    
    def test_song_has_name(self):
        self.assertEqual("Faith", self.song_1.name)
    
    def test_song_has_artist(self):
        self.assertEqual("George Michael", self.song_1.artist)