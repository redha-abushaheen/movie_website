import webbrowser

class Movie():
    """This class provide a way to store movie variables"""
    def __init__(self, movie_title,movie_storyline,poster_image,trailer):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
#        super([object Object], self).__init__()
#        self.arg = arg
