#class movie which been used in main.pu

class Movie():
    def __init__(self, title, movieDes,poster_image_url, trailer_youtube_url):
        self.title =title
        self.movieDes = movieDes
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
