import webbrowser


class Movie():
    """This class provide a way to store movie variables"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        """
        set up movie objects
        movie_title:string repesenting movie title
        movie_storyline:brief plot synopsis
        poster_image:movie image
        trailer: the triler for movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """open trailer in the browser"""
        webbrowser.open(self.trailer_youtube_url)

