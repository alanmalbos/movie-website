import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	"A history of a boy and his toys become to life",
	"/home/alanmalbos/version-control/movie-website/toy_story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

print toy_story.storyline

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"/home/alanmalbos/version-control/movie-website/avatar.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

print avatar.storyline

the_godfather = media.Movie("The Godfather",
	"A history of a mob family fight against their enemies",
	"/home/alanmalbos/version-control/movie-website/the_godfather.jpg",
	"https://www.youtube.com/watch?v=sY1S34973zA")

movies = []
movies.append(toy_story)
movies.append(avatar)
movies.append(the_godfather)

fresh_tomatoes.open_movies_page(movies)