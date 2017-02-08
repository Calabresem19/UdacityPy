import webbrowser

class Movie():
        def __init__(self, MovieTitle, MovieStoryLine, PosterImage, trailerYoutube):
            self.title = MovieTitle
            self.storyline = MovieStoryLine
            self.posterImageUrl = PosterImage
            self.trailerYoutubeUrl = trailerYoutube

        def show_trailer(self):
            webbrowser.open(self.trailerYoutubeUrl)
