"""
This modules is tha main module or entry point of the fresh-tomatoes app. Use this module to start the Fresh Tomatoes web app.
"""
from fresh_tomatoes import open_movies_page
from media import Movie

YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v=" # Youtube base url for trailers.

def create_favourite_movies():
    forest_gump = Movie("Forest Gump", "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
            "{}bLvqoHBptjg".format(YOUTUBE_BASE_URL), 8.8, 1994)

    zohan = Movie("You don't mess with the Zohan", "https://upload.wikimedia.org/wikipedia/en/7/77/With_the_zohan.jpg",
            "{}u_I1cW14Qlg".format(YOUTUBE_BASE_URL), 5.5, 2008)

    deadpool = Movie("Deadpool", "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
            "{}Xithigfg7dA".format(YOUTUBE_BASE_URL), 8.4, 2016)

    the_godfather = Movie("The Godfather", "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
            "{}5DO-nDW43Ik".format(YOUTUBE_BASE_URL), 9.2, 1972)

    return [forest_gump, zohan, deadpool, the_godfather]


if __name__ == '__main__':
    favourite_movies = create_favourite_movies()
    open_movies_page(favourite_movies)
