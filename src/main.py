"""
This modules is tha main module or entry point of the fresh-tomatoes app. Use this module to start the Fresh Tomatoes web app.
"""
from fresh_tomatoes import open_movies_page
from movies_list import MOVIES


if __name__ == '__main__':
    open_movies_page(MOVIES)
