# 38. Build a music playlist where songs are processed in arrival order using Queue

from collections import deque


class Playlist:
    def __init__(self):
        self.songs = deque()

    def add_song(self, song):
        self.songs.append(song)

    def play_next(self):
        if self.songs:
            return self.songs.popleft()
        return None


if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song("Song A")
    playlist.add_song("Song B")
    print("Now playing:", playlist.play_next())
    print("Next:", playlist.play_next())
