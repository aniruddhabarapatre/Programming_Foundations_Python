import webbrowser


class Movie():
    """ This class stores movie related info """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ Constructor for Movie
            Args:
                movie_title: title or name of movie
                movie_storyline: short description of movie
                poster_image: url of movie poster
                trailer_youtube: url of youtube trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # shows trailer using youtube url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
