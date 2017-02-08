import media

toyStory=media.Movie("Toy Story",
                    "A Story of a boy and his toys that come to life",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                    "https://www.youtube.com/watch?v=KYz2wyBy3kc")


print toyStory.storyline

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print avatar.storyline
avatar.show_trailer()
