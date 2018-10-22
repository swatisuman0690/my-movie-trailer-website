import webbrowser

class Movie():
     """ This class stores movie information such as title, poster image, youtube trailer """
     # class constructor
     def __init__(
         self, movie_title,
         poster_image_url,
         trailer_youtube_url
         ):
        # instance variables
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


        
