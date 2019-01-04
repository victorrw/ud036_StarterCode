class Movie():
    """ Construct the movie class.
        Attributes:
        title (str): movie title
        box_art (str): movie brief description
        poster_image_url (str): link with the movie poster image
        trailer_youtube_url (str): link of the movie\'s youtube trailer
    """
        
    def __init__(self, title, box_art, poster_image_url, trailer_youtube_url):
        self.title = title
        self.box_art = box_art
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url