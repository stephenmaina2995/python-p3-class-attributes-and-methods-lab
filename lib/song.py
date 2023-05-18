class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 1
        else:
            Song.genre_count[self.genre] += 1
