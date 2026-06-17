class Song:
    """
    A Song class that represents individual songs and maintains global insights
    about the music library including total count, unique artists/genres, 
    and counts per artist/genre.
    """
    
    # Class attributes to maintain global state across all Song instances
    count = 0  # Total number of songs created
    genres = set()  # Set of unique genres
    artists = set()  # Set of unique artists
    genre_count = {}  # Dictionary mapping genres to song counts
    artist_count = {}  # Dictionary mapping artists to song counts
    
    def __init__(self, name, artist, genre):
        """
        Initialize a Song instance with name, artist, and genre.
        Automatically updates all class attributes when a new song is created.
        
        Args:
            name (str): The name/title of the song
            artist (str): The artist who performed the song
            genre (str): The genre classification of the song
        """
        # Store instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class attributes
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
    
    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by one."""
        cls.count += 1
    
    def add_to_genres(self):
        """
        Add the current song's genre to the genres set.
        The set automatically ensures uniqueness - no duplicates.
        """
        Song.genres.add(self.genre)
    
    def add_to_artists(self):
        """
        Add the current song's artist to the artists set.
        The set automatically ensures uniqueness - no duplicates.
        """
        Song.artists.add(self.artist)
    
    def add_to_genre_count(self):
        """
        Update the genre_count dictionary.
        Increments the count for the song's genre, or adds it if it doesn't exist.
        """
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
    
    def add_to_artist_count(self):
        """
        Update the artist_count dictionary.
        Increments the count for the song's artist, or adds it if it doesn't exist.
        """
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
