import media
import fresh_tomatoes

the_matrix = media.Movie(
    "The Matrix",
    "",
    "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8"    
)

fight_club = media.Movie(
    "Fight Club",
    "",
    "https://m.media-amazon.com/images/M/MV5BMjJmYTNkNmItYjYyZC00MGUxLWJhNWMtZDY4Nzc1MDAwMzU5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg"
)

interestellar = media.Movie(
    "Interestellar",
    "",
    "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E"
)

movies = [
    the_matrix,
    fight_club,
    interestellar
]

fresh_tomatoes.open_movies_page(movies)