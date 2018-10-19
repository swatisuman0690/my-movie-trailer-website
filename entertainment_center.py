import media
import fresh_tomatoes


# define instances
venom = media.Movie(
    "Venom",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Venom_poster.jpg",
    "https://www.youtube.com/watch?reload=9&v=u9Mv98Gr5pY"
    )

                        
captain_marvel = media.Movie(
    "Captain Marvel",
    "https://upload.wikimedia.org/wikipedia/en/8/85/Captain_Marvel_poster.jpg",
    "https://www.youtube.com/watch?v=Z1BCujX3pw8"
    )


aquaman = media.Movie(
    "Aquaman",
    "https://upload.wikimedia.org/wikipedia/en/3/3a/Aquaman_poster.jpg",
    "https://www.youtube.com/watch?v=VMzYtgzYO7U"
    )


shazam = media.Movie(
    "Shazam!",
    "https://upload.wikimedia.org/wikipedia/en/7/74/Shazam_film_poster.jpg",
    "https://www.youtube.com/watch?v=-oD7B7oiBtw"
    )


antman_and_the_wasp = media.Movie(
    "Ant-Man and the Wasp",
    "https://upload.wikimedia.org/wikipedia/en/2/2c/Ant-Man_and_the_Wasp_poster.jpg",
    "https://www.youtube.com/watch?v=8_rTIAOohas"
    )


avengers_infinity_war = media.Movie(
    "Avengers infinity war",
    "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
    "https://www.youtube.com/watch?v=6ZfuNTqbHE8"
    )


# movies list to store instances
movies = [
    venom,
    captain_marvel,
    aquaman, shazam,
    antman_and_the_wasp,
    avengers_infinity_war
    ]


def main():
    # insert movies as parameter
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()
