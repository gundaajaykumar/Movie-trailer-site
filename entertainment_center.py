#!/usr/bin/env python
import media
import fresh_tomatoes
Jakkana = media.Ajay("Jakkana", "action and comedy",
                     "https://bit.ly/2IV9sDd",
                     "https://www.youtube.com/embed/RaO7Fyc1RMQ")
Paddanandipremalomari = media.Ajay("Paddanandipremalomari", "love",
                                   "https://bit.ly/2IWTbOa",
                                   "https://www.youtube.com/embed/16OL_60bnKc")
Titanic = media.Ajay("Titanic", "love",
                     "https://bit.ly/2wYtAzG",
                     "https://www.youtube.com/embed/2e-eXJ6HgkQ")
Shaolinsoccer = media.Ajay("Shaolinsoccer", "game oriented",
                           "https://bit.ly/2s02eTY",
                           "https://www.youtube.com/embed/KEWUDWYDdYs")
Tintin = media.Ajay("Tintin", "advantures",
                    "https://bit.ly/2kd4h3K",
                    "https://www.youtube.com/embed/xz3j8gKRUTg")
Ghajini = media.Ajay("Ghajini", "revange",
                     "https://bit.ly/2GyUwFO",
                     "https://youtu.be/_I0xx8Oj3Ww")
movies = [Jakkana, Paddanandipremalomari,
          Titanic, Shaolinsoccer, Tintin, Ghajini]
fresh_tomatoes.open_movies_page(movies)
