import media
import fresh_tomatoes

the_matrix = media.Movie(
    "The Matrix",
    "The Matrix is a 1999 science fiction action film written and directed by The Wachowskis and starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano It depicts a dystopian future in which reality as perceived by most humans is actually a simulated reality called \"the Matrix\", created by sentient machines to subdue the human population, while their bodies' heat and electrical activity are used as an energy source. Cybercriminal and computer programmer Neo learns this truth and is drawn into a rebellion against the machines, which involves other people who have been freed from the \"dream world.\"", # noqa
    "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg", #noqa
    "https://www.youtube.com/watch?v=vKQi3bBA1y8"    
)

fight_club = media.Movie(
    "Fight Club",
    "Fight Club is a 1999 film based on the 1996 novel by Chuck Palahniuk. It was directed by David Fincher and stars Brad Pitt, Edward Norton, and Helena Bonham Carter. Norton plays the unnamed narrator, who is discontent with his white-collar job. He forms a \"fight club\" with soap salesman Tyler Durden (Pitt), and becomes embroiled in a relationship with him and a destitute woman, Marla Singer (Bonham Carter).", # noqa
    "https://m.media-amazon.com/images/M/MV5BMjJmYTNkNmItYjYyZC00MGUxLWJhNWMtZDY4Nzc1MDAwMzU5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,676,1000_AL_.jpg", # noqa
    "https://www.youtube.com/watch?v=SUXWAEX2jlg"
)

interestellar = media.Movie(
    "Interestellar",
    "Interstellar is a 2014 science fiction film directed, co-written, and co-produced by Christopher Nolan. It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, and Michael Caine. Set in a dystopian future where humanity is struggling to survive, the film follows a group of astronauts who travel through a wormhole in search of a new home for humanity.", # noqa
    "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg", # noqa
    "https://www.youtube.com/watch?v=zSWdZVtXT7E"
)

movies = [
    the_matrix,
    fight_club,
    interestellar
]

fresh_tomatoes.open_movies_page(movies)