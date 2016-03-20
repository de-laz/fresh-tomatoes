"""
This modules is tha main module or entry point of the fresh-tomatoes app. Use this module to start the Fresh Tomatoes web app.
"""
from fresh_tomatoes import open_movies_page
from media import Movie

YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v={}"  # Youtube base url for trailers.


def create_favourite_movies():
    """This function creates and returns a list of movies."""

    forest_gump = Movie(
        "Forest Gump",
        "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
        YOUTUBE_BASE_URL.format("bLvqoHBptjg"),
        8.8,
        1994)

    zohan = Movie(
        "You don't mess with the Zohan",
        "https://upload.wikimedia.org/wikipedia/en/7/77/With_the_zohan.jpg",
        YOUTUBE_BASE_URL.format("u_I1cW14Qlg"),
        5.5,
        2008)

    deadpool = Movie(
        "Deadpool",
        "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
        YOUTUBE_BASE_URL.format("Xithigfg7dA"),
        8.4,
        2016)

    the_godfather = Movie(
        "The Godfather",
        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
        YOUTUBE_BASE_URL.format("5DO-nDW43Ik"),
        9.2,
        1972)

    the_fellowship_of_the_ring = Movie(
        "The Lord of The Rings: The Fellowship of the Ring",
        "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
        YOUTUBE_BASE_URL.format("V75dMMIW2B4"),
        8.8,
        2001)

    the_two_towers = Movie(
        "The Lord of The Rings: The Two Towers",
        "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
        YOUTUBE_BASE_URL.format("LbfMDwc4azU"),
        8.7,
        2002)

    the_return_of_the_king = Movie(
        "The Lord of The Rings: The Return of The King",
        "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
        YOUTUBE_BASE_URL.format("r5X-hFf6Bwo"),
        8.9,
        2003)

    return [forest_gump,
            zohan,
            deadpool,
            the_godfather,
            the_fellowship_of_the_ring,
            the_two_towers,
            the_return_of_the_king]


if __name__ == '__main__':
    favourite_movies = create_favourite_movies()
    open_movies_page(favourite_movies)
