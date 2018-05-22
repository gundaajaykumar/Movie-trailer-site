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
#!/usr/bin/env python
2
import webbrowser
3
# take the webbrowser to run this python file
4
​
5
​
6
class Movie():
7
    # define a class and take an object self.
8
    def __init__(self, movie_name,
9
                 storyline_movie, movieposter_image, movietrailer_youtube):
10
                self.title = movie_name
11
                self.storyline = storyline_movie
12
                self.poster_image_url = movieposter_image
13
                self.trailer_youtube_url = movietrailer_youtube
14
​
15
    def show_trailer(self):
16
        webbrowser.open(self.trailer_youtube_url)
17
