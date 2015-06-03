__author__ = 'fhk'
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipredia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# print toy_story.storyline

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser_Post",
                     "https://www.youtube.com/watch?v=cX0R3mXaod8")

# print avatar.storyline
# avatar.show_trailer()

stand_by_me = media.Movie("Stand By Me",
                          "A machine cat travel back to help a loser persuit his happiness",
                          "http://img4.douban.com/view/photo/raw/public/p2243624548.jpg",
                          "http://movie.douban.com/trailer/175619/#content")

stand_by_me.show_trailer()

