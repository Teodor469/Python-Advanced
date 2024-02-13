from collections import defaultdict

def movie_organizer(*movies):
    genre_movies = defaultdict(list)
    
    for movie_name, genre in movies:
        genre_movies[genre].append(movie_name)

    for genre, movies in genre_movies.items():
        genre_movies[genre] = sorted(movies)

    sorted_genres = sorted(genre_movies.items(), key=lambda x: (-len(x[1]), x[0]))

    output = ""
    for genre, movies in sorted_genres:
        output += f"{genre} - {len(movies)}\n"
        for movie in movies:
            output += f"* {movie}\n"
        output += "\n"

    return output.strip()


result = movie_organizer(("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy"))

print(result.strip())