class Movie:
    """This class is a structure for storing a movie"""

    def __init__(self, title, poster_image_url, trail_youtube_url, imdb_rating, year):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trail_youtube_url
        self.imdb_rating = imdb_rating
        self.year = year
