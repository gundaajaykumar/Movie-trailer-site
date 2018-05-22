#!/usr/bin/env python
import webbrowser
# take the webbrowser to run this python file


class Movie():
    # define a class and take an object self.
    def __init__(self, movie_name,
                 storyline_movie, movieposter_image, movietrailer_youtube):
                self.title = movie_name
                self.storyline = storyline_movie
                self.poster_image_url = movieposter_image
                self.trailer_youtube_url = movietrailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
