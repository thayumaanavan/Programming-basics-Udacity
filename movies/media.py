import webbrowser
class Movie():
    """This class contains movie related info"""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_url):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
