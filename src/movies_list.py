from models import Movie

YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="

MOVIES = [
    Movie("Forest Gump", "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
          "{}bLvqoHBptjg".format(YOUTUBE_BASE_URL), 8.8, 1994),
    Movie("You don't mess with the Zohan", "https://upload.wikimedia.org/wikipedia/en/7/77/With_the_zohan.jpg",
          "{}u_I1cW14Qlg".format(YOUTUBE_BASE_URL), 5.5, 2008),
]
