#!/usr/bin/env python
import media
# here imported the media.py file.
import fresh_tomatoes
# here imported the fresh_tomatoes.py file.
Jakkana = media.Movie("Jakkana", "action and comedy",
                      "https://bit.ly/2IV9sDd",
                      "https://www.youtube.com/embed/RaO7Fyc1RMQ")
Ppremalomari = media.Movie("Paddanandipremalomari", "love",
                           "https://bit.ly/2IWTbOa",
                           "https://www.youtube.com / embed/16OL_60bnKc")
Titanic = media.Movie("Titanic", "love",
                      "https://bit.ly/2wYtAzG",
                      "https://www.youtube.com/embed/2e-eXJ6HgkQ")
Shaolinsoccer = media.Movie("Shaolinsoccer", "game oriented",
                            "https://bit.ly/2s02eTY",
                            "https://www.youtube.com/embed/KEWUDWYDdYs")
Tintin = media.Movie("Tintin", "advantures",
                     "https://bit.ly/2kd4h3K",
                     "https://www.youtube.com/embed/xz3j8gKRUTg")
Ghajini = media.Movie("Ghajini", "revange",
                      "https://bit.ly/2GyUwFO",
                      "https://youtu.be/_I0xx8Oj3Ww")
''' here we connected the class Movie in media.py file
and taken the movies information in tuple format'''
movies = [Jakkana, Ppremalomari,
          Titanic, Shaolinsoccer, Tintin, Ghajini]
fresh_tomatoes.open_movies_page(movies)
# in fresh_tomatoes we open the open_movie_page with above movies.
