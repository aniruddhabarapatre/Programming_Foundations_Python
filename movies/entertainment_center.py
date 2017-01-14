import media
import fresh_tomatoes

'''
Contains list of movies to display
Each movie consists of name, description, movie poster and trailer url
'''

toy_story = media.Movie("Toy Story",
                        "A story of boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

kubo = media.Movie("Kubo and the Two Strings",
                    "A young boy named Kubo must locate a magical suit of armor worn by his late"
                    " father in order to defeat a vengeful spirit from the past.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c4/Kubo_and_the_Two_Strings_poster.png",
                    "https://www.youtube.com/watch?v=oPEz0EYihzE")

jungle_book = media.Movie("The Jungle Book",
                    "A story of a boy raised among wolves in jungle",
                    "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
                    "https://www.youtube.com/watch?v=TmLRj9zm5SE")

zootopia = media.Movie("Zootopia",
                    "A bunny cop and a fox solves a mystery",
                    "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                    "https://www.youtube.com/watch?v=1ZOHlq6Qcz0")

movies = [avatar, toy_story, kubo, jungle_book, zootopia]

fresh_tomatoes.open_movies_page(movies)
